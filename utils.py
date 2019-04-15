# -*- coding: utf-8 -*-
# utility functions and text parsing classes/helper functions

import urllib3
import xml.etree.ElementTree as ET
import os
import re
import json
import errno
import unicodedata


# ==============================================================================
# ==============================================================================
# ==============================================================================
# Useful utility functions

# check if the given file path exists, and if not create it.
# based on Krumelur's answer to
# http://stackoverflow.com/questions/12517451/python-automatically-creating-directories-with-file-output
def check_and_create_path(filename):
    if (not os.path.exists(os.path.dirname(filename))):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

# true if the file exists
def fileExists(filename):
    return os.path.isfile(filename)


# write content to the file at filename. Make the directory path to the given
# file if it does not exist.
def safeWrite(filename, content, dumpJSON=False):
    check_and_create_path(filename)
    out_file = open(filename, "w")
    if dumpJSON:
        content = json.dumps(content)
    out_file.write(content)
    out_file.close()

# get the content from a given file by reading it
# parseJSON is true if we should parse the contents as JSON first
def getContent(inFileName, parseJSON):
    inFile = open(inFileName, 'r')
    inContents = inFile.read()
    inFile.close()
    if parseJSON:
        return json.loads(inContents)
    else:
        return inContents

# ==============================================================================
# ==============================================================================
# ==============================================================================
# Objects for storing authors and texts

# store an author
class Author:
    def __init__(self, name):
        self.authorName = name
        self.works = []

        # list of this author's tokens
        self.allTokens = []

        # indices of book split tokens
        self.bookSplits = {}

        # raw frequency of tokens
        self.tokenFreqs = None
        # total number of tokens for this author
        self.totalTokenCount = None

        # feature data associated with this author
        self.featureData = None
        self.unNormalizedFeatureData = None

    # get the name for saving this author
    def getSaveName(self):
        return self.authorName

    # add a work to this author's list of works
    def addWork(self, work):
        self.works.append(work)

    # download and save all of this author's works
    def downloadAndSaveWorks(self, path, downloadedWorks, oldAuthorWorksList, verbose):
        # ignore already downloaded works
        worksToDownload = []
        for work in self.works:
            if not(work.textName in downloadedWorks):
                worksToDownload.append(work)

        # count the number of texts
        numTexts = len(worksToDownload)


        res = oldAuthorWorksList
        for i in range(len(worksToDownload)):
            work = worksToDownload[i]
            print("    %s. %.2f%% (%d/%d)" % (work.textName, (100*(i+1)/numTexts), (i+1), numTexts))
            try:
                res.append(work.downloadAndSaveText(path, self.authorName, verbose))
            except Exception as e:
                print("    Work failed to download.")
                print(e)

        print("%s Done." % self.authorName)
        return {
            "author": self.authorName,
            "works": res
        }

    def __str__(self):
        return ("%s (%d works)." %(self.authorName, len(self.works)))

# store information needed to download a text
class TextSpec:
    def __init__(self, name, id, books, infix, cardList):
        self.textName = name
        self.textPerseusID = id
        self.numBooks = books
        self.infix = infix
        self.cardList = cardList
        if (len(cardList["suffixes"]) == 0):
            self.downloadFromCards = False
        else:
            self.downloadFromCards = True
        self.loaded = False
        self.books = []

    # convert from name into a proper filename
    def getTextFname(self):
        r = self.textName.replace(" ", "_")
        return r

    # Download text based on the spec.
    def downloadAndSaveText(self, path, author, verbose):
        saveLoc = path + author + "-" + self.getTextFname() + ".json"
        allBooks = []
        urlBase = "http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus%3Atext%3A" + self.textPerseusID + self.infix
        if(self.downloadFromCards):
            if self.cardList["multi"]:
                for s in self.cardList["suffixes"]:
                    bookNum = s["bookNum"]
                    bookPieces = []
                    for c in s["suffs"]:
                        url = urlBase + s["infix2"] + str(c)
                        if (verbose):
                            print(url)
                        xml = get_TEI_XML(url, False)
                        #bookPieces.append(parse_TEI_full_book(xml))
                        bookPieces.append(xml)
                    #bookText = removePunct(" ".join(bookPieces))
                    bookText = " ".join(bookPieces)
                    if (verbose):
                        print(bookText)
                    allBooks.append({
                        "bookNumber": bookNum,
                        "bookText": bookText
                    })
            else:
                bookNum = 1
                bookPieces = []
                for c in self.cardList["suffixes"]:
                    url = urlBase + str(c)
                    if (verbose):
                        print(url)
                    xml = get_TEI_XML(url, False)
                    #bookPieces.append(parse_TEI_full_book(xml))
                    bookPieces.append(xml)
                #bookText = removePunct(" ".join(bookPieces))
                bookText = " ".join(bookPieces)
                if (verbose):
                    print(bookText)
                allBooks.append({
                    "bookNumber": bookNum,
                    "bookText": bookText
                })
        else:
            for b in range(self.numBooks):
                bookNum = b + 1
                if (bookNum == 8 and author == "Aelian" and self.textName == "De Natura Animalium"):
                    continue
                url = urlBase + str(bookNum)
                if (verbose):
                    print(url)
                xml = get_TEI_XML(url, False)
                #print(xml)
                #bookText = removePunct(parse_TEI_full_book(xml))
                bookText = xml
                if (verbose):
                    print(bookText)
                allBooks.append({
                    "bookNumber": bookNum,
                    "bookText": bookText
                })
        self.loaded = True

        textObj = {
            "name": self.textName,
            "author": author,
            "numBooks": self.numBooks,
            "booksRaw": allBooks
        }
        safeWrite(saveLoc, textObj, True)

        return {
            "name": self.textName,
            "location": saveLoc
        }

# ==============================================================================
# ==============================================================================
# ==============================================================================
# Functions for getting web pages

# get an html page
def getHtmlPage(url):
    http = urllib3.PoolManager()
    max_tries = 5
    response = http.request('GET', url, retries=urllib3.Retry(max_tries, redirect=2))
    res = response.data.decode('utf-8')
    return res

# grab the TEI file at the given URL from Perseus; the result should be in
# betacode if isBetacode is set to true .
def get_TEI_XML(url, isBetaCode):
    http = urllib3.PoolManager()
    max_tries = 5
    if (isBetaCode):
        hdrs = {
            "Cookie": "disp.prefs=\"greek.display=PerseusBetaCode\"" #|default.scheme=book:card|default.type=book
        }
    else:
        hdrs = {}
    response = http.request('GET', url, headers=hdrs, retries=urllib3.Retry(max_tries, redirect=2))
    xml = response.data.decode('utf-8')
    if (xml[0:5] != "<?xml"):
        print(url)
        # print(xml)
        raise Exception("Got back HTML for %s." % (url))
    return xml


# parse the TEI data for a full book
def parse_TEI_full_book(xml):
    # remove notes, bibliography, heads, and foreign languages
    noNotes = re.sub(r'<note[\S\s]*?/note>', " ", xml)
    noBibl = re.sub(r'<bibl[\S\s]*?/bibl>', " ", noNotes)
    noHead = re.sub(r'<head[\S\s]*?/head>', " ", noBibl)
    noForeign = re.sub(r'<foreign lang="(la|en)"[\S\s]*?/foreign>', " ", noHead)
    noForeign = re.sub(r'<p lang="(la|en)"[\S\s]*?/p>', " ", noForeign)
    # remove all the xml tags since we just need the whole text
    noTags = re.sub(r'<[^>][\S\s]*?>', " ", noForeign)
    return noTags
