# Download texts from Perseus.
from authorsList import authors
import utils

resultFolder = "perseus_texts/"

# get already downloaded texts
try:
    available = utils.getContent(resultFolder + "available.json", True)
except(FileNotFoundError):
    available = []

# go through already downloaded texts and add them to the list
alreadyDownloaded = {}
authorWorks = {}
for o in available:
    author = o['author']
    works = o['works']
    workNames = set()
    for w in works:
        workNames.add(w['name'])
    alreadyDownloaded[author] = workNames
    authorWorks[author] = o['works']

# Count number of authors
numAuthors = 0
for author in authors:
    numAuthors += 1

print('Downloading...')
result = []
VERBOSE = False
# go through authors and download the texts that haven't been downloaded.
for i in range(len(authors)):
    author = authors[i]
    if (author.authorName in alreadyDownloaded):
        downloadedTexts = alreadyDownloaded[author.authorName]
        prevWorks = authorWorks[author.authorName]
    else:
        downloadedTexts = []
        prevWorks = []
    print("%s. %.2f%% (%d/%d)" % (author.authorName, (100*i/numAuthors), i, numAuthors))
    result.append(author.downloadAndSaveWorks(resultFolder, downloadedTexts, prevWorks, VERBOSE))

# save the result
utils.safeWrite(resultFolder+"available.json", result, True)
