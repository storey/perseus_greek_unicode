# A list of all of the authors and their works, with associated data
# for downloading the texts from Perseus.
import utils

from itertools import chain

# Create authors
authors = []


ach_tat = utils.Author("AchillesTatius")
ach_tat.addWork(utils.TextSpec("Leucippe et Clitophon", "2008.01.0665", 8, "%3Abook%3D", {"multi": False, "suffixes": []}))
authors.append(ach_tat)

aelian = utils.Author("Aelian")
aelian.addWork(utils.TextSpec("De Natura Animalium", "2008.01.0590", 17, "%3Abook%3D", {"multi": False, "suffixes": []}))
aelian.addWork(utils.TextSpec("Epistulae Rusticae", "2008.01.0592", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 20+1) # 1 to 20
}))
aelian.addWork(utils.TextSpec("Varia Historia", "2008.01.0591", 14, "%3Abook%3D", {"multi": False, "suffixes": []}))
authors.append(aelian)

aen_tac = utils.Author("AeneasTacticus")
aen_tac.addWork(utils.TextSpec("Poliorcetica", "2008.01.0667", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["praef", "III", "IV", "V", "VI", "XI", "XII", "XIII", "XIV", "XVI", "XIX", "XX", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX", "XXXI", "XXXII", "XXXIII", "XXXIV", "XXXV", "XXXVI", "XXXVII", "XXXVIII", "XXXIX", "XL"]
}))
authors.append(aen_tac)

aeschines = utils.Author("Aeschines")
aeschines.addWork(utils.TextSpec("Against Timarchus", "1999.01.0001", 1, "%3Aspeech%3D1%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 196+1)
}))
aeschines.addWork(utils.TextSpec("On the Embassy", "1999.01.0001", 1, "%3Aspeech%3D2%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 184+1)
}))
aeschines.addWork(utils.TextSpec("Against Ctesiphon", "1999.01.0001", 1, "%3Aspeech%3D3%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 260+1)
}))
authors.append(aeschines)

aeschylus = utils.Author("Aeschylus")
aeschylus.addWork(utils.TextSpec("Agamemnon", "1999.01.0003", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": [1, 40, 83, 104, 122, 140, 160, 167, 176, 184, 192, 205, 218, 228, 238, 248, 258, 281, 320, 355, 367, 385, 403, 420, 437, 456, 475, 488, 538, 583, 613, 636, 681, 699, 716, 727, 737, 750, 763, 772, 782, 810, 855, 887, 914, 944, 975, 988, 1001, 1017, 1035, 1072, 1076, 1080, 1085, 1090, 1095, 1100, 1107, 1114, 1125, 1136, 1146, 1156, 1167, 1178, 1202, 1242, 1295, 1331, 1343, 1344, 1345, 1346, 1348, 1372, 1407, 1412, 1426, 1431, 1448, 1455, 1462, 1468, 1475, 1481, 1489, 1497, 1505, 1513, 1521, 1531, 1537, 1551, 1560, 1567, 1577, 1617, 1649]
}))
aeschylus.addWork(utils.TextSpec("Eumenides", "1999.01.0005", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "34", "64", "94", "131", "143", "149", "155", "162", "169", "174", "178", "213", "254", "276", "299", "307", "321", "328", "334", "341", "347", "354", "360", "354a", "368", "372", "377", "372a", "381", "389", "397", "436", "470", "490", "499", "508", "517", "526", "538", "550", "558", "566", "607", "640", "674", "711", "744", "778", "793", "808", "823", "837", "848", "870", "881", "916", "927", "938", "949", "956", "968", "976", "988", "996", "1003", "1014", "1021", "1032", "1035", "1040", "1044"]
}))
aeschylus.addWork(utils.TextSpec("Libation Bearers", "1999.01.0007", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "22", "32", "42", "55", "66", "71", "75", "84", "106", "152", "164", "195", "225", "264", "306", "315", "323", "332", "340", "345", "354", "363", "372", "380", "386", "394", "400", "405", "410", "418", "423", "429", "434", "439", "445", "451", "456", "461", "466", "471", "476", "479", "510", "540", "585", "594", "602", "612", "623", "631", "639", "646", "653", "691", "719", "730", "766", "783", "789", "794", "800", "806", "811", "819", "827", "831", "838", "855", "869", "875", "900", "935", "942", "946", "942a", "953", "961", "966", "972", "973", "1007", "1010", "1018", "1021", "1051", "1065"]
}))
aeschylus.addWork(utils.TextSpec("Persians", "1999.01.0011", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "41", "65", "73", "81", "87", "93", "100", "107", "111", "115", "120", "126", "133", "140", "155", "159", "176", "200", "215", "232", "249", "256", "260", "262", "266", "268", "272", "274", "278", "280", "284", "286", "290", "331", "353", "395", "433", "472", "480", "515", "532", "548", "558", "568", "576", "584", "591", "598", "623", "633", "640", "647", "652", "657", "664", "673", "681", "694", "697", "700", "703", "715", "739", "759", "787", "800", "843", "852", "858", "864", "871", "879", "889", "898", "909", "932", "941", "950", "962", "974", "988", "1002", "1008", "1014", "1026", "1038", "1046", "1054", "1060", "1066"]
}))
aeschylus.addWork(utils.TextSpec("Prometheus Bound", "1999.01.0009", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "36", "61", "88", "95", "101", "114", "121", "128", "136", "144", "152", "160", "168", "180", "189", "196", "244", "265", "279", "300", "332", "343", "379", "399", "407", "415", "420", "425", "436", "472", "507", "526", "537", "545", "552", "561", "566", "575", "589", "593", "609", "640", "687", "696", "742", "780", "819", "846", "877", "887", "894", "901", "907", "944", "964", "1007", "1040", "1080"]
}))
aeschylus.addWork(utils.TextSpec("Seven Against Thebes", "1999.01.0013", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "39", "78", "109", "128", "149", "158", "166", "174", "181", "203", "211", "219", "226", "233", "239", "245", "288", "304", "321", "333", "345", "357", "369", "417", "422", "452", "457", "481", "486", "521", "526", "563", "568", "626", "631", "686", "692", "698", "705", "712", "720", "727", "734", "742", "750", "758", "766", "772", "778", "785", "792", "822", "833", "840", "848", "875", "881", "888", "900", "911", "922", "933", "945", "957", "966", "980", "994", "1011", "1032", "1048"]
}))
aeschylus.addWork(utils.TextSpec("Suppliant Women", "1999.01.0015", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "40", "49", "58", "63", "68", "77", "86", "91", "96", "104", "112", "117", "123", "128", "134", "141", "144", "151", "154", "162", "168", "162a", "176", "207", "234", "274", "291", "323", "348", "354", "359", "365", "370", "376", "381", "387", "392", "397", "402", "407", "418", "423", "428", "433", "438", "490", "524", "531", "538", "547", "556", "565", "574", "582", "590", "595", "600", "625", "630", "643", "656", "667", "678", "688", "698", "704", "710", "736", "739", "743", "746", "750", "753", "757", "760", "776", "784", "792", "800", "808", "817", "825", "836", "843", "849", "854", "861", "866", "872", "876", "882", "885", "893", "895", "902", "930", "966", "980", "1018", "1026", "1034", "1043", "1052", "1057", "1062", "1068"]
}))
authors.append(aeschylus)

andocides = utils.Author("Andocides")
andocides.addWork(utils.TextSpec("On the Mysteries", "1999.01.0017", 1, "%3Aspeech%3D1%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 150+1)
}))
andocides.addWork(utils.TextSpec("On his Return", "1999.01.0017", 1, "%3Aspeech%3D2%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 28+1)
}))
andocides.addWork(utils.TextSpec("On the Peace", "1999.01.0017", 1, "%3Aspeech%3D3%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 41+1)
}))
andocides.addWork(utils.TextSpec("Against Alcibiades", "1999.01.0017", 1, "%3Aspeech%3D4%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 42+1)
}))
authors.append(andocides)


antiphon = utils.Author("Antiphon")
antiphon.addWork(utils.TextSpec("Against the Stepmother for Poisoning", "1999.01.0019", 1, "%3Aspeech%3D1%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 31+1)
}))
antiphon.addWork(utils.TextSpec("First Tetralogy", "1999.01.0019", 1, "%3Aspeech%3D2%3Atetralogy%3D", {
    "multi": False,
    "suffixes": range(1, 4+1)
}))
antiphon.addWork(utils.TextSpec("Second Tetralogy", "1999.01.0019", 1, "%3Aspeech%3D3%3Atetralogy%3D", {
    "multi": False,
    "suffixes": range(1, 4+1)
}))
antiphon.addWork(utils.TextSpec("Third Tetralogy", "1999.01.0019", 1, "%3Aspeech%3D4%3Atetralogy%3D", {
    "multi": False,
    "suffixes": range(1, 4+1)
}))
antiphon.addWork(utils.TextSpec("On the murder of Herodes", "1999.01.0019", 1, "%3Aspeech%3D5%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 96+1)
}))
antiphon.addWork(utils.TextSpec("On the Choreutes", "1999.01.0019", 1, "%3Aspeech%3D6%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 51+1)
}))
authors.append(antiphon)

apollodorus = utils.Author("PseudoApollodorus")
apollodorus.addWork(utils.TextSpec("Library", "1999.01.0021", 3, "%3Atext%3DLibrary%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
apollodorus.addWork(utils.TextSpec("Epitome", "1999.01.0021", 1, "%3Atext%3DEpitome%3Abook%3D", {
    "multi": False,
    "suffixes": ["E"]
}))
authors.append(apollodorus)

apoll_rhodius = utils.Author("ApolloniusRhodius")
apoll_rhodius.addWork(utils.TextSpec("Argonautica", "1999.01.0227", 4, "%3Abook%3D", {"multi": False, "suffixes": []}))
authors.append(apoll_rhodius)

appian = utils.Author("Appian")
appian.addWork(utils.TextSpec("The Civil Wars", "1999.01.0231", 5, "%3Abook%3D", {"multi": False, "suffixes": []}))
appian.addWork(utils.TextSpec("The Foreign Wars", "1999.01.0229", 1, "%3Atext%3D", {
    "multi": True,
    "suffixes": [
        {"bookNum": "Reg.",  "infix2": "Reg.%3Achapter%3D",  "suffs": range(1, 1+1)},
        {"bookNum": "Ital.", "infix2": "Ital.%3Achapter%3D", "suffs": range(1, 1+1)},
        {"bookNum": "Sam.",  "infix2": "Sam.%3Achapter%3D",  "suffs": range(1, 1+1)},
        {"bookNum": "Gall.", "infix2": "Gall.%3Achapter%3D", "suffs": range(1, 1+1)},
        {"bookNum": "Sic.",  "infix2": "Sic.%3Achapter%3D",  "suffs": range(1, 1+1)},
        {"bookNum": "Hisp.", "infix2": "Hisp.%3Achapter%3D", "suffs": range(1, 16+1)},
        {"bookNum": "Hann.", "infix2": "Hann.%3Achapter%3D", "suffs": range(1, 9+1)},
        {"bookNum": "Pun.",  "infix2": "Pun.%3Achapter%3D",  "suffs": range(1, 20+1)},
        {"bookNum": "Num.",  "infix2": "Num.%3Asection%3D",  "suffs": range(1, 5+1)},
        {"bookNum": "Mac.",  "infix2": "Mac.%3Achapter%3D",  "suffs": range(1, 1+1)},
        {"bookNum": "Ill.",  "infix2": "Ill.%3Achapter%3D",  "suffs": range(1, 5+1)},
        {"bookNum": "Syr.",  "infix2": "Syr.%3Achapter%3D",  "suffs": range(1, 11+1)},
        {"bookNum": "Mith.", "infix2": "Mith.%3Achapter%3D", "suffs": range(1, 17+1)}]
}))
authors.append(appian)

aratus_sol = utils.Author("AratusSolensis")
aratus_sol.addWork(utils.TextSpec("Phaenomena", "2008.01.0483", 1, "%3Abook%3D", {"multi": False, "suffixes": []}))
authors.append(aratus_sol)

aretaeus = utils.Author("Aretaeus")
aretaeus.addWork(utils.TextSpec("On the Causes and Signs of Acute Diseases (Book 1)", "1999.01.0253", 1, "%3Atext%3D", {
    "multi": False,
    "suffixes": ["sa"]
}))
aretaeus.addWork(utils.TextSpec("On the Causes and Signs of Acute Diseases (Book 2)", "1999.01.0253", 1, "%3Atext%3D", {
    "multi": False,
    "suffixes": ["sd"]
}))
aretaeus.addWork(utils.TextSpec("On the Cures of Acute Diseases (Book 2)", "1999.01.0253", 1, "%3Atext%3D", {
    "multi": False,
    "suffixes": ["ca"]
}))
aretaeus.addWork(utils.TextSpec("On the Cures of Long Lasting Diseases (Book 2)", "1999.01.0253", 1, "%3Atext%3D", {
    "multi": False,
    "suffixes": ["cd"]
}))
authors.append(aretaeus)

aeliusAristides = utils.Author("AeliusAristides")
aeliusAristides.addWork(utils.TextSpec("Ars Rhetorica", "2008.01.0589", 1, "%3Atext%3D", {
    "multi": False,
    "suffixes": [56]
}))
aeliusAristides.addWork(utils.TextSpec("Orationes", "2008.01.0588", 1, "%3Atext%3D", {
    "multi": True,
    "suffixes": [
        {"bookNum": "1",  "infix2": "1%3Ajebb+page%3D",  "suffs": range(1, 8+1)},
        {"bookNum": "2",  "infix2": "2%3Ajebb+page%3D",  "suffs": range(9, 17+1)},
        {"bookNum": "3",  "infix2": "3%3Ajebb+page%3D",  "suffs": range(17, 28+1)},
        {"bookNum": "4",  "infix2": "4%3Ajebb+page%3D",  "suffs": range(28, 31+1)},
        {"bookNum": "5",  "infix2": "5%3Ajebb+page%3D",  "suffs": range(31, 36+1)},
        {"bookNum": "6",  "infix2": "6%3Ajebb+page%3D",  "suffs": range(36, 40+1)},
        {"bookNum": "7",  "infix2": "7%3Ajebb+page%3D",  "suffs": range(41, 46+1)},
        {"bookNum": "8",  "infix2": "8%3Ajebb+page%3D",  "suffs": range(47, 56+1)},
        {"bookNum": "9",  "infix2": "9%3Ajebb+page%3D",  "suffs": range(56, 67+1)},
        {"bookNum": "10", "infix2": "10%3Ajebb+page%3D", "suffs": range(68, 75+1)},
        {"bookNum": "11", "infix2": "11%3Ajebb+page%3D", "suffs": range(75, 80+1)},
        {"bookNum": "12", "infix2": "12%3Ajebb+page%3D", "suffs": range(80, 90+1)},
        {"bookNum": "13", "infix2": "13%3Ajebb+page%3D", "suffs": range(91, 197+1)},
        {"bookNum": "14", "infix2": "14%3Ajebb+page%3D", "suffs": range(197, 228+1)},
        {"bookNum": "15", "infix2": "15%3Ajebb+page%3D", "suffs": range(229, 235+1)},
        {"bookNum": "16", "infix2": "16%3Ajebb+page%3D", "suffs": range(236, 247+1)},
        {"bookNum": "17", "infix2": "17%3Ajebb+page%3D", "suffs": range(247, 251+1)},
        {"bookNum": "18", "infix2": "18%3Ajebb+page%3D", "suffs": range(252, 256+1)},
        {"bookNum": "19", "infix2": "19%3Ajebb+page%3D", "suffs": range(256, 260+1)},
        {"bookNum": "20", "infix2": "20%3Ajebb+page%3D", "suffs": range(260, 263+1)},
        {"bookNum": "21", "infix2": "21%3Ajebb+page%3D", "suffs": range(263, 269+1)},
        {"bookNum": "22", "infix2": "22%3Ajebb+page%3D", "suffs": range(269, 273+1)},
        {"bookNum": "23", "infix2": "23%3Ajebb+page%3D", "suffs": range(273, 290+1)},
        {"bookNum": "24", "infix2": "24%3Ajebb+page%3D", "suffs": range(291, 309+1)},
        {"bookNum": "25", "infix2": "25%3Ajebb+page%3D", "suffs": range(309, 320+1)},
        {"bookNum": "26", "infix2": "26%3Ajebb+page%3D", "suffs": range(321, 346+1)},
        {"bookNum": "27", "infix2": "27%3Ajebb+page%3D", "suffs": range(347, 361+1)},
        {"bookNum": "28", "infix2": "28%3Ajebb+page%3D", "suffs": range(362, 362+1)},
        {"bookNum": "29", "infix2": "29%3Ajebb+page%3D", "suffs": range(363, 375+1)},
        {"bookNum": "30", "infix2": "30%3Ajebb+page%3D", "suffs": range(376, 391+1)},
        {"bookNum": "31", "infix2": "31%3Ajebb+page%3D", "suffs": range(391, 399+1)},
        {"bookNum": "32", "infix2": "32%3Ajebb+page%3D", "suffs": range(399, 406+1)},
        {"bookNum": "33", "infix2": "33%3Ajebb+page%3D", "suffs": range(407, 426+1)},
        {"bookNum": "34", "infix2": "34%3Ajebb+page%3D", "suffs": range(427, 447+1)},
        {"bookNum": "35", "infix2": "35%3Ajebb+page%3D", "suffs": range(448, 457+1)},
        {"bookNum": "36", "infix2": "36%3Ajebb+page%3D", "suffs": range(457, 465+1)},
        {"bookNum": "37", "infix2": "37%3Ajebb+page%3D", "suffs": range(465, 476+1)},
        {"bookNum": "38", "infix2": "38%3Ajebb+page%3D", "suffs": range(477, 490+1)},
        {"bookNum": "39", "infix2": "39%3Ajebb+page%3D", "suffs": range(490, 504+1)},
        {"bookNum": "40", "infix2": "40%3Ajebb+page%3D", "suffs": range(504, 512+1)},
        {"bookNum": "41", "infix2": "41%3Ajebb+page%3D", "suffs": range(512, 516+1)},
        {"bookNum": "42", "infix2": "42%3Ajebb+page%3D", "suffs": range(517, 538+1)},
        {"bookNum": "43", "infix2": "43%3Ajebb+page%3D", "suffs": range(539, 557+1)},
        {"bookNum": "44", "infix2": "44%3Ajebb+page%3D", "suffs": range(557, 572+1)},
        {"bookNum": "45", "infix2": "45%3Ajebb+page%3D", "suffs": range(1, 115+1)},
        {"bookNum": "46", "infix2": "46%3Ajebb+page%3D", "suffs": range(116, 315+1)},
        {"bookNum": "47", "infix2": "47%3Ajebb+page%3D", "suffs": range(315, 330+1)},
        {"bookNum": "48", "infix2": "48%3Ajebb+page%3D", "suffs": range(331, 364+1)},
        {"bookNum": "49", "infix2": "49%3Ajebb+page%3D", "suffs": range(365, 401+1)},
        {"bookNum": "50", "infix2": "50%3Ajebb+page%3D", "suffs": range(401, 416+1)},
        {"bookNum": "51", "infix2": "51%3Ajebb+page%3D", "suffs": range(416, 424+1)},
        {"bookNum": "52", "infix2": "52%3Ajebb+page%3D", "suffs": range(425, 437+1)},
        {"bookNum": "53", "infix2": "53%3Ajebb+page%3D", "suffs": range(1, 33+1)},
        {"bookNum": "54", "infix2": "54%3Ajebb+page%3D", "suffs": [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186]},
        {"bookNum": "55", "infix2": "", "suffs": ["55"]}]
}))
authors.append(aeliusAristides)

aristophanes = utils.Author("Aristophanes")
aristophanes.addWork(utils.TextSpec("Acharnians", "1999.01.0023", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "43", "65", "100", "134", "172", "204", "208", "219", "225", "234", "241", "263", "280", "284", "302", "335", "347", "358", "366", "385", "393", "407", "454", "490", "496", "541", "557", "566", "572", "626", "628", "659", "665", "676", "692", "703", "719", "750", "799", "836", "842", "848", "854", "860", "895", "929", "940", "952", "971", "988", "1000", "1008", "1018", "1037", "1047", "1069", "1095", "1143", "1150", "1162", "1174", "1204", "1227"]
}))
aristophanes.addWork(utils.TextSpec("Birds", "1999.01.0025", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "49", "90", "125", "164", "209", "223", "227", "263", "267", "310", "327", "336", "339", "343", "352", "354", "386", "400", "407", "435", "451", "460", "462", "499", "523", "539", "548", "550", "592", "611", "627", "639", "658", "676", "685", "708", "723", "737", "752", "769", "785", "801", "851", "859", "895", "903", "941", "967", "989", "1021", "1058", "1072", "1088", "1102", "1118", "1148", "1189", "1196", "1224", "1263", "1313", "1325", "1337", "1372", "1410", "1436", "1470", "1482", "1494", "1525", "1553", "1565", "1606", "1646", "1694", "1706", "1720", "1731", "1737", "1743"]
}))
aristophanes.addWork(utils.TextSpec("Clouds", "1999.01.0027", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "25", "56", "90", "133", "180", "221", "262", "275", "291", "299", "314", "356", "392", "437", "457", "476", "510", "518", "563", "575", "595", "607", "627", "658", "700", "707", "731", "776", "804", "814", "854", "889", "920", "949", "959", "961", "986", "1000", "1009", "1024", "1034", "1036", "1067", "1086", "1105", "1113", "1115", "1131", "1154", "1170", "1206", "1213", "1259", "1303", "1311", "1321", "1345", "1351", "1353", "1386", "1391", "1397", "1399", "1437", "1445", "1452", "1476"]
}))
aristophanes.addWork(utils.TextSpec("Ecclesiazusae", "1999.01.0029", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "41", "86", "128", "169", "204", "241", "289", "300", "311", "354", "389", "434", "478", "483", "493", "504", "535", "571", "581", "583", "604", "635", "667", "711", "746", "776", "805", "834", "877", "900", "906", "911", "918", "924", "952", "960", "969", "972", "976", "1010", "1049", "1079", "1112", "1155", "1163"]
}))
aristophanes.addWork(utils.TextSpec("Frogs", "1999.01.0031", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "38", "60", "89", "116", "152", "185", "209", "225", "268", "316", "323", "337", "340", "354", "372", "378", "384", "386", "391", "396", "399", "405", "411", "417", "420", "423", "426", "429", "432", "435", "438", "449", "455", "460", "503", "534", "549", "590", "605", "675", "686", "706", "718", "738", "788", "814", "818", "822", "826", "830", "860", "895", "905", "907", "937", "971", "992", "1004", "1006", "1045", "1078", "1099", "1110", "1119", "1158", "1206", "1251", "1296", "1309", "1370", "1378", "1414", "1460", "1482", "1491", "1500", "1528"]
}))
aristophanes.addWork(utils.TextSpec("Knights", "1999.01.0033", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "40", "85", "131", "175", "213", "242", "284", "303", "314", "323", "333", "335", "367", "384", "391", "398", "409", "441", "457", "461", "498", "507", "547", "551", "565", "581", "595", "611", "616", "624", "658", "683", "691", "728", "756", "761", "763", "790", "824", "836", "841", "843", "887", "911", "942", "973", "985", "997", "1014", "1060", "1111", "1151", "1191", "1231", "1264", "1274", "1290", "1300", "1316", "1335", "1362", "1372", "1390"]
}))
aristophanes.addWork(utils.TextSpec("Lysistrata", "1999.01.0035", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "46", "86", "130", "175", "215", "254", "258", "266", "273", "281", "286", "296", "306", "321", "335", "350", "387", "443", "467", "476", "484", "486", "532", "539", "541", "549", "551", "598", "608", "614", "626", "636", "648", "658", "672", "683", "696", "706", "749", "781", "805", "829", "870", "915", "954", "980", "1014", "1043", "1058", "1072", "1112", "1157", "1189", "1203", "1216", "1247", "1273", "1279", "1295"]
}))
aristophanes.addWork(utils.TextSpec("Peace", "1999.01.0037", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "50", "82", "118", "154", "173", "200", "250", "301", "346", "361", "383", "385", "400", "426", "431", "459", "473", "486", "500", "512", "520", "551", "571", "582", "601", "651", "657", "700", "729", "734", "765", "774", "797", "819", "856", "868", "910", "922", "939", "956", "974", "1016", "1023", "1039", "1063", "1105", "1127", "1140", "1156", "1159", "1172", "1188", "1191", "1230", "1270", "1298", "1305", "1316", "1320"]
}))
aristophanes.addWork(utils.TextSpec("Plutus", "1999.01.0039", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "51", "107", "170", "220", "253", "290", "296", "302", "309", "316", "322", "377", "418", "467", "487", "489", "535", "598", "627", "651", "696", "748", "771", "802", "850", "901", "959", "1003", "1052", "1097", "1135", "1171"]
}))
aristophanes.addWork(utils.TextSpec("Thesmophoriazusae", "1999.01.0041", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "52", "101", "153", "206", "266", "295", "312", "331", "352", "372", "434", "443", "459", "466", "520", "531", "533", "574", "626", "655", "659", "663", "668", "689", "699", "707", "728", "776", "785", "814", "830", "846", "902", "947", "959", "962", "966", "969", "977", "985", "990", "995", "1001", "1056", "1098", "1136", "1140", "1143", "1145", "1148", "1155", "1160", "1226"]
}))
aristophanes.addWork(utils.TextSpec("Wasps", "1999.01.0043", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "54", "85", "136", "183", "230", "273", "281", "291", "303", "316", "334", "336", "342", "346", "348", "358", "365", "367", "373", "379", "381", "403", "420", "430", "461", "477", "488", "526", "546", "548", "576", "605", "621", "631", "648", "650", "696", "719", "725", "729", "743", "760", "799", "826", "863", "868", "875", "885", "903", "953", "1009", "1015", "1051", "1060", "1071", "1091", "1102", "1122", "1170", "1224", "1265", "1275", "1284", "1292", "1326", "1335", "1342", "1388", "1417", "1450", "1462", "1474", "1516", "1518", "1523", "1529"]
}))
authors.append(aristophanes)

aristotle = utils.Author("Aristotle")
aristotle.addWork(utils.TextSpec("Athenian Constitution", "1999.01.0045", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["fragments", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
}))
aristotle.addWork(utils.TextSpec("Economics", "1999.01.0047", 2, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
aristotle.addWork(utils.TextSpec("Eudemian Ethics", "1999.01.0049", 7, "%3Abook%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "7", "8"]
}))
aristotle.addWork(utils.TextSpec("Metaphysics", "1999.01.0051", 14, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
aristotle.addWork(utils.TextSpec("Nicomachean Ethics", "1999.01.0053", 10, "", {
    "multi": True,
    "suffixes": [
        {"bookNum": "1",  "infix2": "%3Abekker%20page%3D",  "suffs":  ["1094a", "1094b", "1095a", "1095b", "1096a", "1096b", "1097a", "1097b", "1098a", "1098b", "1099a", "1099b", "1100a", "1100b", "1101a", "1101b", "1102a", "1102b", "1103a%3Abekker+line%3D1", "1103a%3Abekker+line%3D5", "1103a%3Abekker+line%3D10"]},
        {"bookNum": "2",  "infix2": "%3Abekker%20page%3D",  "suffs":  ["1103a%3Abekker+line%3D14", "1103a%3Abekker+line%3D15", "1103a%3Abekker+line%3D20", "1103a%3Abekker+line%3D25", "1103a%3Abekker+line%3D30", "1103a", "1103b", "1104a", "1104b", "1105a", "1105b", "1106a", "1106b", "1107a", "1107b", "1108a", "1108b", "1109a", "1109b"]},
        {"bookNum": "3",  "infix2": "%3Abekker%20page%3D",  "suffs":  ["pos%3D33", "1110a", "1110b", "1111a", "1111b", "1112a", "1112b", "1113a", "1113b", "1114a", "1114b", "1115a", "1115b", "1116a", "1116b", "1117a", "1117b", "1118a", "1118b", "1119a", "1119b"]},
        {"bookNum": "4",  "infix2": "%3Abekker%20page%3D",  "suffs":  ["pos%3D54", "1120a", "1120b", "1121a", "1121b", "1122a", "1122b", "1123a", "1123b", "1124a", "1124b", "1125a", "1125b", "1126a", "1126b", "1127a", "1127b", "1128a", "1128b"]},
        {"bookNum": "5",  "infix2": "%3Abekker%20page%3D",  "suffs":  ["1129a", "1129b", "1130a", "1130b", "1131a", "1131b", "1132a", "1132b", "1133a", "1133b", "1134a", "1134b", "1135a", "1135b", "1136a", "1136b", "1137a", "1137b", "1138a", "1138b"]},
        {"bookNum": "6",  "infix2": "%3Abekker%20page%3D",  "suffs":  ["pos%3D93", "1139a", "1139b", "1140a", "1140b", "1141a", "1141b", "1142a", "1142b", "1143a", "1143b", "1144a", "1144b", "1145a%3Abekker+line%3D1", "1145a%3Abekker+line%3D5", "1145a%3Abekker+line%3D10"]},
        {"bookNum": "7",  "infix2": "%3Abekker%20page%3D",  "suffs":  ["1145a%3Abekker+line%3D15", "1145a%3Abekker+line%3D20", "1145a%3Abekker+line%3D25", "1145a%3Abekker+line%3D30", "1145a%3Abekker+line%3D35", "1145b", "1146a", "1146b", "1147a", "1147b", "1148a", "1148b", "1149a", "1149b", "1150a", "1150b", "1151a", "1151b", "1152a", "1152b", "1153a", "1153b", "1154a", "1154b"]},
        {"bookNum": "8",  "infix2": "%3Abekker%20page%3D",  "suffs":  ["1155a", "1155b", "1156a", "1156b", "1157a", "1157b", "1158a", "1158b", "1159a", "1159b", "1160a", "1160b", "1161a", "1161b", "1162a", "1162b", "1163a", "1163b"]},
        {"bookNum": "9",  "infix2": "%3Abekker%20page%3D",  "suffs":  ["pos%3D144", "1164a", "1164b", "1165a", "1165b", "1166a", "1166b", "1167a", "1167b", "1168a", "1168b", "1169a", "1169b", "1170a", "1170b", "1171a", "1171b"]},
        {"bookNum": "10",  "infix2": "%3Abekker%20page%3D",  "suffs": ["1172a", "1172b", "1173a", "1173b", "1174a", "1174b", "1175a", "1175b", "1176a", "1176b", "1177a", "1177b", "1178a", "1178b", "1179a", "1179b", "1180a", "1180b", "1181a", "1181b"]},
    ]
}))
aristotle.addWork(utils.TextSpec("Poetics", "1999.01.0055", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": ["1447a", "1447b", "1448a", "1448b", "1449a", "1449b", "1450a", "1450b", "1451a", "1451b", "1452a", "1452b", "1453a", "1453b", "1454a", "1454b", "1455a", "1455b", "1456a", "1456b", "1457a", "1457b", "1458a", "1458b", "1459a", "1459b", "1460a", "1460b", "1461a", "1461b", "1462a", "1462b"]
}))
aristotle.addWork(utils.TextSpec("Politics", "1999.01.0057", 8, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
aristotle.addWork(utils.TextSpec("Rhetoric", "1999.01.0059", 3, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
aristotle.addWork(utils.TextSpec("Virtues and Vices", "1999.01.0061", 1, "%3Abekker+page%3D", {
    "multi": False,
    "suffixes": ["1249a", "1249b", "1250a", "1250b", "1251a", "1251b"]
}))
authors.append(aristotle)

arrian = utils.Author("Arrian")
arrian.addWork(utils.TextSpec("Acies Contra Alanos", "2008.01.0535", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1,31+1)
}))
arrian.addWork(utils.TextSpec("Anabasis", "2008.01.0530", 7, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
arrian.addWork(utils.TextSpec("Cynegeticus", "2008.01.0532", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 36+1) # technically there is a preface too, but it is a table of contents
}))
arrian.addWork(utils.TextSpec("Indica", "2008.01.0531", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 43+1)
}))
arrian.addWork(utils.TextSpec("Periplus Ponti Euxini", "2008.01.0533", 1, "%3Asection%3Dpos%3D", {
    "multi": False,
    "suffixes": range(1, 108+1)
}))
arrian.addWork(utils.TextSpec("Tactica", "2008.01.0534", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 44+1)
}))
authors.append(arrian)

asclepiodotus = utils.Author("Asclepiodotus")
asclepiodotus.addWork(utils.TextSpec("Tactica", "2008.01.0635", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 12+1)
}))
authors.append(asclepiodotus)

athenaeus = utils.Author("Athenaeus")
athenaeus.addWork(utils.TextSpec("Deipnosophistae", "2013.01.0001", 15, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(athenaeus)

marcusAurelius = utils.Author("MarcusAurelius")
marcusAurelius.addWork(utils.TextSpec("Marcus Antonius Imperator Ad Se Ipsum", "2008.01.0641", 12, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(marcusAurelius)

bacchylides = utils.Author("Bacchylides")
bacchylides.addWork(utils.TextSpec("Epinicians", "1999.01.0063", 1, "%3Abook%3DEp%3Apoem%3D", {
    "multi": False,
    "suffixes": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, "14b"]
}))
bacchylides.addWork(utils.TextSpec("Dithyrambs", "1999.01.0063", 1, "%3Abook%3DDith%3Apoem%3D", {
    "multi": False,
    "suffixes": range(15, 20+1)
}))
authors.append(bacchylides)

barnabas = utils.Author("Barnabas")
barnabas.addWork(utils.TextSpec("Barnabae Epistula", "2008.01.0629", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 21+1)
}))
authors.append(barnabas)

basil = utils.Author("BasilBishopOfCaesarea")
basil.addWork(utils.TextSpec("De legendis gentilium libris", "2008.01.0638", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 10+1)
}))
basil.addWork(utils.TextSpec("Epistulae", "2008.01.0637", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 368+1)
}))
authors.append(basil)

bion = utils.Author("BionOfPhlossa")
bion.addWork(utils.TextSpec("Epithalamium Achillis et Deidameiae", "2008.01.0671", 1, "%3Apoem%3D", {
    "multi": False,
    "suffixes": [2]
}))
bion.addWork(utils.TextSpec("Epitaphius Adonis", "2008.01.0672", 1, "%3Apoem%3D", {
    "multi": False,
    "suffixes": [1]
}))
bion.addWork(utils.TextSpec("Fragments", "2008.01.0673", 1, "%3Apoem%3D", {
    "multi": False,
    "suffixes": range(3, 18+1)
}))
authors.append(bion)

callimachus = utils.Author("Callimachus")
callimachus.addWork(utils.TextSpec("Epigrams and Fragments", "2008.01.0482", 1, "%3Apoem%3D", {
    "multi": False,
    "suffixes": range(1, 64+1)
}))
callimachus.addWork(utils.TextSpec("Hymns", "2008.01.0481", 1, "%3Ahymn%3D", {
    "multi": False,
    "suffixes": range(1, 6+1)
}))
authors.append(callimachus)

callistratus = utils.Author("Callistratus")
callistratus.addWork(utils.TextSpec("Statuaram Descriptiones", "2008.01.0594", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 14+1)
}))
authors.append(callistratus)

chariton = utils.Author("Chariton")
chariton.addWork(utils.TextSpec("De Chaerea et Callirhoe", "2008.01.0668", 8, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(chariton)

clement = utils.Author("ClementOfAlexandria")
clement.addWork(utils.TextSpec("Quis Dis Salvetur", "2008.01.0631", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 42+1)
}))
clement.addWork(utils.TextSpec("Exhortation to Endurance", "2008.01.0632", 1, "%3Atext%3D", {
    "multi": False,
    "suffixes": []
}))
clement.addWork(utils.TextSpec("Protrepticus", "2008.01.0633", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 12+1)
}))
authors.append(clement)

colluthus = utils.Author("Colluthus")
colluthus.addWork(utils.TextSpec("Rape of Helen", "2008.01.0495", 1, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(colluthus)

demades = utils.Author("Demades")
demades.addWork(utils.TextSpec("On the Twelve Years", "1999.01.0065", 1, "%3Aspeech%3D1%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 65+1)
}))
authors.append(demades)

demetrius = utils.Author("DemetriusOfPhaleron")
demetrius.addWork(utils.TextSpec("Libro de Elocutione", "2008.01.0630", 5, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(demetrius)

demosthenes = utils.Author("Demosthenes")
demosthenes.addWork(utils.TextSpec("Exordia", "1999.01.0067", 1, "%3Aexordium%3D", {
    "multi": False,
    "suffixes": range(1, 56+1)
}))
demosthenes.addWork(utils.TextSpec("Letters", "1999.01.0213", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1.5", "1.11", "2", "2.3", "2.9", "2.12", "2.17", "2.21", "2.25", "3", "3.5", "3.9", "3.11", "3.16", "3.19", "3.21", "3.23", "3.27", "3.29", "3.31", "3.35", "3.37", "3.39", "3.41", "3.44", "4", "4.3", "4.5", "4.10", "5", "6"]
}))
demosthenes.addWork(utils.TextSpec("Speeches", "", 61, "", {
    "multi": True,
    "suffixes": [
        {"bookNum": "1",   "infix2": "1999.01.0069%3Aspeech%3D1%3Asection%3D",   "suffs": range(1, 28+1)},
        {"bookNum": "2",   "infix2": "1999.01.0069%3Aspeech%3D2%3Asection%3D",   "suffs": range(1, 31+1)},
        {"bookNum": "3",   "infix2": "1999.01.0069%3Aspeech%3D3%3Asection%3D",   "suffs": range(1, 36+1)},
        {"bookNum": "4",   "infix2": "1999.01.0069%3Aspeech%3D4%3Asection%3D",   "suffs": range(1, 51+1)},
        {"bookNum": "5",   "infix2": "1999.01.0069%3Aspeech%3D5%3Asection%3D",   "suffs": range(1, 25+1)},
        {"bookNum": "6",   "infix2": "1999.01.0069%3Aspeech%3D6%3Asection%3D",   "suffs": range(1, 37+1)},
        {"bookNum": "7",   "infix2": "1999.01.0069%3Aspeech%3D7%3Asection%3D",   "suffs": range(1, 46+1)},
        {"bookNum": "8",   "infix2": "1999.01.0069%3Aspeech%3D8%3Asection%3D",   "suffs": range(1, 77+1)},
        {"bookNum": "9",   "infix2": "1999.01.0069%3Aspeech%3D9%3Asection%3D",   "suffs": range(1, 76+1)},
        {"bookNum": "10",  "infix2": "1999.01.0069%3Aspeech%3D10%3Asection%3D",  "suffs": range(1, 76+1)},
        {"bookNum": "11",  "infix2": "1999.01.0071%3Aspeech%3D11%3Asection%3D",  "suffs": range(1, 23+1)},
        {"bookNum": "12",  "infix2": "1999.01.0071%3Aspeech%3D12%3Asection%3D",  "suffs": range(1, 23+1)},
        {"bookNum": "13",  "infix2": "1999.01.0071%3Aspeech%3D13%3Asection%3D",  "suffs": range(1, 36+1)},
        {"bookNum": "14",  "infix2": "1999.01.0071%3Aspeech%3D14%3Asection%3D",  "suffs": range(1, 41+1)},
        {"bookNum": "15",  "infix2": "1999.01.0071%3Aspeech%3D15%3Asection%3D",  "suffs": range(1, 35+1)},
        {"bookNum": "16",  "infix2": "1999.01.0071%3Aspeech%3D16%3Asection%3D",  "suffs": range(1, 32+1)},
        {"bookNum": "17",  "infix2": "1999.01.0071%3Aspeech%3D17%3Asection%3D",  "suffs": range(1, 30+1)},
        {"bookNum": "18",  "infix2": "1999.01.0071%3Aspeech%3D18%3Asection%3D",  "suffs": range(1, 324+1)},
        {"bookNum": "19",  "infix2": "1999.01.0071%3Aspeech%3D19%3Asection%3D",  "suffs": chain(range(1, 103+1), range(109, 343+1))},
        {"bookNum": "20",  "infix2": "1999.01.0071%3Aspeech%3D20%3Asection%3D",  "suffs": range(1, 167+1)},
        {"bookNum": "21",  "infix2": "1999.01.0073%3Aspeech%3D21%3Asection%3D",  "suffs": range(1, 227+1)},
        {"bookNum": "22",  "infix2": "1999.01.0073%3Aspeech%3D22%3Asection%3D",  "suffs": range(1, 78+1)},
        {"bookNum": "23",  "infix2": "1999.01.0073%3Aspeech%3D23%3Asection%3D",  "suffs": range(1, 220+1)},
        {"bookNum": "24",  "infix2": "1999.01.0073%3Aspeech%3D24%3Asection%3D",  "suffs": range(1, 218+1)},
        {"bookNum": "25",  "infix2": "1999.01.0073%3Aspeech%3D25%3Asection%3D",  "suffs": range(1, 101+1)},
        {"bookNum": "26",  "infix2": "1999.01.0073%3Aspeech%3D26%3Asection%3D",  "suffs": range(1, 27+1)},
        {"bookNum": "27",  "infix2": "1999.01.0073%3Aspeech%3D27%3Asection%3D",  "suffs": range(1, 69+1)},
        {"bookNum": "28",  "infix2": "1999.01.0073%3Aspeech%3D28%3Asection%3D",  "suffs": range(1, 24+1)},
        {"bookNum": "29",  "infix2": "1999.01.0073%3Aspeech%3D29%3Asection%3D",  "suffs": range(1, 60+1)},
        {"bookNum": "30",  "infix2": "1999.01.0073%3Aspeech%3D30%3Asection%3D",  "suffs": range(1, 39+1)},
        {"bookNum": "31",  "infix2": "1999.01.0075%3Aspeech%3D31%3Asection%3D",  "suffs": range(1, 14+1)},
        {"bookNum": "32",  "infix2": "1999.01.0075%3Aspeech%3D32%3Asection%3D",  "suffs": range(1, 32+1)},
        {"bookNum": "33",  "infix2": "1999.01.0075%3Aspeech%3D33%3Asection%3D",  "suffs": range(1, 38+1)},
        {"bookNum": "34",  "infix2": "1999.01.0075%3Aspeech%3D34%3Asection%3D",  "suffs": range(1, 52+1)},
        {"bookNum": "35",  "infix2": "1999.01.0075%3Aspeech%3D35%3Asection%3D",  "suffs": range(1, 56+1)},
        {"bookNum": "36",  "infix2": "1999.01.0075%3Aspeech%3D36%3Asection%3D",  "suffs": range(1, 62+1)},
        {"bookNum": "37",  "infix2": "1999.01.0075%3Aspeech%3D37%3Asection%3D",  "suffs": range(1, 60+1)},
        {"bookNum": "38",  "infix2": "1999.01.0075%3Aspeech%3D38%3Asection%3D",  "suffs": range(1, 28+1)},
        {"bookNum": "39",  "infix2": "1999.01.0075%3Aspeech%3D39%3Asection%3D",  "suffs": range(1, 41+1)},
        {"bookNum": "40",  "infix2": "1999.01.0075%3Aspeech%3D40%3Asection%3D",  "suffs": range(1, 61+1)},
        {"bookNum": "41",  "infix2": "1999.01.0077%3Aspeech%3D41%3Asection%3D",  "suffs": range(1, 30+1)},
        {"bookNum": "42",  "infix2": "1999.01.0077%3Aspeech%3D42%3Asection%3D",  "suffs": range(1, 32+1)},
        {"bookNum": "43",  "infix2": "1999.01.0077%3Aspeech%3D43%3Asection%3D",  "suffs": range(1, 84+1)},
        {"bookNum": "44",  "infix2": "1999.01.0077%3Aspeech%3D44%3Asection%3D",  "suffs": range(1, 68+1)},
        {"bookNum": "45",  "infix2": "1999.01.0077%3Aspeech%3D45%3Asection%3D",  "suffs": range(1, 88+1)},
        {"bookNum": "46",  "infix2": "1999.01.0077%3Aspeech%3D46%3Asection%3D",  "suffs": range(1, 28+1)},
        {"bookNum": "47",  "infix2": "1999.01.0077%3Aspeech%3D47%3Asection%3D",  "suffs": range(1, 82+1)},
        {"bookNum": "48",  "infix2": "1999.01.0077%3Aspeech%3D48%3Asection%3D",  "suffs": range(1, 58+1)},
        {"bookNum": "49",  "infix2": "1999.01.0077%3Aspeech%3D49%3Asection%3D",  "suffs": range(1, 69+1)},
        {"bookNum": "50",  "infix2": "1999.01.0077%3Aspeech%3D50%3Asection%3D",  "suffs": range(1, 68+1)},
        {"bookNum": "51",  "infix2": "1999.01.0079%3Aspeech%3D51%3Asection%3D",  "suffs": range(1, 22+1)},
        {"bookNum": "52",  "infix2": "1999.01.0079%3Aspeech%3D52%3Asection%3D",  "suffs": range(1, 33+1)},
        {"bookNum": "53",  "infix2": "1999.01.0079%3Aspeech%3D53%3Asection%3D",  "suffs": range(1, 29+1)},
        {"bookNum": "54",  "infix2": "1999.01.0079%3Aspeech%3D54%3Asection%3D",  "suffs": range(1, 44+1)},
        {"bookNum": "55",  "infix2": "1999.01.0079%3Aspeech%3D55%3Asection%3D",  "suffs": range(1, 35+1)},
        {"bookNum": "56",  "infix2": "1999.01.0079%3Aspeech%3D56%3Asection%3D",  "suffs": range(1, 50+1)},
        {"bookNum": "57",  "infix2": "1999.01.0079%3Aspeech%3D57%3Asection%3D",  "suffs": range(1, 70+1)},
        {"bookNum": "58",  "infix2": "1999.01.0079%3Aspeech%3D58%3Asection%3D",  "suffs": range(1, 70+1)},
        {"bookNum": "59",  "infix2": "1999.01.0079%3Aspeech%3D59%3Asection%3D",  "suffs": range(1, 126+1)},
        {"bookNum": "60",  "infix2": "1999.01.0079%3Aspeech%3D60%3Asection%3D",  "suffs": range(1, 37+1)},
        {"bookNum": "61",  "infix2": "1999.01.0079%3Aspeech%3D61%3Asection%3D",  "suffs": range(1, 57+1)},
    ]
}))
authors.append(demosthenes)

dinarchus = utils.Author("Dinarchus")
dinarchus.addWork(utils.TextSpec("Speeches", "1999.01.0081", 3, "%3Aspeech%3D", {
    "multi": True,
    "suffixes": [
        {"bookNum": "1",   "infix2": "1%3Asection%3D",   "suffs": range(1, 114+1)},
        {"bookNum": "2",   "infix2": "2%3Asection%3D",   "suffs": range(1, 26+1)},
        {"bookNum": "3",   "infix2": "3%3Asection%3D",   "suffs": range(1, 22+1)},
    ]
}))
authors.append(dinarchus)

dioChrysostom = utils.Author("DioChrysostom")
dioChrysostom.addWork(utils.TextSpec("Orationes", "2008.01.0567", 80, "%3Aspeech%3D", {
    "multi": True,
    "suffixes": [
        {"bookNum": "1", "infix2": "1", "suffs": [""]},
        {"bookNum": "2", "infix2": "2", "suffs": [""]},
        {"bookNum": "3", "infix2": "3", "suffs": [""]},
        {"bookNum": "4", "infix2": "4", "suffs": [""]},
        {"bookNum": "5", "infix2": "5", "suffs": [""]},
        {"bookNum": "6", "infix2": "6", "suffs": [""]},
        {"bookNum": "7", "infix2": "7", "suffs": [""]},
        {"bookNum": "8", "infix2": "8", "suffs": [""]},
        {"bookNum": "9", "infix2": "9", "suffs": [""]},
        {"bookNum": "10", "infix2": "10", "suffs": [""]},
        {"bookNum": "11", "infix2": "11", "suffs": [""]},
        {"bookNum": "12", "infix2": "12", "suffs": [""]},
        {"bookNum": "13", "infix2": "13", "suffs": [""]},
        {"bookNum": "19", "infix2": "19", "suffs": [""]},
        {"bookNum": "20", "infix2": "20", "suffs": [""]},
        {"bookNum": "21", "infix2": "21", "suffs": [""]},
        {"bookNum": "22", "infix2": "22", "suffs": [""]},
        {"bookNum": "23", "infix2": "23", "suffs": [""]},
        {"bookNum": "24", "infix2": "24", "suffs": [""]},
        {"bookNum": "25", "infix2": "25", "suffs": [""]},
        {"bookNum": "26", "infix2": "26", "suffs": [""]},
        {"bookNum": "27", "infix2": "27", "suffs": [""]},
        {"bookNum": "28", "infix2": "28", "suffs": [""]},
        {"bookNum": "29", "infix2": "29", "suffs": [""]},
        {"bookNum": "30", "infix2": "30", "suffs": [""]},
        {"bookNum": "31", "infix2": "31", "suffs": [""]},
        {"bookNum": "32", "infix2": "32", "suffs": [""]},
        {"bookNum": "33", "infix2": "33", "suffs": [""]},
        {"bookNum": "34", "infix2": "34", "suffs": [""]},
        {"bookNum": "35", "infix2": "35", "suffs": [""]},
        {"bookNum": "36", "infix2": "36", "suffs": [""]},
        {"bookNum": "37", "infix2": "37", "suffs": [""]},
        {"bookNum": "38", "infix2": "38", "suffs": [""]},
        {"bookNum": "39", "infix2": "39", "suffs": [""]},
        {"bookNum": "40", "infix2": "40", "suffs": [""]},
        {"bookNum": "41", "infix2": "41", "suffs": [""]},
        {"bookNum": "42", "infix2": "42", "suffs": [""]},
        {"bookNum": "43", "infix2": "43", "suffs": [""]},
        {"bookNum": "44", "infix2": "44", "suffs": [""]},
        {"bookNum": "45", "infix2": "45", "suffs": [""]},
        {"bookNum": "46", "infix2": "46", "suffs": [""]},
        {"bookNum": "47", "infix2": "47", "suffs": [""]},
        {"bookNum": "48", "infix2": "48", "suffs": [""]},
        {"bookNum": "49", "infix2": "49", "suffs": [""]},
        {"bookNum": "50", "infix2": "50", "suffs": [""]},
        {"bookNum": "51", "infix2": "51", "suffs": [""]},
        {"bookNum": "52", "infix2": "52", "suffs": [""]},
        {"bookNum": "53", "infix2": "53", "suffs": [""]},
        {"bookNum": "54", "infix2": "54", "suffs": [""]},
        {"bookNum": "55", "infix2": "55", "suffs": [""]},
        {"bookNum": "56", "infix2": "56", "suffs": [""]},
        {"bookNum": "57", "infix2": "57", "suffs": [""]},
        {"bookNum": "58", "infix2": "58", "suffs": [""]},
        {"bookNum": "59", "infix2": "59", "suffs": [""]},
        {"bookNum": "60", "infix2": "60", "suffs": [""]},
        {"bookNum": "61", "infix2": "61", "suffs": [""]},
        {"bookNum": "62", "infix2": "62", "suffs": [""]},
        {"bookNum": "63", "infix2": "63", "suffs": [""]},
        {"bookNum": "64", "infix2": "64", "suffs": [""]},
        {"bookNum": "65", "infix2": "65", "suffs": [""]},
        {"bookNum": "66", "infix2": "66", "suffs": [""]},
        {"bookNum": "67", "infix2": "67", "suffs": [""]},
        {"bookNum": "68", "infix2": "68", "suffs": [""]},
        {"bookNum": "69", "infix2": "69", "suffs": [""]},
        {"bookNum": "70", "infix2": "70", "suffs": [""]},
        {"bookNum": "71", "infix2": "71", "suffs": [""]},
        {"bookNum": "72", "infix2": "72", "suffs": [""]},
        {"bookNum": "73", "infix2": "73", "suffs": [""]},
        {"bookNum": "74", "infix2": "74", "suffs": [""]},
        {"bookNum": "75", "infix2": "75", "suffs": [""]},
        {"bookNum": "76", "infix2": "76", "suffs": [""]},
        {"bookNum": "77", "infix2": "77", "suffs": [""]},
        {"bookNum": "78", "infix2": "78", "suffs": [""]},
        {"bookNum": "79", "infix2": "79", "suffs": [""]},
        {"bookNum": "80", "infix2": "80", "suffs": [""]},
        {"bookNum": "pos%3D31", "infix2": "pos%3D31", "suffs": [""]},
        {"bookNum": "pos%3D32", "infix2": "pos%3D32", "suffs": [""]},
        {"bookNum": "pos%3D33", "infix2": "pos%3D33", "suffs": [""]},
        {"bookNum": "pos%3D34", "infix2": "pos%3D34", "suffs": [""]},
        {"bookNum": "pos%3D35", "infix2": "pos%3D35", "suffs": [""]}
    ]
}))
authors.append(dioChrysostom)

cassiusDio = utils.Author("CassiusDio")
cassiusDio.addWork(utils.TextSpec("Historia Romanae", "2008.01.0593", 80, "%3Abook%3D", {
    "multi": True,
    "suffixes": [
        {"bookNum": "1", "infix2": "", "suffs": ["1"]},
        {"bookNum": "2", "infix2": "", "suffs": ["2"]},
        {"bookNum": "3", "infix2": "", "suffs": ["3"]},
        {"bookNum": "4", "infix2": "", "suffs": ["4"]},
        {"bookNum": "5", "infix2": "", "suffs": ["5"]},
        {"bookNum": "6", "infix2": "", "suffs": ["6"]},
        {"bookNum": "7", "infix2": "", "suffs": ["7"]},
        {"bookNum": "8", "infix2": "", "suffs": ["8"]},
        {"bookNum": "9", "infix2": "", "suffs": ["9"]},
        {"bookNum": "10", "infix2": "", "suffs": ["10"]},
        {"bookNum": "11", "infix2": "", "suffs": ["11"]},
        {"bookNum": "12", "infix2": "", "suffs": ["12"]},
        {"bookNum": "13", "infix2": "", "suffs": ["13"]},
        {"bookNum": "14", "infix2": "", "suffs": ["14"]},
        {"bookNum": "15", "infix2": "", "suffs": ["15"]},
        {"bookNum": "16", "infix2": "", "suffs": ["16"]},
        {"bookNum": "17", "infix2": "", "suffs": ["17"]},
        {"bookNum": "18", "infix2": "", "suffs": ["18"]},
        {"bookNum": "19", "infix2": "", "suffs": ["19"]},
        {"bookNum": "20", "infix2": "", "suffs": ["20"]},
        {"bookNum": "21", "infix2": "", "suffs": ["21"]},
        {"bookNum": "22", "infix2": "", "suffs": ["22"]},
        {"bookNum": "23", "infix2": "", "suffs": ["23"]},
        {"bookNum": "24", "infix2": "", "suffs": ["24"]},
        {"bookNum": "25", "infix2": "", "suffs": ["25"]},
        {"bookNum": "26", "infix2": "", "suffs": ["26"]},
        {"bookNum": "27", "infix2": "", "suffs": ["27"]},
        {"bookNum": "28", "infix2": "", "suffs": ["28"]},
        {"bookNum": "29", "infix2": "", "suffs": ["29"]},
        {"bookNum": "30-35", "infix2": "", "suffs": ["30-35"]},
        {"bookNum": "unknown", "infix2": "", "suffs": ["unknown"]},
        {"bookNum": "36", "infix2": "", "suffs": ["36"]},
        {"bookNum": "37", "infix2": "", "suffs": ["37"]},
        {"bookNum": "38", "infix2": "", "suffs": ["38"]},
        {"bookNum": "39", "infix2": "", "suffs": ["39"]},
        {"bookNum": "40", "infix2": "", "suffs": ["40"]},
        {"bookNum": "41", "infix2": "", "suffs": ["41"]},
        {"bookNum": "42", "infix2": "", "suffs": ["42"]},
        {"bookNum": "43", "infix2": "", "suffs": ["43"]},
        {"bookNum": "44", "infix2": "", "suffs": ["44"]},
        {"bookNum": "45", "infix2": "", "suffs": ["45"]},
        {"bookNum": "46", "infix2": "", "suffs": ["46"]},
        {"bookNum": "pos%3D43", "infix2": "", "suffs": ["pos%3D43"]},
        {"bookNum": "48", "infix2": "", "suffs": ["48"]}, # same as pos%3D44
        {"bookNum": "49", "infix2": "", "suffs": ["49"]},
        {"bookNum": "50", "infix2": "", "suffs": ["50"]},
        {"bookNum": "51", "infix2": "", "suffs": ["51"]},
        {"bookNum": "52", "infix2": "", "suffs": ["52"]},
        {"bookNum": "53", "infix2": "", "suffs": ["53"]},
        {"bookNum": "54", "infix2": "", "suffs": ["54"]},
        {"bookNum": "55", "infix2": "", "suffs": ["55"]},
        {"bookNum": "56", "infix2": "", "suffs": ["56"]},
        {"bookNum": "57fr", "infix2": "", "suffs": ["57fr"]},
        {"bookNum": "57", "infix2": "", "suffs": ["57"]},
        {"bookNum": "58", "infix2": "", "suffs": ["58"]},
        {"bookNum": "59", "infix2": "", "suffs": ["59"]},
        {"bookNum": "60", "infix2": "", "suffs": ["60"]},
        {"bookNum": "61", "infix2": "", "suffs": ["61"]},
        {"bookNum": "61b", "infix2": "", "suffs": ["61b"]},
        {"bookNum": "62", "infix2": "", "suffs": ["62"]},
        {"bookNum": "62b", "infix2": "", "suffs": ["62b"]},
        {"bookNum": "63", "infix2": "", "suffs": ["63"]},
        {"bookNum": "64b", "infix2": "", "suffs": ["64b"]},
        {"bookNum": "64", "infix2": "", "suffs": ["64"]},
        {"bookNum": "65", "infix2": "", "suffs": ["65"]},
        {"bookNum": "66", "infix2": "", "suffs": ["66"]},
        {"bookNum": "67", "infix2": "", "suffs": ["67"]},
        {"bookNum": "68", "infix2": "", "suffs": ["68"]},
        {"bookNum": "69", "infix2": "", "suffs": ["69"]},
        {"bookNum": "70", "infix2": "", "suffs": ["70"]},
        {"bookNum": "pos%3D71", "infix2": "", "suffs": ["pos%3D71"]},
        {"bookNum": "72", "infix2": "", "suffs": ["72"]},
        {"bookNum": "73", "infix2": "", "suffs": ["73"]},
        {"bookNum": "74", "infix2": "", "suffs": ["74"]},
        {"bookNum": "75", "infix2": "", "suffs": ["75"]},
        {"bookNum": "76", "infix2": "", "suffs": ["76"]},
        {"bookNum": "77", "infix2": "", "suffs": ["77"]},
        {"bookNum": "78", "infix2": "", "suffs": ["78"]},
        {"bookNum": "79", "infix2": "", "suffs": ["79"]},
        {"bookNum": "80", "infix2": "", "suffs": ["80"]},
        {"bookNum": "80b", "infix2": "", "suffs": ["80b"]}
    ]
}))
authors.append(cassiusDio)

diodorus = utils.Author("DiodorusSiculus")
diodorus.addWork(utils.TextSpec("Bibliotheca Historica", "", 20, "", {
    "multi": True,
    "suffixes": [
        {"bookNum": "1",   "infix2": "2008.01.0540%3Abook%3D1",   "suffs": [""]},
        {"bookNum": "2",   "infix2": "2008.01.0540%3Abook%3D2",   "suffs": [""]},
        {"bookNum": "3",   "infix2": "2008.01.0540%3Abook%3D3",   "suffs": [""]},
        {"bookNum": "4",   "infix2": "2008.01.0540%3Abook%3D4",   "suffs": [""]},
        {"bookNum": "5",   "infix2": "2008.01.0540%3Abook%3D5",   "suffs": [""]},
        {"bookNum": "9",   "infix2": "1999.01.0083%3Abook%3D9",   "suffs": [""]},
        {"bookNum": "10",  "infix2": "1999.01.0083%3Abook%3D10",  "suffs": [""]},
        {"bookNum": "11",  "infix2": "1999.01.0083%3Abook%3D11",  "suffs": [""]},
        {"bookNum": "12",  "infix2": "1999.01.0083%3Abook%3D12",  "suffs": [""]},
        {"bookNum": "13",  "infix2": "1999.01.0083%3Abook%3D13",  "suffs": [""]},
        {"bookNum": "14",  "infix2": "1999.01.0083%3Abook%3D14",  "suffs": [""]},
        {"bookNum": "15",  "infix2": "1999.01.0083%3Abook%3D15",  "suffs": [""]},
        {"bookNum": "16",  "infix2": "1999.01.0083%3Abook%3D16",  "suffs": [""]},
        {"bookNum": "17",  "infix2": "1999.01.0083%3Abook%3D17",  "suffs": [""]},
        {"bookNum": "18",  "infix2": "2008.01.0541%3Abook%3D18",  "suffs": [""]},
        {"bookNum": "19",  "infix2": "2008.01.0541%3Abook%3D19",  "suffs": [""]},
        {"bookNum": "20",  "infix2": "2008.01.0541%3Abook%3D20",  "suffs": [""]}
    ]
}))
authors.append(diodorus)

diogenesLaertius = utils.Author("DiogenesLaertius")
diogenesLaertius.addWork(utils.TextSpec("Lives of Eminent Philosophers", "1999.01.0257", 10, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(diogenesLaertius)

dionysiusOfHalicarnassus = utils.Author("DionysiusOfHalicarnassus")
dionysiusOfHalicarnassus.addWork(utils.TextSpec("Antiquitates Romanae", "2008.01.0572", 19, "%3Abook%3D", {
    "multi": True,
    "suffixes": [
        {"bookNum": "1",   "infix2": "1",   "suffs": [""]},
        {"bookNum": "2",   "infix2": "2",   "suffs": [""]},
        {"bookNum": "3",   "infix2": "3",   "suffs": [""]},
        {"bookNum": "4",   "infix2": "4",   "suffs": [""]},
        {"bookNum": "5",   "infix2": "5",   "suffs": [""]},
        {"bookNum": "9",   "infix2": "9",   "suffs": [""]},
        {"bookNum": "10",  "infix2": "10",  "suffs": [""]},
        {"bookNum": "11",  "infix2": "11",  "suffs": [""]},
        {"bookNum": "12",  "infix2": "12",  "suffs": [""]},
        {"bookNum": "13",  "infix2": "13",  "suffs": [""]},
        {"bookNum": "14",  "infix2": "14",  "suffs": [""]},
        {"bookNum": "15",  "infix2": "15",  "suffs": [""]},
        {"bookNum": "16",  "infix2": "16",  "suffs": [""]},
        {"bookNum": "17-18",  "infix2": "17-18",  "suffs": [""]},
        {"bookNum": "19",  "infix2": "19",  "suffs": [""]},
        {"bookNum": "20",  "infix2": "20",  "suffs": [""]}
    ]
}))
dionysiusOfHalicarnassus.addWork(utils.TextSpec("De Antiquis Oratibus", "2008.01.0576", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 4+1)
}))
dionysiusOfHalicarnassus.addWork(utils.TextSpec("De Lysia", "2008.01.0577", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, "pos%3D15", 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
}))
dionysiusOfHalicarnassus.addWork(utils.TextSpec("De Isocrate", "2008.01.0578", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 20+1)
}))
dionysiusOfHalicarnassus.addWork(utils.TextSpec("De Isaeo", "2008.01.0579", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 20+1)
}))
dionysiusOfHalicarnassus.addWork(utils.TextSpec("De Demothene", "2008.01.0580", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]
}))
dionysiusOfHalicarnassus.addWork(utils.TextSpec("Ad Ammaeum", "2008.01.0582", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 12+1)
}))
dionysiusOfHalicarnassus.addWork(utils.TextSpec("De Thucydidis Idiomatibus", "2008.01.0585", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 17+1)
}))
dionysiusOfHalicarnassus.addWork(utils.TextSpec("De Compositione Verborum", "2008.01.0586", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 26+1)
}))
dionysiusOfHalicarnassus.addWork(utils.TextSpec("De Thucydide", "2008.01.0584", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 55+1)
}))
dionysiusOfHalicarnassus.addWork(utils.TextSpec("Epistula ad Pompeium Geminum", "2008.01.0587", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 6+1)
}))
authors.append(dionysiusOfHalicarnassus)

# one could grab the fragments from Elegy and Iambus here, but since the goal in this is to get full books worth of text, fragments aren't very useful.


epictetus = utils.Author("Epictetus")
epictetus.addWork(utils.TextSpec("Discourses", "1999.01.0235", 4, "%3Atext%3Ddisc%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
epictetus.addWork(utils.TextSpec("Enchiridion", "1999.01.0235", 1, "%3Atext%3Denc%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 53+1)
}))
epictetus.addWork(utils.TextSpec("Fragments", "1999.01.0235", 1, "%3Atext%3Dfrag%3Abook%3D", {
    "multi": False,
    "suffixes": [0, 2, 3]
}))
authors.append(epictetus)

euclid = utils.Author("Euclid")
euclid.addWork(utils.TextSpec("Elements", "1999.01.0085", 13, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(euclid)

euripides = utils.Author("Euripides")
euripides.addWork(utils.TextSpec("Alcestis", "1999.01.0087", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "28", "38", "77", "86", "93", "98", "105", "112", "121", "132", "136", "213", "226", "238", "244", "246", "248", "250", "252", "257", "259", "264", "266", "273", "280", "328", "371", "393", "404", "406", "416", "435", "445", "455", "466", "477", "507", "536", "568", "578", "588", "597", "606", "629", "675", "708", "741", "747", "773", "816", "861", "872", "878", "889", "895", "903", "912", "926", "935", "962", "973", "984", "995", "1006", "1037", "1072", "1118", "1159"]
}))
euripides.addWork(utils.TextSpec("Andromache", "1999.01.0089", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "56", "103", "117", "126", "135", "141", "147", "183", "232", "274", "284", "293", "301", "309", "352", "384", "425", "464", "471", "479", "486", "494", "501", "515", "523", "537", "545", "590", "642", "693", "729", "766", "777", "788", "802", "825", "829", "833", "837", "841", "851", "854", "866", "907", "957", "1009", "1019", "1028", "1037", "1047", "1085", "1117", "1166", "1173", "1184", "1186", "1197", "1214", "1226", "1231", "1284"]
}))
euripides.addWork(utils.TextSpec("Bacchae", "1999.01.0091", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "43", "64", "73", "88", "105", "120", "135", "170", "215", "266", "298", "343", "370", "386", "402", "417", "434", "476", "519", "537", "556", "576", "604", "642", "677", "728", "775", "810", "862", "882", "902", "912", "945", "977", "997", "1017", "1024", "1043", "1084", "1114", "1153", "1165", "1168", "1184", "1200", "1244", "1280", "1330", "1368"]
}))
euripides.addWork(utils.TextSpec("Cyclops", "1999.01.0093", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "41", "49", "55", "63", "82", "131", "175", "203", "241", "273", "316", "356", "361", "370", "375", "409", "441", "483", "495", "503", "511", "519", "566", "608", "624", "656", "663"]
}))
euripides.addWork(utils.TextSpec("Electra", "1999.01.0095", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "50", "82", "112", "125", "127", "140", "150", "157", "167", "190", "213", "262", "300", "341", "364", "401", "432", "442", "452", "464", "476", "487", "524", "547", "585", "596", "646", "671", "699", "713", "726", "737", "747", "774", "819", "859", "866", "873", "880", "907", "957", "988", "998", "1035", "1060", "1100", "1147", "1155", "1165", "1172", "1177", "1190", "1206", "1214", "1221", "1227", "1233", "1238", "1264", "1292", "1321"]
}))
euripides.addWork(utils.TextSpec("Hecuba", "1999.01.0097", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "35", "59", "98", "130", "154", "177", "197", "216", "251", "299", "342", "382", "402", "444", "455", "466", "475", "484", "518", "553", "585", "629", "638", "648", "658", "681", "722", "767", "812", "864", "905", "914", "923", "933", "943", "953", "986", "1025", "1035", "1056", "1085", "1089", "1107", "1145", "1187", "1217", "1252", "1293"]
}))
euripides.addWork(utils.TextSpec("Helen", "1999.01.0099", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "31", "68", "115", "164", "167", "179", "191", "211", "229", "253", "293", "330", "362", "375", "386", "437", "476", "515", "528", "566", "597", "625", "666", "698", "734", "758", "793", "832", "865", "894", "944", "969", "998", "1032", "1067", "1107", "1122", "1137", "1151", "1165", "1206", "1250", "1301", "1319", "1338", "1353", "1369", "1412", "1451", "1465", "1478", "1495", "1512", "1554", "1577", "1621", "1642", "1688"]
}))
euripides.addWork(utils.TextSpec("Heracleidae", "1999.01.0103", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "48", "73", "95", "111", "134", "181", "232", "253", "288", "297", "333", "353", "362", "371", "381", "427", "474", "520", "567", "608", "618", "630", "660", "702", "709", "748", "759", "770", "777", "784", "830", "869", "892", "901", "910", "919", "928", "975", "1018", "1053"]
}))
euripides.addWork(utils.TextSpec("Heracles", "1999.01.0101", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "26", "60", "107", "119", "130", "138", "170", "217", "252", "275", "316", "348", "359", "364", "375", "380", "389", "394", "403", "408", "419", "425", "436", "442", "451", "497", "534", "562", "599", "637", "655", "673", "687", "701", "735", "751", "763", "772", "781", "798", "815", "822", "855", "875", "922", "950", "977", "1016", "1039", "1042", "1086", "1131", "1178", "1214", "1255", "1294", "1340", "1389", "1427"]
}))
euripides.addWork(utils.TextSpec("Hippolytus", "1999.01.0105", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "34", "58", "73", "121", "131", "141", "151", "161", "170", "198", "239", "267", "313", "362", "373", "419", "459", "486", "525", "535", "545", "555", "565", "571", "575", "577", "581", "585", "589", "591", "596", "601", "638", "669", "680", "732", "742", "752", "764", "776", "811", "817", "834", "836", "852", "856", "866", "874", "877", "891", "936", "983", "1021", "1060", "1102", "1111", "1120", "1131", "1142", "1151", "1198", "1243", "1268", "1283", "1296", "1342", "1370", "1389", "1431", "1462"]
}))
euripides.addWork(utils.TextSpec("Ion", "1999.01.0109", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "41", "82", "112", "128", "144", "184", "194", "205", "219", "237", "275", "308", "355", "401", "452", "472", "492", "510", "544", "566", "607", "650", "676", "695", "714", "725", "774", "808", "836", "859", "881", "907", "923", "966", "998", "1048", "1061", "1074", "1090", "1106", "1132", "1177", "1201", "1229", "1244", "1250", "1261", "1282", "1320", "1369", "1395", "1437", "1468", "1510", "1553", "1571", "1606"]
}))
euripides.addWork(utils.TextSpec("Iphigenia in Aulis", "1999.01.0107", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "80", "3", "115", "164", "185", "206", "231", "242", "253", "265", "277", "288", "303", "317", "349", "376", "378", "402", "440", "471", "506", "543", "558", "573", "590", "607", "640", "677", "716", "751", "762", "773", "801", "831", "855", "900", "917", "944", "992", "1036", "1058", "1080", "1098", "1146", "1185", "1211", "1255", "1276", "1313", "1336", "1338", "1374", "1402", "1433", "1475", "1500", "1532", "1578", "1615", "1621", "1627"]
}))
euripides.addWork(utils.TextSpec("Iphigenia in Tauris", "1999.01.0111", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "42", "67", "93", "123", "143", "178", "203", "236", "260", "295", "342", "392", "407", "421", "439", "456", "467", "492", "540", "578", "617", "644", "658", "687", "725", "769", "798", "827", "868", "900", "939", "987", "1017", "1056", "1089", "1106", "1123", "1138", "1153", "1203", "1234", "1259", "1284", "1327", "1364", "1390", "1435", "1475", "1490"]
}))
euripides.addWork(utils.TextSpec("Medea", "1999.01.0113", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "49", "96", "131", "139", "148", "160", "173", "184", "205", "214", "252", "292", "324", "357", "364", "410", "421", "431", "439", "446", "492", "522", "545", "588", "627", "636", "645", "654", "663", "689", "731", "759", "764", "790", "824", "835", "846", "856", "866", "908", "941", "976", "983", "990", "996", "1002", "1049", "1081", "1116", "1136", "1181", "1231", "1251", "1261", "1273", "1282", "1293", "1323", "1361", "1389"]
}))
euripides.addWork(utils.TextSpec("Orestes", "1999.01.0115", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "34", "71", "110", "140", "153", "166", "187", "208", "253", "280", "316", "332", "348", "356", "385", "427", "470", "507", "544", "591", "640", "682", "729", "763", "786", "807", "819", "831", "844", "866", "898", "931", "960", "971", "982", "1013", "1018", "1069", "1105", "1155", "1204", "1246", "1266", "1286", "1302", "1311", "1353", "1366", "1393", "1425", "1473", "1506", "1537", "1549", "1554", "1598", "1625", "1666", "1682"]
}))
euripides.addWork(utils.TextSpec("Phoenissae", "1999.01.0117", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "32", "69", "103", "145", "193", "203", "214", "226", "239", "250", "261", "293", "327", "355", "387", "427", "469", "499", "549", "588", "614", "638", "657", "676", "690", "737", "784", "801", "818", "834", "865", "911", "960", "991", "1019", "1043", "1067", "1104", "1153", "1202", "1242", "1284", "1296", "1307", "1310", "1335", "1340", "1390", "1427", "1454", "1480", "1485", "1530", "1555", "1582", "1625", "1672", "1710", "1758", "1764"]
}))
euripides.addWork(utils.TextSpec("Rhesus", "1999.01.0119", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "23", "34", "41", "52", "85", "131", "137", "164", "195", "201", "224", "233", "242", "254", "264", "284", "319", "342", "351", "360", "370", "379", "388", "422", "454", "467", "488", "527", "546", "565", "595", "642", "675", "683", "692", "710", "728", "733", "736", "738", "745", "747", "754", "780", "820", "833", "882", "890", "895", "904", "906", "915", "952", "993"]
}))
euripides.addWork(utils.TextSpec("Suppliants", "1999.01.0121", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "42", "48", "54", "63", "71", "79", "87", "113", "162", "195", "219", "253", "271", "286", "334", "365", "369", "373", "377", "381", "399", "426", "465", "494", "549", "598", "608", "618", "626", "634", "673", "726", "778", "786", "794", "798", "811", "824", "837", "881", "918", "925", "955", "963", "971", "980", "990", "1009", "1012", "1031", "1072", "1080", "1114", "1123", "1132", "1139", "1146", "1153", "1159", "1165", "1196", "1232"]
}))
euripides.addWork(utils.TextSpec("Trojan Women", "1999.01.0123", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "48", "98", "122", "153", "176", "197", "214", "230", "239", "278", "292", "308", "341", "386", "424", "444", "462", "511", "531", "551", "568", "577", "582", "587", "591", "595", "601", "608", "634", "673", "709", "740", "782", "799", "809", "820", "840", "860", "895", "945", "987", "1033", "1060", "1071", "1081", "1100", "1118", "1123", "1156", "1168", "1216", "1218", "1226", "1232", "1235", "1240", "1251", "1260", "1287", "1302", "1317"]
}))
authors.append(euripides)

eusebius = utils.Author("EusebiusOfCaesarea")
eusebius.addWork(utils.TextSpec("Historia Ecclesiastica", "2008.01.0640", 10, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(eusebius)

galen = utils.Author("Galen")
galen.addWork(utils.TextSpec("On the Natural Faculties", "1999.01.0255", 3, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(galen)

# anthology would be here if you wanted everything.

valeriusHarpocration = utils.Author("ValeriusHarpocration")
valeriusHarpocration.addWork(utils.TextSpec("Lexion in decem oratores Atticos", "2013.01.0002", 3, "%3Aletter%3D", {
    "multi": False,
    "suffixes": ["a", "b", "g", "d", "e", "z", "h", "q", "i", "k", "l", "m", "n", "c", "o", "p", "r", "s", "t", "u", "f", "y"]
}))
authors.append(valeriusHarpocration)

herodotus = utils.Author("Herodotus")
herodotus.addWork(utils.TextSpec("The Histories", "1999.01.0125", 9, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(herodotus)

hesiod = utils.Author("Hesiod")
hesiod.addWork(utils.TextSpec("Shield of Heracles", "1999.01.0127", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "39", "78", "115", "154", "178", "216", "245", "280", "327", "365", "402", "443"]
}))
hesiod.addWork(utils.TextSpec("Theogony", "1999.01.0129", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "29", "53", "63", "104", "139", "173", "207", "240", "270", "304", "337", "371", "404", "453", "492", "507", "545", "585", "617", "654", "687", "729", "767", "807", "820", "853", "886", "901", "938", "963", "1003"]
}))
hesiod.addWork(utils.TextSpec("Works and Days", "1999.01.0131", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "11", "42", "59", "83", "109", "140", "174", "202", "238", "274", "320", "370", "405", "448", "479", "504", "536", "571", "609", "641", "678", "706", "737", "765", "800"]
}))
authors.append(hesiod)

hippocrates = utils.Author("Hippocrates")
hippocrates.addWork(utils.TextSpec("Works1", "1999.01.0249", 1, "%3Atext%3D", {
    "multi": True,
    "suffixes": [
        {"bookNum": "De prisca medicina",   "infix2": "VM%3Asection%3D",   "suffs": range(1, 24+1)},
        {"bookNum": "De aere aquis et locis",   "infix2": "Aer.%3Asection%3D",   "suffs": range(1, 24+1)},
        {"bookNum": "De moribus popularibus 1",   "infix2": "Epid.%3Abook%3D",   "suffs": [1]},
        {"bookNum": "De moribus popularibus 3",   "infix2": "Epid.%3Abook%3D",   "suffs": [3]},
        {"bookNum": "Jusjurandum",   "infix2": "Jusj.%3Asection%3D",   "suffs": range(1, 1+1)},
        {"bookNum": "Praeceptiones",   "infix2": "Praec.%3Asection%3D",   "suffs": range(1, 14+1)},
        {"bookNum": "De alimento",   "infix2": "Alim.%3Asection%3D",   "suffs": range(1, 55+1)}
    ]
}))
hippocrates.addWork(utils.TextSpec("Works2", "1999.01.0250", 1, "%3Atext%3D", {
    "multi": True,
    "suffixes": [
        {"bookNum": "1",   "infix2": "acut.",   "suffs": [""]},
        {"bookNum": "2",   "infix2": "Acut.+sp.",   "suffs": [""]},
        {"bookNum": "3",   "infix2": "haem.",   "suffs": [""]},
        {"bookNum": "4",   "infix2": "fist.",   "suffs": [""]},
        {"bookNum": "5",   "infix2": "ulc.",   "suffs": [""]},
        {"bookNum": "6",   "infix2": "art.",   "suffs": [""]},
        {"bookNum": "7",   "infix2": "mochl.",   "suffs": [""]},
        {"bookNum": "8",   "infix2": "Aph.",   "suffs": [""]},
        {"bookNum": "9",   "infix2": "prog.",   "suffs": [""]},
        {"bookNum": "10",   "infix2": "fract.",   "suffs": [""]},
        {"bookNum": "11",   "infix2": "Morb.+sacr.",   "suffs": [""]},
        {"bookNum": "12",   "infix2": "vc",   "suffs": [""]},
        {"bookNum": "13",   "infix2": "off.",   "suffs": [""]}
    ]
}))
authors.append(hippocrates)

homer = utils.Author("Homer")
homer.addWork(utils.TextSpec("Iliad", "1999.01.0133", 24, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
homer.addWork(utils.TextSpec("Odyssey", "1999.01.0135", 24, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(homer)

anonHymns0 = utils.Author("Anonymous(Hymns_Dionysus)")
anonHymns0.addWork(utils.TextSpec("Hymn to Dionysus", "1999.01.0137", 1, "%3Ahymn%3D", {
    "multi": False,
    "suffixes": ["1"]
}))
authors.append(anonHymns0)

anonHymns1 = utils.Author("Anonymous(Hymns_Demeter)")
anonHymns1.addWork(utils.TextSpec("Hymn to Demeter", "1999.01.0137", 1, "%3Ahymn%3D", {
    "multi": False,
    "suffixes": ["2"]
}))
authors.append(anonHymns1)

anonHymns2 = utils.Author("Anonymous(Hymns_Apollo)")
anonHymns2.addWork(utils.TextSpec("Hymn to Apollo", "1999.01.0137", 1, "%3Ahymn%3D", {
    "multi": False,
    "suffixes": ["3"]
}))
authors.append(anonHymns2)

anonHymns3 = utils.Author("Anonymous(Hymns_Hermes)")
anonHymns3.addWork(utils.TextSpec("Hymn to Hermes", "1999.01.0137", 1, "%3Ahymn%3D", {
    "multi": False,
    "suffixes": ["4"]
}))
authors.append(anonHymns3)

anonHymns4 = utils.Author("Anonymous(Hymns_Aphrodite)")
anonHymns4.addWork(utils.TextSpec("Hymn to Aphrodite", "1999.01.0137", 1, "%3Ahymn%3D", {
    "multi": False,
    "suffixes": ["5"]
}))
authors.append(anonHymns4)

anonHymns5 = utils.Author("Anonymous(Hymns_Rest)")
anonHymns5.addWork(utils.TextSpec("Short Homeric Hymns", "1999.01.0137", 1, "%3Ahymn%3D", {
    "multi": False,
    "suffixes": range(6, 33+1)
}))
authors.append(anonHymns5)

hyperides = utils.Author("Hyperides")
hyperides.addWork(utils.TextSpec("Speeches", "1999.01.0139", 6, "%3Aspeech%3D", {
    "multi": True,
    "suffixes": [
        {"bookNum": "1",   "infix2": "1%3Asection%3D",   "suffs": range(1, 20+1)},
        {"bookNum": "2",   "infix2": "2%3Asection%3D",   "suffs": range(1, 13+1)},
        {"bookNum": "3",   "infix2": "3%3Asection%3D",   "suffs": range(1, 36+1)},
        {"bookNum": "4",   "infix2": "4%3Asection%3D",   "suffs": range(1, 41+1)},
        {"bookNum": "5",   "infix2": "5%3Afragment%3D",   "suffs": [1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d"]},
        {"bookNum": "6",   "infix2": "6%3Asection%3D",   "suffs": range(1, 43+1)}
    ]
}))
authors.append(hyperides)

isaeus = utils.Author("Isaeus")
isaeus.addWork(utils.TextSpec("Speeches", "1999.01.0141", 12, "%3Aspeech%3D", {
    "multi": True,
    "suffixes": [
        {"bookNum": "1",    "infix2": "1%3Asection%3D",    "suffs": range(1, 51+1)},
        {"bookNum": "2",    "infix2": "2%3Asection%3D",    "suffs": range(1, 47+1)},
        {"bookNum": "3",    "infix2": "3%3Asection%3D",    "suffs": range(1, 80+1)},
        {"bookNum": "4",    "infix2": "4%3Asection%3D",    "suffs": range(1, 31+1)},
        {"bookNum": "5",    "infix2": "5%3Asection%3D",    "suffs": range(1, 47+1)},
        {"bookNum": "6",    "infix2": "6%3Asection%3D",    "suffs": range(1, 65+1)},
        {"bookNum": "7",    "infix2": "7%3Asection%3D",    "suffs": range(1, 45+1)},
        {"bookNum": "8",    "infix2": "8%3Asection%3D",    "suffs": range(1, 46+1)},
        {"bookNum": "9",    "infix2": "9%3Asection%3D",    "suffs": range(1, 37+1)},
        {"bookNum": "10",   "infix2": "10%3Asection%3D",   "suffs": range(1, 26+1)},
        {"bookNum": "11",   "infix2": "11%3Asection%3D",   "suffs": range(1, 50+1)},
        {"bookNum": "12",   "infix2": "12%3Asection%3D",   "suffs": range(1, 12+1)}
    ]
}))
authors.append(isaeus)

isocrates = utils.Author("Isocrates")
isocrates.addWork(utils.TextSpec("Letters", "1999.01.0245", 1, "%3Acollection%3Dl.%3Aletter%3D", {
    "multi": False,
    "suffixes": range(1, 9+1)
}))
isocrates.addWork(utils.TextSpec("Speeches", "1999.01.0143", 21, "%3Aspeech%3D", {
    "multi": True,
    "suffixes": [
        {"bookNum": "1",    "infix2": "1%3Asection%3D",    "suffs": range(1, 52+1)},
        {"bookNum": "2",    "infix2": "2%3Asection%3D",    "suffs": range(1, 54+1)},
        {"bookNum": "3",    "infix2": "3%3Asection%3D",    "suffs": range(1, 64+1)},
        {"bookNum": "4",    "infix2": "4%3Asection%3D",    "suffs": range(1, 189+1)},
        {"bookNum": "5",    "infix2": "5%3Asection%3D",    "suffs": range(1, 155+1)},
        {"bookNum": "6",    "infix2": "6%3Asection%3D",    "suffs": range(1, 111+1)},
        {"bookNum": "7",    "infix2": "7%3Asection%3D",    "suffs": range(1, 84+1)},
        {"bookNum": "8",    "infix2": "8%3Asection%3D",    "suffs": range(1, 145+1)},
        {"bookNum": "9",    "infix2": "9%3Asection%3D",    "suffs": range(1, 81+1)},
        {"bookNum": "10",   "infix2": "10%3Asection%3D",   "suffs": range(1, 69+1)},
        {"bookNum": "11",   "infix2": "11%3Asection%3D",   "suffs": range(1, 50+1)},
        {"bookNum": "12",   "infix2": "12%3Asection%3D",   "suffs": range(1, 272+1)},
        {"bookNum": "13",   "infix2": "13%3Asection%3D",   "suffs": range(1, 22+1)},
        {"bookNum": "14",   "infix2": "14%3Asection%3D",   "suffs": range(1, 63+1)},
        {"bookNum": "15",   "infix2": "15%3Asection%3D",   "suffs": range(1, 323+1)},
        {"bookNum": "16",   "infix2": "16%3Asection%3D",   "suffs": range(1, 50+1)},
        {"bookNum": "17",   "infix2": "17%3Asection%3D",   "suffs": range(1, 58+1)},
        {"bookNum": "18",   "infix2": "18%3Asection%3D",   "suffs": range(1, 68+1)},
        {"bookNum": "19",   "infix2": "19%3Asection%3D",   "suffs": range(1, 51+1)},
        {"bookNum": "20",   "infix2": "20%3Asection%3D",   "suffs": range(1, 22+1)},
        {"bookNum": "21",   "infix2": "21%3Asection%3D",   "suffs": range(1, 21+1)},
    ]
}))
authors.append(isocrates)

johnOfDamascus = utils.Author("JohnOfDamascus")
johnOfDamascus.addWork(utils.TextSpec("Vita Barlaam et Joasaph", "2008.01.0666", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 40+1)
}))
authors.append(johnOfDamascus)

flaviusJosephus = utils.Author("FlaviusJosephus")
flaviusJosephus.addWork(utils.TextSpec("Antiquitates Judaicae", "1999.01.0145", 20, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
flaviusJosephus.addWork(utils.TextSpec("Contra Apionem", "1999.01.0215", 2, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
flaviusJosephus.addWork(utils.TextSpec("De Bello Judaico", "1999.01.0147", 7, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
flaviusJosephus.addWork(utils.TextSpec("Josephi Vitae", "1999.01.0149", 1, "%3Awhiston+section%3D", {
    "multi": False,
    "suffixes": range(1, 76+1)
}))
authors.append(flaviusJosephus)

longinus = utils.Author("Longinus")
longinus.addWork(utils.TextSpec("De Sublimitate", "2008.01.0639", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 44+1)
}))
authors.append(longinus)

longus = utils.Author("Longus")
longus.addWork(utils.TextSpec("Daphne and Chloe", "2008.01.0642", 4, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(longus)

lucian = utils.Author("Lucian")
lucian.addWork(utils.TextSpec("Abdicatus", "2008.01.0471", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 32+1)
}))
lucian.addWork(utils.TextSpec("Adversus indoctum et libros multos ementem", "2008.01.0447", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": list(chain(range(1, 22+1), range(203, 203+1), range(24,30+1)))
}))
lucian.addWork(utils.TextSpec("Alexander", "2008.01.0457", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1,61+1)
}))
lucian.addWork(utils.TextSpec("Anacharsis", "2008.01.0453", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 40+1)
}))
lucian.addWork(utils.TextSpec("Apologia", "2008.01.0517", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 15+1)
}))
lucian.addWork(utils.TextSpec("Bacchus", "2008.01.0422", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 8+1)
}))
lucian.addWork(utils.TextSpec("Bis accusatus sive tribunalia", "2008.01.0445", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 35+1)
}))
lucian.addWork(utils.TextSpec("Calumniae non temere credundum", "2008.01.0432", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 31+1)
}))
lucian.addWork(utils.TextSpec("Cataplus", "2008.01.0435", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 28+1)
}))
lucian.addWork(utils.TextSpec("Contemplantes", "2008.01.0442", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 24+1)
}))
lucian.addWork(utils.TextSpec("De Astrologia", "2008.01.0467", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 29+1)
}))
lucian.addWork(utils.TextSpec("De Domo", "2008.01.0428", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 32+1)
}))
lucian.addWork(utils.TextSpec("De Luctu", "2008.01.0455", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 24+1)
}))
lucian.addWork(utils.TextSpec("De Mercede", "2008.01.0452", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 42+1)
}))
lucian.addWork(utils.TextSpec("De Morte Peregrini", "2008.01.0461", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 45+1)
}))
lucian.addWork(utils.TextSpec("De parasito sive artem esse parasiticam", "2008.01.0449", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 61+1)
}))
lucian.addWork(utils.TextSpec("De Sacrificiis", "2008.01.0446", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 15+1)
}))
lucian.addWork(utils.TextSpec("De Saltatione", "2008.01.0464", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 85+1)
}))
lucian.addWork(utils.TextSpec("De Syria Dea", "2008.01.0460", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 60+1)
}))
lucian.addWork(utils.TextSpec("Dearum judicium", "2008.01.0451", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 16+1)
}))
lucian.addWork(utils.TextSpec("Demonax", "2008.01.0427", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 67+1)
}))
lucian.addWork(utils.TextSpec("Deorum Concilium", "2008.01.0469", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 19+1)
}))
lucian.addWork(utils.TextSpec("Dialogi deorum", "2008.01.0526", 1, "%3Abook%3D", {
    "multi": False,
    "suffixes": range(1, 26+1)
}))
lucian.addWork(utils.TextSpec("Dialogi Marini", "2008.01.0525", 1, "%3Abook%3D", {
    "multi": False,
    "suffixes": range(1, 15+1)
}))
lucian.addWork(utils.TextSpec("Dialogi Meretricii", "2008.01.0527", 1, "%3Abook%3D", {
    "multi": False,
    "suffixes": range(1, 15+1)
}))
lucian.addWork(utils.TextSpec("Dialogi Mortuorum", "2008.01.0524", 1, "%3Abook%3D", {
    "multi": False,
    "suffixes": range(1, 30+1)
}))
lucian.addWork(utils.TextSpec("Dipsades", "2008.01.0512", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 9+1)
}))
lucian.addWork(utils.TextSpec("Electrum", "2008.01.0424", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 6+1)
}))
lucian.addWork(utils.TextSpec("Eunuchus", "2008.01.0466", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 13+1)
}))
lucian.addWork(utils.TextSpec("Fugitivi", "2008.01.0462", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 33+1)
}))
lucian.addWork(utils.TextSpec("Gallus", "2008.01.0438", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 33+1)
}))
lucian.addWork(utils.TextSpec("Harmonides", "2008.01.0518", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 4+1)
}))
lucian.addWork(utils.TextSpec("Hercules", "2008.01.0423", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 8+1)
}))
lucian.addWork(utils.TextSpec("Hermotimus", "2008.01.0521", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 86+1)
}))
lucian.addWork(utils.TextSpec("Herodotus", "2008.01.0514", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 8+1)
}))
lucian.addWork(utils.TextSpec("Hesiod", "2008.01.0519", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 9+1)
}))
lucian.addWork(utils.TextSpec("Hippias", "2008.01.0421", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 8+1)
}))
lucian.addWork(utils.TextSpec("Icaromenippus", "2008.01.0440", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 34+1)
}))
lucian.addWork(utils.TextSpec("Imagines", "2008.01.0458", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 23+1)
}))
lucian.addWork(utils.TextSpec("Judicium Vocalium", "2008.01.0433", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 12+1)
}))
lucian.addWork(utils.TextSpec("Juppiter Confuatus", "2008.01.0436", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 19+1)
}))
lucian.addWork(utils.TextSpec("Juppiter Trageodeus", "2008.01.0437", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 53+1)
}))
lucian.addWork(utils.TextSpec("Lexiphanes", "2008.01.0465", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 25+1)
}))
lucian.addWork(utils.TextSpec("Macrobii", "2008.01.0430", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 29+1)
}))
lucian.addWork(utils.TextSpec("Muscae Encomium", "2008.01.0425", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 12+1)
}))
lucian.addWork(utils.TextSpec("Navigium", "2008.01.0523", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 46+1)
}))
lucian.addWork(utils.TextSpec("Necyomantia", "2008.01.0454", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 22+1)
}))
lucian.addWork(utils.TextSpec("Nigrinus", "2008.01.0426", 1, "%3Awork%3D1%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 38+1)
}))
lucian.addWork(utils.TextSpec("Patriae Encomium", "2008.01.0429", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 12+1)
}))
lucian.addWork(utils.TextSpec("Phalaris", "2008.01.0420", 1, "%3Abook%3D", {
    "multi": False,
    "suffixes": range(1, 2+1)
}))
lucian.addWork(utils.TextSpec("Philopsuedes Sive Incredulus", "2008.01.0450", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 40+1)
}))
lucian.addWork(utils.TextSpec("Piscator", "2008.01.0444", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 52+1)
}))
lucian.addWork(utils.TextSpec("Podagra", "2008.01.0529", 1, "%3Atext%3D", {
    "multi": False,
    "suffixes": range(1, 1+1)
}))
lucian.addWork(utils.TextSpec("Pro Imaginibus", "2008.01.0459", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 29+1)
}))
lucian.addWork(utils.TextSpec("Prometheus", "2008.01.0439", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 21+1)
}))
lucian.addWork(utils.TextSpec("Prometheus Es In Verbis", "2008.01.0522", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 7+1)
}))
lucian.addWork(utils.TextSpec("Pseudologista", "2008.01.0468", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 32+1)
}))
lucian.addWork(utils.TextSpec("Quomodo Historia Conscribenda Sit", "2008.01.0511", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 63+1)
}))
lucian.addWork(utils.TextSpec("Rhetorum Praeceptor", "2008.01.0456", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 26+1)
}))
lucian.addWork(utils.TextSpec("Saturnalia", "2008.01.0513", 1, "%3Atext%3D", {
    "multi": False,
    "suffixes": range(1, 3+1)
}))
lucian.addWork(utils.TextSpec("Scytha", "2008.01.0520", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 11+1)
}))
lucian.addWork(utils.TextSpec("Soleocista", "2008.01.0528", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 12+1)
}))
lucian.addWork(utils.TextSpec("Somnium Sive Vita Luciani", "2008.01.0448", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 18+1)
}))
lucian.addWork(utils.TextSpec("Symposium", "2008.01.0434", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 48+1)
}))
lucian.addWork(utils.TextSpec("Timon", "2008.01.0441", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 58+1)
}))
lucian.addWork(utils.TextSpec("Tyrannicida", "2008.01.0470", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 22+1)
}))
lucian.addWork(utils.TextSpec("Verae Historiae", "2008.01.0431", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 47+1)
}))
lucian.addWork(utils.TextSpec("Vitarum Auctio", "2008.01.0443", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": list(chain(range(1, 17+1), range(19,27+1)))
}))
lucian.addWork(utils.TextSpec("Zeuxis", "2008.01.0515", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1,12+1)
}))
authors.append(lucian)

lycophron = utils.Author("Lycophron")
lycophron.addWork(utils.TextSpec("Alexandra", "2008.01.0484", 1, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(lycophron)

lycurgus = utils.Author("Lycurgus")
lycurgus.addWork(utils.TextSpec("Against Leocrates", "1999.01.0151", 1, "%3Aspeech%3D1%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 150+1)
}))
authors.append(lycurgus)

lysias = utils.Author("Lysias")
lysias.addWork(utils.TextSpec("Speeches", "1999.01.0153", 1, "%3Aspeech%3D", {
    "multi": True,
    "suffixes": [
        {"bookNum": "1",    "infix2": "1%3Asection%3D",    "suffs": range(1, 50+1)},
        {"bookNum": "2",    "infix2": "2%3Asection%3D",    "suffs": range(1, 81+1)},
        {"bookNum": "3",    "infix2": "3%3Asection%3D",    "suffs": range(1, 48+1)},
        {"bookNum": "4",    "infix2": "4%3Asection%3D",    "suffs": range(1, 20+1)},
        {"bookNum": "5",    "infix2": "5%3Asection%3D",    "suffs": range(1, 5+1)},
        {"bookNum": "6",    "infix2": "6%3Asection%3D",    "suffs": range(1, 55+1)},
        {"bookNum": "7",    "infix2": "7%3Asection%3D",    "suffs": range(1, 43+1)},
        {"bookNum": "8",    "infix2": "8%3Asection%3D",    "suffs": range(1, 20+1)},
        {"bookNum": "9",    "infix2": "9%3Asection%3D",    "suffs": range(1, 22+1)},
        {"bookNum": "10",   "infix2": "10%3Asection%3D",   "suffs": range(1, 32+1)},
        {"bookNum": "11",   "infix2": "11%3Asection%3D",   "suffs": range(1, 12+1)},
        {"bookNum": "12",   "infix2": "12%3Asection%3D",   "suffs": range(1, 100+1)},
        {"bookNum": "13",   "infix2": "13%3Asection%3D",   "suffs": range(1, 97+1)},
        {"bookNum": "14",   "infix2": "14%3Asection%3D",   "suffs": range(1, 47+1)},
        {"bookNum": "15",   "infix2": "15%3Asection%3D",   "suffs": range(1, 12+1)},
        {"bookNum": "16",   "infix2": "16%3Asection%3D",   "suffs": range(1, 21+1)},
        {"bookNum": "17",   "infix2": "17%3Asection%3D",   "suffs": range(1, 10+1)},
        {"bookNum": "18",   "infix2": "18%3Asection%3D",   "suffs": range(1, 27+1)},
        {"bookNum": "19",   "infix2": "19%3Asection%3D",   "suffs": range(1, 64+1)},
        {"bookNum": "20",   "infix2": "20%3Asection%3D",   "suffs": range(1, 36+1)},
        {"bookNum": "21",   "infix2": "21%3Asection%3D",   "suffs": range(1, 25+1)},
        {"bookNum": "22",   "infix2": "22%3Asection%3D",   "suffs": range(1, 22+1)},
        {"bookNum": "23",   "infix2": "23%3Asection%3D",   "suffs": range(1, 16+1)},
        {"bookNum": "24",   "infix2": "24%3Asection%3D",   "suffs": range(1, 27+1)},
        {"bookNum": "25",   "infix2": "25%3Asection%3D",   "suffs": range(1, 35+1)},
        {"bookNum": "26",   "infix2": "26%3Asection%3D",   "suffs": range(1, 24+1)},
        {"bookNum": "27",   "infix2": "27%3Asection%3D",   "suffs": range(1, 16+1)},
        {"bookNum": "28",   "infix2": "28%3Asection%3D",   "suffs": range(1, 17+1)},
        {"bookNum": "29",   "infix2": "29%3Asection%3D",   "suffs": range(1, 14+1)},
        {"bookNum": "30",   "infix2": "30%3Asection%3D",   "suffs": range(1, 35+1)},
        {"bookNum": "31",   "infix2": "31%3Asection%3D",   "suffs": range(1, 34+1)},
        {"bookNum": "32",   "infix2": "32%3Asection%3D",   "suffs": range(1, 29+1)},
        {"bookNum": "33",   "infix2": "33%3Asection%3D",   "suffs": range(1, 9+1)},
        {"bookNum": "34",   "infix2": "34%3Asection%3D",   "suffs": range(1, 11+1)},
    ]
}))
authors.append(lysias)

moschus = utils.Author("Moschus")
moschus.addWork(utils.TextSpec("Eros Drapeta", "2008.01.0648", 1, "%3Apoem%3D", {
    "multi": False,
    "suffixes": [1]
}))
moschus.addWork(utils.TextSpec("Europa", "2008.01.0644", 1, "%3Apoem%3D", {
    "multi": False,
    "suffixes": [2]
}))
moschus.addWork(utils.TextSpec("Fragmenta", "2008.01.0646", 1, "%3Apoem%3D", {
    "multi": False,
    "suffixes": range(4, 7+1)
}))
# Included with Moschus but possibly not his works
moschus.addWork(utils.TextSpec("Epitaphius Bios", "2008.01.0647", 1, "%3Apoem%3D", {
    "multi": False,
    "suffixes": [3]
}))
moschus.addWork(utils.TextSpec("Megara", "2008.01.0645", 1, "%3Apoem%3D", {
    "multi": False,
    "suffixes": [4]
}))
authors.append(moschus)

bible = utils.Author("Bible")
bible.addWork(utils.TextSpec("Bible", "1999.01.0155", 27, "%3Abook%3D", {
    "multi": True,
    "suffixes": [
        {"bookNum": "Matthew",    "infix2": "Matthew%3Achapter%3D",    "suffs": range(1, 28+1)},
        {"bookNum": "Mark",    "infix2": "Mark%3Achapter%3D",    "suffs": range(1, 16+1)},
        {"bookNum": "Luke",    "infix2": "Luke%3Achapter%3D",    "suffs": range(1, 24+1)},
        {"bookNum": "John",    "infix2": "John%3Achapter%3D",    "suffs": range(1, 21+1)},
        {"bookNum": "Acts",    "infix2": "Acts%3Achapter%3D",    "suffs": range(1, 28+1)},
        {"bookNum": "James",    "infix2": "James%3Achapter%3D",    "suffs": range(1, 5+1)},
        {"bookNum": "1 Peter",    "infix2": "I+Peter%3Achapter%3D",    "suffs": range(1, 5+1)},
        {"bookNum": "2 Peter",    "infix2": "II+Peter%3Achapter%3D",    "suffs": range(1, 3+1)},
        {"bookNum": "1 John",    "infix2": "I+John%3Achapter%3D",    "suffs": range(1, 5+1)},
        {"bookNum": "2 John",    "infix2": "II+John%3Achapter%3D",    "suffs": range(1, 1+1)},
        {"bookNum": "3 John",    "infix2": "III+John%3Achapter%3D",    "suffs": range(1, 1+1)},
        {"bookNum": "Jude",    "infix2": "Jude%3Achapter%3D",    "suffs": range(1, 1+1)},
        {"bookNum": "Romans",    "infix2": "Romans%3Achapter%3D",    "suffs": range(1, 16+1)},
        {"bookNum": "1 Corinthians",    "infix2": "I+Corinthians%3Achapter%3D",    "suffs": range(1, 16+1)},
        {"bookNum": "2 Corinthians",    "infix2": "II+Corinthians%3Achapter%3D",    "suffs": range(1, 13+1)},
        {"bookNum": "Galatians",    "infix2": "Galatians%3Achapter%3D",    "suffs": range(1, 6+1)},
        {"bookNum": "Ephesians",    "infix2": "Ephesians%3Achapter%3D",    "suffs": range(1, 6+1)},
        {"bookNum": "Philippians",    "infix2": "Philippians%3Achapter%3D",    "suffs": range(1, 4+1)},
        {"bookNum": "Colossians",    "infix2": "Colossians%3Achapter%3D",    "suffs": range(1, 4+1)},
        {"bookNum": "1 Thessalonians",    "infix2": "I+Thessalonians%3Achapter%3D",    "suffs": range(1, 5+1)},
        {"bookNum": "2 Thessalonians",    "infix2": "II+Thessalonians%3Achapter%3D",    "suffs": range(1, 3+1)},
        {"bookNum": "Hebrews",    "infix2": "Hebrews%3Achapter%3D",    "suffs": range(1, 13+1)},
        {"bookNum": "1 Timothy",    "infix2": "I+Timothy%3Achapter%3D",    "suffs": range(1, 6+1)},
        {"bookNum": "2 Timothy",    "infix2": "II+Timothy%3Achapter%3D",    "suffs": range(1, 4+1)},
        {"bookNum": "Titus",    "infix2": "Titus%3Achapter%3D",    "suffs": range(1, 3+1)},
        {"bookNum": "Philemon",    "infix2": "Philemon%3Achapter%3D",    "suffs": range(1, 1+1)},
        {"bookNum": "Revelation",    "infix2": "Revelation%3Achapter%3D",    "suffs": range(1, 22+1)},
    ]
}))
authors.append(bible)

nonnus = utils.Author("Nonnus")
nonnus.addWork(utils.TextSpec("Dionysiaca", "2008.01.0485", 48, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(nonnus)

onasander = utils.Author("Onasander")
onasander.addWork(utils.TextSpec("Strategicus", "2008.01.0634", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 42+1)
}))
authors.append(onasander)

oppianOfApamea = utils.Author("OppianOfApamea")
oppianOfApamea.addWork(utils.TextSpec("Cynegetica", "2008.01.0489", 4, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(oppianOfApamea)

oppian = utils.Author("Oppian")
oppian.addWork(utils.TextSpec("Halieutica", "2008.01.0488", 5, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(oppian)

parthenius = utils.Author("Parthenius")
parthenius.addWork(utils.TextSpec("Narrationes Amatoriae", "2008.01.0643", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1,36+1)
}))
authors.append(parthenius)

pausanias = utils.Author("Pausanias")
pausanias.addWork(utils.TextSpec("Description of Greece", "1999.01.0159", 10, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(pausanias)

philostratus = utils.Author("PhilostratusTheAthenian")
philostratus.addWork(utils.TextSpec("De Gymnastica", "2008.01.0600", 1, "%3Asection%3D", {
    "multi": False,
    "suffixes": range(1, 58+1)
}))
philostratus.addWork(utils.TextSpec("Epistulae et Dialexeis", "2008.01.0599", 2, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
philostratus.addWork(utils.TextSpec("Heroicus", "2008.01.0597", 1, "%3Aolpage%3D", {
    "multi": False,
    "suffixes": range(660,753+1)
}))
philostratus.addWork(utils.TextSpec("Nero", "2008.01.0598", 1, "%3Aolpage%3D", {
    "multi": False,
    "suffixes": range(636, 643+1)
}))
philostratus.addWork(utils.TextSpec("Vita Apollonii", "2008.01.0595", 8, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
philostratus.addWork(utils.TextSpec("Vitae Sophistarum", "2008.01.0596", 2, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(philostratus)

philostratusMinor = utils.Author("PhilostratusMinor")
philostratusMinor.addWork(utils.TextSpec("Imagines", "2008.01.0602", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 17+1)
}))
authors.append(philostratusMinor)

philostratusMajor = utils.Author("PhilostratusTheLemnian")
philostratusMajor.addWork(utils.TextSpec("Imagines", "2008.01.0601", 2, "%3Abook%3D", {
    "multi": True,
    "suffixes": [
        {"bookNum": "1",    "infix2": "",    "suffs": ["1"]},
        {"bookNum": "2",    "infix2": "",    "suffs": ["pos%3D2"]}
    ]
}))
authors.append(philostratusMajor)

pindar = utils.Author("Pindar")
pindar.addWork(utils.TextSpec("Odes", "1999.01.0161", 4, "%3Abook%3D", {
    "multi": True,
    "suffixes": [
        {"bookNum": "Olympian",    "infix2": "O.%3Apoem%3D",    "suffs": range(1, 14+1)},
        {"bookNum": "Pythian",    "infix2": "P.%3Apoem%3D",    "suffs": range(1, 12+1)},
        {"bookNum": "Nemean",    "infix2": "N.%3Apoem%3D",    "suffs": range(1, 11+1)},
        {"bookNum": "Isthmean",    "infix2": "I.%3Apoem%3D",    "suffs": range(1, 8+1)},
    ]
}))
authors.append(pindar)

plato = utils.Author("Plato")
plato.addWork(utils.TextSpec("Alcibiades 1", "1999.01.0175", 1, "%3Atext%3DAlc.+1%3Asection%3D", {
    "multi": False,
    "suffixes": ["103a", "103b", "104a", "104b", "104c", "104d", "104e", "105a", "105b", "105c", "105d", "105e", "106a", "106b", "106c", "106d", "106e", "107a", "107b", "107c", "107d", "107e", "108a", "108b", "108c", "108d", "108e", "109a", "109b", "109c", "109d", "109e", "110a", "110b", "110c", "110d", "110e", "111a", "111b", "111c", "111d", "111e", "112a", "112b", "112c", "112d", "112e", "113a", "113b", "113c", "113d", "113e", "114a", "114b", "114c", "114d", "114e", "115a", "115b", "115c", "115d", "115e", "116a", "116b", "116c", "116d", "116e", "117a", "117b", "117c", "117d", "117e", "118a", "118b", "118c", "118d", "118e", "119a", "119b", "119c", "119d", "119e", "120a", "120b", "120c", "120d", "120e", "121a", "121b", "121c", "121d", "121e", "122a", "122b", "122c", "122d", "122e", "123a", "123b", "123c", "123d", "123e", "124a", "124b", "124c", "124d", "124e", "125a", "125b", "125c", "125d", "125e", "126a", "126b", "126c", "126d", "126e", "127a", "127b", "127c", "127d", "127e", "128a", "128b", "128c", "128d", "128e", "129a", "129b", "129c", "129d", "129e", "130a", "130b", "130c", "130d", "130e", "131a", "131b", "131c", "131d", "131e", "132a", "132b", "132c", "132d", "132e", "133a", "133b", "133c", "133d", "133e", "134a", "134b", "134c", "134d", "134e", "135a", "135b", "135c", "135d", "135e"]
}))
plato.addWork(utils.TextSpec("Alcibiades 2", "1999.01.0175", 1, "%3Atext%3DAlc.+2%3Asection%3D", {
    "multi": False,
    "suffixes": ["138a", "138b", "138c", "138d", "139a", "139b", "139c", "139d", "139e", "140a", "140b", "140c", "140d", "140e", "141a", "141b", "141c", "141d", "141e", "142a", "142b", "142c", "142d", "142e", "143a", "143b", "143c", "143d", "143e", "144a", "144b", "144c", "144d", "144e", "145a", "145b", "145c", "145d", "145e", "146a", "146b", "146c", "146d", "146e", "147a", "147b", "147c", "147d", "147e", "148a", "148b", "148c", "148d", "148e", "149a", "149b", "149c", "149d", "149e", "150a", "150b", "150c", "150d", "150e", "151a", "151b", "151c"]
}))
plato.addWork(utils.TextSpec("Hipparchus", "1999.01.0175", 1, "%3Atext%3DHipparch.%3Asection%3D", {
    "multi": False,
    "suffixes": ["225a", "225b", "225c", "225d", "226a", "226b", "226c", "226d", "226e", "227a", "227b", "227c", "227d", "227e", "228a", "228b", "228c", "228d", "228e", "229a", "229b", "229c", "229d", "229e", "230a", "230b", "230c", "230d", "230e", "231a", "231b", "231c", "231d", "231e", "232a", "232b", "232c"]
}))
plato.addWork(utils.TextSpec("Lovers", "1999.01.0175", 1, "%3Atext%3DLovers%3Asection%3D", {
    "multi": False,
    "suffixes": ["132a", "132b", "132c", "132d", "133a", "133b", "133c", "133d", "133e", "134a", "134b", "134c", "134d", "134e", "135a", "135b", "135c", "135d", "135e", "136a", "136b", "136c", "136d", "136e", "137a", "137b", "137c", "137d", "137e", "138a", "138b", "138c", "138d", "138e", "139a"]
}))
plato.addWork(utils.TextSpec("Theages", "1999.01.0175", 1, "%3Atext%3DTheag.%3Asection%3D", {
    "multi": False,
    "suffixes": ["121a", "121b", "121c", "121d", "122a", "122b", "122c", "122d", "122e", "123a", "123b", "123c", "123d", "123e", "124a", "124b", "124c", "124d", "124e", "125a", "125b", "125c", "125d", "125e", "126a", "126b", "126c", "126d", "126e", "127a", "127b", "127c", "127d", "127e", "128a", "128b", "128c", "128d", "128e", "129a", "129b", "129c", "129d", "129e", "130a", "130b", "130c", "130d", "130e", "131a"]
}))
plato.addWork(utils.TextSpec("Charmides", "1999.01.0175", 1, "%3Atext%3DCharm.%3Asection%3D", {
    "multi": False,
    "suffixes": ["153a", "153b", "153c", "153d", "154a", "154b", "154c", "154d", "154e", "155a", "155b", "155c", "155d", "155e", "156a", "156b", "156c", "156d", "156e", "157a", "157b", "157c", "157d", "157e", "158a", "158b", "158c", "158d", "158e", "159a", "159b", "159c", "159d", "159e", "160a", "160b", "160c", "160d", "160e", "161a", "161b", "161c", "161d", "161e", "162a", "162b", "162c", "162d", "162e", "163a", "163b", "163c", "163d", "163e", "164a", "164b", "164c", "164d", "164e", "165a", "165b", "165c", "165d", "165e", "166a", "166b", "166c", "166d", "166e", "167a", "167b", "167c", "167d", "167e", "168a", "168b", "168c", "168d", "168e", "169a", "169b", "169c", "169d", "169e", "170a", "170b", "170c", "170d", "170e", "171a", "171b", "171c", "171d", "171e", "172a", "172b", "172c", "172d", "172e", "173a", "173b", "173c", "173d", "173e", "174a", "174b", "174c", "174d", "174e", "175a", "175b", "175c", "175d", "175e", "176a", "176b", "176c", "176d"]
}))
plato.addWork(utils.TextSpec("Laches", "1999.01.0175", 1, "%3Atext%3DLach.%3Asection%3D", {
    "multi": False,
    "suffixes": ["178a", "178b", "179a", "179b", "179c", "179d", "179e", "180a", "180b", "180c", "180d", "180e", "181a", "181b", "181c", "181d", "181e", "182a", "182b", "182c", "182d", "182e", "183a", "183b", "183c", "183d", "183e", "184a", "184b", "184c", "184d", "184e", "185a", "185b", "185c", "185d", "185e", "186a", "186b", "186c", "186d", "186e", "187a", "187b", "187c", "187d", "187e", "188a", "188b", "188c", "188d", "188e", "189a", "189b", "189c", "189d", "189e", "190a", "190b", "190c", "190d", "190e", "191a", "191b", "191c", "191d", "191e", "192a", "192b", "192c", "192d", "192e", "193a", "193b", "193c", "193d", "193e", "194a", "194b", "194c", "194d", "194e", "195a", "195b", "195c", "195d", "195e", "196a", "196b", "196c", "196d", "196e", "197a", "197b", "197c", "197d", "197e", "198a", "198b", "198c", "198d", "198e", "199a", "199b", "199c", "199d", "199e", "200a", "200b", "200c", "200d", "200e", "201a", "201b", "201c"]
}))
plato.addWork(utils.TextSpec("Lysis", "1999.01.0175", 1, "%3Atext%3DLysis%3Asection%3D", {
    "multi": False,
    "suffixes": ["203a", "203b", "204a", "204b", "204c", "204d", "204e", "205a", "205b", "205c", "205d", "205e", "206a", "206b", "206c", "206d", "206e", "207a", "207b", "207c", "207d", "207e", "208a", "208b", "208c", "208d", "208e", "209a", "209b", "209c", "209d", "209e", "210a", "210b", "210c", "210d", "210e", "211a", "211b", "211c", "211d", "211e", "212a", "212b", "212c", "212d", "212e", "213a", "213b", "213c", "213d", "213e", "214a", "214b", "214c", "214d", "214e", "215a", "215b", "215c", "215d", "215e", "216a", "216b", "216c", "216d", "216e", "217a", "217b", "217c", "217d", "217e", "218a", "218b", "218c", "218d", "218e", "219a", "219b", "219c", "219d", "219e", "220a", "220b", "220c", "220d", "220e", "221a", "221b", "221c", "221d", "221e", "222a", "222b", "222c", "222d", "222e", "223a", "223b"]
}))
plato.addWork(utils.TextSpec("Cratylus", "1999.01.0171", 1, "%3Atext%3DCrat.%3Asection%3D", {
    "multi": False,
    "suffixes": ["383a", "383b", "384a", "384b", "384c", "384d", "384e", "385a", "385b", "385c", "385d", "385e", "386a", "386b", "386c", "386d", "386e", "387a", "387b", "387c", "387d", "387e", "388a", "388b", "388c", "388d", "388e", "389a", "389b", "389c", "389d", "389e", "390a", "390b", "390c", "390d", "390e", "391a", "391b", "391c", "391d", "391e", "392a", "392b", "392c", "392d", "392e", "393a", "393b", "393c", "393d", "393e", "394a", "394b", "394c", "394d", "394e", "395a", "395b", "395c", "395d", "395e", "396a", "396b", "396c", "396d", "396e", "397a", "397b", "397c", "397d", "397e", "398a", "398b", "398c", "398d", "398e", "399a", "399b", "399c", "399d", "399e", "400a", "400b", "400c", "400d", "400e", "401a", "401b", "401c", "401d", "401e", "402a", "402b", "402c", "402d", "402e", "403a", "403b", "403c", "403d", "403e", "404a", "404b", "404c", "404d", "404e", "405a", "405b", "405c", "405d", "405e", "406a", "406b", "406c", "406d", "406e", "407a", "407b", "407c", "407d", "407e", "408a", "408b", "408c", "408d", "408e", "409a", "409b", "409c", "409d", "409e", "410a", "410b", "410c", "410d", "410e", "411a", "411b", "411c", "411d", "411e", "412a", "412b", "412c", "412d", "412e", "413a", "413b", "413c", "413d", "413e", "414a", "414b", "414c", "414d", "414e", "415a", "415b", "415c", "415d", "415e", "416a", "416b", "416c", "416d", "416e", "417a", "417b", "417c", "417d", "417e", "418a", "418b", "418c", "418d", "418e", "419a", "419b", "419c", "419d", "419e", "420a", "420b", "420c", "420d", "420e", "421a", "421b", "421c", "421d", "421e", "422a", "422b", "422c", "422d", "422e", "423a", "423b", "423c", "423d", "423e", "424a", "424b", "424c", "424d", "424e", "425a", "425b", "425c", "425d", "425e", "426a", "426b", "426c", "426d", "426e", "427a", "427b", "427c", "427d", "427e", "428a", "428b", "428c", "428d", "428e", "429a", "429b", "429c", "429d", "429e", "430a", "430b", "430c", "430d", "430e", "431a", "431b", "431c", "431d", "431e", "432a", "432b", "432c", "432d", "432e", "433a", "433b", "433c", "433d", "433e", "434a", "434b", "434c", "434d", "434e", "435a", "435b", "435c", "435d", "435e", "436a", "436b", "436c", "436d", "436e", "437a", "437b", "437c", "437d", "438a", "438b", "438c", "438d", "438e", "439a", "439b", "439c", "439d", "439e", "440a", "440b", "440c", "440d", "440e"]
}))
plato.addWork(utils.TextSpec("Theaetetus", "1999.01.0171", 1, "%3Atext%3DTheaet.%3Asection%3D", {
    "multi": False,
    "suffixes": ["142a", "142b", "142c", "142d", "143a", "143b", "143c", "143d", "143e", "144a", "144b", "144c", "144d", "144e", "145a", "145b", "145c", "145d", "145e", "146a", "146b", "146c", "146d", "146e", "147a", "147b", "147c", "147d", "147e", "148a", "148b", "148c", "148d", "148e", "149a", "149b", "149c", "149d", "149e", "150a", "150b", "150c", "150d", "150e", "151a", "151b", "151c", "151d", "151e", "152a", "152b", "152c", "152d", "152e", "153a", "153b", "153c", "153d", "153e", "154a", "154b", "154c", "154d", "154e", "155a", "155b", "155c", "155d", "155e", "156a", "156b", "156c", "156d", "156e", "157a", "157b", "157c", "157d", "157e", "158a", "158b", "158c", "158d", "158e", "159a", "159b", "159c", "159d", "159e", "160a", "160b", "160c", "160d", "160e", "161a", "161b", "161c", "161d", "161e", "162a", "162b", "162c", "162d", "162e", "163a", "163b", "163c", "163d", "163e", "164a", "164b", "164c", "164d", "164e", "165a", "165b", "165c", "165d", "165e", "166a", "166b", "166c", "166d", "166e", "167a", "167b", "167c", "167d", "167e", "168a", "168b", "168c", "168d", "168e", "169a", "169b", "169c", "169d", "169e", "170a", "170b", "170c", "170d", "170e", "171a", "171b", "171c", "171d", "171e", "172a", "172b", "172c", "172d", "172e", "173a", "173b", "173c", "173d", "173e", "174a", "174b", "174c", "174d", "174e", "175a", "175b", "175c", "175d", "175e", "176a", "176b", "176c", "176d", "176e", "177a", "177b", "177c", "177d", "177e", "178a", "178b", "178c", "178d", "178e", "179a", "179b", "179c", "179d", "179e", "180a", "180b", "180c", "180d", "180e", "181a", "181b", "181c", "181d", "181e", "182a", "182b", "182c", "182d", "182e", "183a", "183b", "183c", "183d", "183e", "184a", "184b", "184c", "184d", "184e", "185a", "185b", "185c", "185d", "185e", "186a", "186b", "186c", "186d", "186e", "187a", "187b", "187c", "187d", "187e", "188a", "188b", "188c", "188d", "188e", "189a", "189b", "189c", "189d", "189e", "190a", "190b", "190c", "190d", "190e", "191a", "191b", "191c", "191d", "191e", "192a", "192b", "192c", "192d", "192e", "193a", "193b", "193c", "193d", "193e", "194a", "194b", "194c", "194d", "194e", "195a", "195b", "195c", "195d", "195e", "196a", "196b", "196c", "196d", "196e", "197a", "197b", "197c", "197d", "197e", "198a", "198b", "198c", "198d", "198e", "199a", "199b", "199c", "199d", "199e", "200a", "200b", "200c", "200d", "200e", "201a", "201b", "201c", "201d", "201e", "202a", "202b", "202c", "202d", "202e", "203a", "203b", "203c", "203d", "203e", "204a", "204b", "204c", "204d", "204e", "205a", "205b", "205c", "205d", "205e", "206a", "206b", "206c", "206d", "206e", "207a", "207b", "207c", "207d", "207e", "208a", "208b", "208c", "208d", "208e", "209a", "209b", "209c", "209d", "209e", "210a", "210b", "210c", "210d"]
}))
plato.addWork(utils.TextSpec("Sophist", "1999.01.0171", 1, "%3Atext%3DSoph.%3Asection%3D", {
    "multi": False,
    "suffixes": ["216a", "216b", "216c", "216d", "217a", "217b", "217c", "217d", "217e", "218a", "218b", "218c", "218d", "218e", "219a", "219b", "219c", "219d", "219e", "220a", "220b", "220c", "220d", "220e", "221a", "221b", "221c", "221d", "221e", "222a", "222b", "222c", "222d", "222e", "223a", "223b", "223c", "223d", "223e", "224a", "224b", "224c", "224d", "224e", "225a", "225b", "225c", "225d", "225e", "226a", "226b", "226c", "226d", "226e", "227a", "227b", "227c", "227d", "228a", "228b", "228c", "228d", "228e", "229a", "229b", "229c", "229d", "229e", "230a", "230b", "230c", "230d", "230e", "231a", "231b", "231c", "231d", "231e", "232a", "232b", "232c", "232d", "232e", "233a", "233b", "233c", "233d", "233e", "234a", "234b", "234c", "234d", "234e", "235a", "235b", "235c", "235d", "235e", "236a", "236b", "236c", "236d", "236e", "237a", "237b", "237c", "237d", "237e", "238a", "238b", "238c", "238d", "238e", "239a", "239b", "239c", "239d", "239e", "240a", "240b", "240c", "240d", "240e", "241a", "241b", "241c", "241d", "241e", "242a", "242b", "242c", "242d", "242e", "243a", "243b", "243c", "243d", "243e", "244a", "244b", "244c", "244d", "244e", "245a", "245b", "245c", "245d", "245e", "246a", "246b", "246c", "246d", "246e", "247a", "247b", "247c", "247d", "247e", "248a", "248b", "248c", "248d", "248e", "249a", "249b", "249c", "249d", "249e", "250a", "250b", "250c", "250d", "250e", "251a", "251b", "251c", "251d", "251e", "252a", "252b", "252c", "252d", "252e", "253a", "253b", "253c", "253d", "253e", "254a", "254b", "254c", "254d", "254e", "255a", "255b", "255c", "255d", "255e", "256a", "256b", "256c", "256d", "256e", "257a", "257b", "257c", "257d", "257e", "258a", "258b", "258c", "258d", "258e", "259a", "259b", "259c", "259d", "259e", "260a", "260b", "260c", "260d", "260e", "261a", "261b", "261c", "261d", "261e", "262a", "262b", "262c", "262d", "262e", "263a", "263b", "263c", "263d", "263e", "264a", "264b", "264c", "264d", "264e", "265a", "265b", "265c", "265d", "265e", "266a", "266b", "266c", "266d", "266e", "267a", "267b", "267c", "267d", "267e", "268a", "268b", "268c", "268d"]
}))
plato.addWork(utils.TextSpec("Statesman", "1999.01.0171", 1, "%3Atext%3DStat.%3Asection%3D", {
    "multi": False,
    "suffixes": ["257a", "257b", "257c", "257d", "258a", "258b", "258c", "258d", "258e", "259a", "259b", "259c", "259d", "259e", "260a", "260b", "260c", "260d", "260e", "261a", "261b", "261c", "261d", "261e", "262a", "262b", "262c", "262d", "262e", "263a", "263b", "263c", "263d", "263e", "264a", "264b", "264c", "264d", "264e", "265a", "265b", "265c", "265d", "265e", "266a", "266b", "266c", "266d", "266e", "267a", "267b", "267c", "267d", "267e", "268a", "268b", "268c", "268d", "268e", "269a", "269b", "269c", "269d", "269e", "270a", "270b", "270c", "270d", "270e", "271a", "271b", "271c", "271d", "271e", "272a", "272b", "272c", "272d", "272e", "273a", "273b", "273c", "273d", "273e", "274a", "274b", "274c", "274d", "274e", "275a", "275b", "275c", "275d", "275e", "276a", "276b", "276c", "276d", "276e", "277a", "277b", "277c", "277d", "277e", "278a", "278b", "278c", "278d", "278e", "279a", "279b", "279c", "279d", "279e", "280a", "280b", "280c", "280d", "280e", "281a", "281b", "281c", "281d", "281e", "282a", "282b", "282c", "282d", "282e", "283a", "283b", "283c", "283d", "283e", "284a", "284b", "284c", "284d", "284e", "285a", "285b", "285c", "285d", "285e", "286a", "286b", "286c", "286d", "286e", "287a", "287b", "287c", "287d", "287e", "288a", "288b", "288c", "288d", "288e", "289a", "289b", "289c", "289d", "289e", "290a", "290b", "290c", "290d", "290e", "291a", "291b", "291c", "291d", "291e", "292a", "292b", "292c", "292d", "292e", "293a", "293b", "293c", "293d", "293e", "294a", "294b", "294c", "294d", "294e", "295a", "295b", "295c", "295d", "295e", "296a", "296b", "296c", "296d", "296e", "297a", "297b", "297c", "297d", "297e", "298a", "298b", "298c", "298d", "298e", "299a", "299b", "299c", "299d", "299e", "300a", "300b", "300c", "300d", "300e", "301a", "301b", "301c", "301d", "301e", "302a", "302b", "302c", "302d", "302e", "303a", "303b", "303c", "303d", "303e", "304a", "304b", "304c", "304d", "304e", "305a", "305b", "305c", "305d", "305e", "306a", "306b", "306c", "306d", "306e", "307a", "307b", "307c", "307d", "307e", "308a", "308b", "308c", "308d", "308e", "309a", "309b", "309c", "309d", "309e", "310a", "310b", "310c", "310d", "310e", "311a", "311b", "311c"]
}))
plato.addWork(utils.TextSpec("Epistles", "1999.01.0163", 1, "%3Aletter%3D", {
    "multi": False,
    "suffixes": range(1, 13+1)
}))
plato.addWork(utils.TextSpec("Euthydemus", "1999.01.0177", 1, "%3Atext%3DEuthyd.%3Asection%3D", {
    "multi": False,
    "suffixes": ["271a", "271b", "271c", "271d", "272a", "272b", "272c", "272d", "272e", "273a", "273b", "273c", "273d", "273e", "274a", "274b", "274c", "274d", "274e", "275a", "275b", "275c", "275d", "275e", "276a", "276b", "276c", "276d", "276e", "277a", "277b", "277c", "277d", "277e", "278a", "278b", "278c", "278d", "278e", "279a", "279b", "279c", "279d", "279e", "280a", "280b", "280c", "280d", "280e", "281a", "281b", "281c", "281d", "281e", "282a", "282b", "282c", "282d", "282e", "283a", "283b", "283c", "283d", "283e", "284a", "284b", "284c", "284d", "284e", "285a", "285b", "285c", "285d", "285e", "286a", "286b", "286c", "286d", "286e", "287a", "287b", "287c", "287d", "287e", "288a", "288b", "288c", "288d", "288e", "289a", "289b", "289c", "289d", "289e", "290a", "290b", "290c", "290d", "290e", "291a", "291b", "291c", "291d", "291e", "292a", "292b", "292c", "292d", "292e", "293a", "293b", "293c", "293d", "293e", "294a", "294b", "294c", "294d", "294e", "295a", "295b", "295c", "295d", "295e", "296a", "296b", "296c", "296d", "296e", "297a", "297b", "297c", "297d", "297e", "298a", "298b", "298c", "298d", "298e", "299a", "299b", "299c", "299d", "299e", "300a", "300b", "300c", "300d", "300e", "301a", "301b", "301c", "301d", "301e", "302a", "302b", "302c", "302d", "302e", "303a", "303b", "303c", "303d", "303e", "304a", "304b", "304c", "304d", "304e", "305a", "305b", "305c", "305d", "305e", "306a", "306b", "306c", "306d", "306e", "307a", "307b", "307c"]
}))
plato.addWork(utils.TextSpec("Protagoras", "1999.01.0177", 1, "%3Atext%3DProt.%3Asection%3D", {
    "multi": False,
    "suffixes": ["309a", "309b", "309c", "309d", "310a", "310b", "310c", "310d", "310e", "311a", "311b", "311c", "311d", "311e", "312a", "312b", "312c", "312d", "312e", "313a", "313b", "313c", "313d", "313e", "314a", "314b", "314c", "314d", "314e", "315a", "315b", "315c", "315d", "315e", "316a", "316b", "316c", "316d", "316e", "317a", "317b", "317c", "317d", "317e", "318a", "318b", "318c", "318d", "318e", "319a", "319b", "319c", "319d", "319e", "320a", "320b", "320c", "320d", "320e", "321a", "321b", "321c", "321d", "321e", "322a", "322b", "322c", "322d", "322e", "323a", "323b", "323c", "323d", "323e", "324a", "324b", "324c", "324d", "324e", "325a", "325b", "325c", "325d", "325e", "326a", "326b", "326c", "326d", "326e", "327a", "327b", "327c", "327d", "327e", "328a", "328b", "328c", "328d", "328e", "329a", "329b", "329c", "329d", "329e", "330a", "330b", "330c", "330d", "330e", "331a", "331b", "331c", "331d", "331e", "332a", "332b", "332c", "332d", "332e", "333a", "333b", "333c", "333d", "333e", "334a", "334b", "334c", "334d", "334e", "335a", "335b", "335c", "335d", "335e", "336a", "336b", "336c", "336d", "336e", "337a", "337b", "337c", "337d", "337e", "338a", "338b", "338c", "338d", "338e", "339a", "339b", "339c", "339d", "339e", "340a", "340b", "340c", "340d", "340e", "341a", "341b", "341c", "341d", "341e", "342a", "342b", "342c", "342d", "342e", "343a", "343b", "343c", "343d", "343e", "344a", "344b", "344c", "344d", "344e", "345a", "345b", "345c", "345d", "345e", "346a", "346b", "346c", "346d", "346e", "347a", "347b", "347c", "347d", "347e", "348a", "348b", "348c", "348d", "348e", "349a", "349b", "349c", "349d", "349e", "350a", "350b", "350c", "350d", "350e", "351a", "351b", "351c", "351d", "351e", "352a", "352b", "352c", "352d", "352e", "353a", "353b", "353c", "353d", "353e", "354a", "354b", "354c", "354d", "354e", "355a", "355b", "355c", "355d", "355e", "356a", "356b", "356c", "356d", "356e", "357a", "357b", "357c", "357d", "357e", "358a", "358b", "358c", "358d", "358e", "359a", "359b", "359c", "359d", "359e", "360a", "360b", "360c", "360d", "360e", "361a", "361b", "361c", "361d", "361e", "362a"]
}))
plato.addWork(utils.TextSpec("Gorgias", "1999.01.0177", 1, "%3Atext%3DGorg.%3Asection%3D", {
    "multi": False,
    "suffixes": ["447a", "447b", "447c", "447d", "448a", "448b", "448c", "448d", "448e", "449a", "449b", "449c", "449d", "449e", "450a", "450b", "450c", "450d", "450e", "451a", "451b", "451c", "451d", "451e", "452a", "452b", "452c", "452d", "452e", "453a", "453b", "453c", "453d", "453e", "454a", "454b", "454c", "454d", "454e", "455a", "455b", "455c", "455d", "455e", "456a", "456b", "456c", "456d", "456e", "457a", "457b", "457c", "457d", "457e", "458a", "458b", "458c", "458d", "458e", "459a", "459b", "459c", "459d", "459e", "460a", "460b", "460c", "460d", "460e", "461a", "461b", "461c", "461d", "461e", "462a", "462b", "462c", "462d", "462e", "463a", "463b", "463c", "463d", "463e", "464a", "464b", "464c", "464d", "464e", "465a", "465b", "465c", "465d", "465e", "466a", "466b", "466c", "466d", "466e", "467a", "467b", "467c", "467d", "467e", "468a", "468b", "468c", "468d", "468e", "469a", "469b", "469c", "469d", "469e", "470a", "470b", "470c", "470d", "470e", "471a", "471b", "471c", "471d", "471e", "472a", "472b", "472c", "472d", "472e", "473a", "473b", "473c", "473d", "473e", "474a", "474b", "474c", "474d", "474e", "475a", "475b", "475c", "475d", "475e", "476a", "476b", "476c", "476d", "476e", "477a", "477b", "477c", "477d", "477e", "478a", "478b", "478c", "478d", "478e", "479a", "479b", "479c", "479d", "479e", "480a", "480b", "480c", "480d", "480e", "481a", "481b", "481c", "481d", "481e", "482a", "482b", "482c", "482d", "482e", "483a", "483b", "483c", "483d", "483e", "484a", "484b", "484c", "484d", "484e", "485a", "485b", "485c", "485d", "485e", "486a", "486b", "486c", "486d", "486e", "487a", "487b", "487c", "487d", "487e", "488a", "488b", "488c", "488d", "488e", "489a", "489b", "489c", "489d", "489e", "490a", "490b", "490c", "490d", "490e", "491a", "491b", "491c", "491d", "491e", "492a", "492b", "492c", "492d", "492e", "493a", "493b", "493c", "493d", "493e", "494a", "494b", "494c", "494d", "494e", "495a", "495b", "495c", "495d", "495e", "496a", "496b", "496c", "496d", "496e", "497a", "497b", "497c", "497d", "497e", "498a", "498b", "498c", "498d", "498e", "499a", "499b", "499c", "499d", "499e", "500a", "500b", "500c", "500d", "500e", "501a", "501b", "501c", "501d", "501e", "502a", "502b", "502c", "502d", "502e", "503a", "503b", "503c", "503d", "503e", "504a", "504b", "504c", "504d", "504e", "505a", "505b", "505c", "505d", "505e", "506a", "506b", "506c", "506d", "506e", "507a", "507b", "507c", "507d", "507e", "508a", "508b", "508c", "508d", "508e", "509a", "509b", "509c", "509d", "509e", "510a", "510b", "510c", "510d", "510e", "511a", "511b", "511c", "511d", "511e", "512a", "512b", "512c", "512d", "512e", "513a", "513b", "513c", "513d", "513e", "514a", "514b", "514c", "514d", "514e", "515a", "515b", "515c", "515d", "515e", "516a", "516b", "516c", "516d", "516e", "517a", "517b", "517c", "517d", "517e", "518a", "518b", "518c", "518d", "518e", "519a", "519b", "519c", "519d", "519e", "520a", "520b", "520c", "520d", "520e", "521a", "521b", "521c", "521d", "521e", "522a", "522b", "522c", "522d", "522e", "523a", "523b", "523c", "523d", "523e", "524a", "524b", "524c", "524d", "524e", "525a", "525b", "525c", "525d", "525e", "526a", "526b", "526c", "526d", "526e", "527a", "527b", "527c", "527d", "527e"]
}))
plato.addWork(utils.TextSpec("Meno", "1999.01.0177", 1, "%3Atext%3DMeno%3Asection%3D", {
    "multi": False,
    "suffixes": ["70a", "70b", "70c", "71a", "71b", "71c", "71d", "71e", "72a", "72b", "72c", "72d", "72e", "73a", "73b", "73c", "73d", "73e", "74a", "74b", "74c", "74d", "74e", "75a", "75b", "75c", "75d", "75e", "76a", "76b", "76c", "76d", "76e", "77a", "77b", "77c", "77d", "77e", "78a", "78b", "78c", "78d", "78e", "79a", "79b", "79c", "79d", "79e", "80a", "80b", "80c", "80d", "80e", "81a", "81b", "81c", "81d", "81e", "82a", "82b", "82c", "82d", "82e", "83a", "83b", "83c", "83d", "83e", "84a", "84b", "84c", "84d", "84e", "85a", "85b", "85c", "85d", "85e", "86a", "86b", "86c", "86d", "86e", "87a", "87b", "87c", "87d", "87e", "88a", "88b", "88c", "88d", "88e", "89a", "89b", "89c", "89d", "89e", "90a", "90b", "90c", "90d", "90e", "91a", "91b", "91c", "91d", "91e", "92a", "92b", "92c", "92d", "92e", "93a", "93b", "93c", "93d", "93e", "94a", "94b", "94c", "94d", "94e", "95a", "95b", "95c", "95d", "95e", "96a", "96b", "96c", "96d", "96e", "97a", "97b", "97c", "97d", "97e", "98a", "98b", "98c", "98d", "98e", "99a", "99b", "99c", "99d", "99e", "100a", "100b", "100c"]
}))
plato.addWork(utils.TextSpec("Euthyphro", "1999.01.0169", 1, "%3Atext%3DEuthyph.%3Asection%3D", {
    "multi": False,
    "suffixes": ["2a", "2b", "2c", "2d", "3a", "3b", "3c", "3d", "3e", "4a", "4b", "4c", "4d", "4e", "5a", "5b", "5c", "5d", "5e", "6a", "6b", "6c", "6d", "6e", "7a", "7b", "7c", "7d", "7e", "8a", "8b", "8c", "8d", "8e", "9a", "9b", "9c", "9d", "9e", "10a", "10b", "10c", "10d", "10e", "11a", "11b", "11c", "11d", "11e", "12a", "12b", "12c", "12d", "12e", "13a", "13b", "13c", "13d", "13e", "14a", "14b", "14c", "14d", "14e", "15a", "15b", "15c", "15d", "15e", "16a"]
}))
plato.addWork(utils.TextSpec("Apology", "1999.01.0169", 1, "%3Atext%3DApol.%3Asection%3D", {
    "multi": False,
    "suffixes": ["17a", "17b", "17c", "17d", "18a", "18b", "18c", "18d", "18e", "19a", "19b", "19c", "19d", "19e", "20a", "20b", "20c", "20d", "20e", "21a", "21b", "21c", "21d", "21e", "22a", "22b", "22c", "22d", "22e", "23a", "23b", "23c", "23d", "23e", "24a", "24b", "24c", "24d", "24e", "25a", "25b", "25c", "25d", "25e", "26a", "26b", "26c", "26d", "26e", "27a", "27b", "27c", "27d", "27e", "28a", "28b", "28c", "28d", "28e", "29a", "29b", "29c", "29d", "29e", "30a", "30b", "30c", "30d", "30e", "31a", "31b", "31c", "31d", "31e", "32a", "32b", "32c", "32d", "32e", "33a", "33b", "33c", "33d", "33e", "34a", "34b", "34c", "34d", "34e", "35a", "35b", "35c", "35d", "35e", "36a", "36b", "36c", "36d", "36e", "37a", "37b", "37c", "37d", "37e", "38a", "38b", "38c", "38d", "38e", "39a", "39b", "39c", "39d", "39e", "40a", "40b", "40c", "40d", "40e", "41a", "41b", "41c", "41d", "41e", "42a"]
}))
plato.addWork(utils.TextSpec("Crito", "1999.01.0169", 1, "%3Atext%3DCrito%3Asection%3D", {
    "multi": False,
    "suffixes": ["43a", "43b", "43c", "43d", "44a", "44b", "44c", "44d", "44e", "45a", "45b", "45c", "45d", "45e", "46a", "46b", "46c", "46d", "46e", "47a", "47b", "47c", "47d", "47e", "48a", "48b", "48c", "48d", "48e", "49a", "49b", "49c", "49d", "49e", "50a", "50b", "50c", "50d", "50e", "51a", "51b", "51c", "51d", "51e", "52a", "52b", "52c", "52d", "52e", "53a", "53b", "53c", "53d", "53e", "54a", "54b", "54c", "54d", "54e"]
}))
plato.addWork(utils.TextSpec("Phaedo", "1999.01.0169", 1, "%3Atext%3DPhaedo%3Asection%3D", {
    "multi": False,
    "suffixes": ["57a", "57b", "58a", "58b", "58c", "58d", "58e", "59a", "59b", "59c", "59d", "59e", "60a", "60b", "60c", "60d", "60e", "61a", "61b", "61c", "61d", "61e", "62a", "62b", "62c", "62d", "62e", "63a", "63b", "63c", "63d", "63e", "64a", "64b", "64c", "64d", "64e", "65a", "65b", "65c", "65d", "65e", "66a", "66b", "66c", "66d", "66e", "67a", "67b", "67c", "67d", "67e", "68a", "68b", "68c", "68d", "68e", "69a", "69b", "69c", "69d", "69e", "70a", "70b", "70c", "70d", "70e", "71a", "71b", "71c", "71d", "71e", "72a", "72b", "72c", "72d", "72e", "73a", "73b", "73c", "73d", "73e", "74a", "74b", "74c", "74d", "74e", "75a", "75b", "75c", "75d", "75e", "76a", "76b", "76c", "76d", "76e", "77a", "77b", "77c", "77d", "77e", "78a", "78b", "78c", "78d", "78e", "79a", "79b", "79c", "79d", "79e", "80a", "80b", "80c", "80d", "80e", "81a", "81b", "81c", "81d", "81e", "82a", "82b", "82c", "82d", "82e", "83a", "83b", "83c", "83d", "83e", "84a", "84b", "84c", "84d", "84e", "85a", "85b", "85c", "85d", "85e", "86a", "86b", "86c", "86d", "86e", "87a", "87b", "87c", "87d", "87e", "88a", "88b", "88c", "88d", "88e", "89a", "89b", "89c", "89d", "89e", "90a", "90b", "90c", "90d", "90e", "91a", "91b", "91c", "91d", "91e", "92a", "92b", "92c", "92d", "92e", "93a", "93b", "93c", "93d", "93e", "94a", "94b", "94c", "94d", "94e", "95a", "95b", "95c", "95d", "95e", "96a", "96b", "96c", "96d", "96e", "97a", "97b", "97c", "97d", "97e", "98a", "98b", "98c", "98d", "98e", "99a", "99b", "99c", "99d", "99e", "100a", "100b", "100c", "100d", "100e", "101a", "101b", "101c", "101d", "101e", "102a", "102b", "102c", "102d", "102e", "103a", "103b", "103c", "103d", "103e", "104a", "104b", "104c", "104d", "104e", "105a", "105b", "105c", "105d", "105e", "106a", "106b", "106c", "106d", "106e", "107a", "107b", "107c", "107d", "107e", "108a", "108b", "108c", "108d", "108e", "109a", "109b", "109c", "109d", "109e", "110a", "110b", "110c", "110d", "110e", "111a", "111b", "111c", "111d", "111e", "112a", "112b", "112c", "112d", "112e", "113a", "113b", "113c", "113d", "113e", "114a", "114b", "114c", "114d", "114e", "115a", "115b", "115c", "115d", "115e", "116a", "116b", "116c", "116d", "116e", "117a", "117b", "117c", "117d", "117e", "118a"]
}))
plato.addWork(utils.TextSpec("Greater Hippias", "1999.01.0179", 1, "%3Atext%3DHipp.+Maj.%3Asection%3D", {
    "multi": False,
    "suffixes": ["281a", "281b", "281c", "281d", "282a", "282b", "282c", "282d", "282e", "283a", "283b", "283c", "283d", "283e", "284a", "284b", "284c", "284d", "284e", "285a", "285b", "285c", "285d", "285e", "286a", "286b", "286c", "286d", "286e", "287a", "287b", "287c", "287d", "287e", "288a", "288b", "288c", "288d", "288e", "289a", "289b", "289c", "289d", "289e", "290a", "290b", "290c", "290d", "290e", "291a", "291b", "291c", "291d", "291e", "292a", "292b", "292c", "292d", "292e", "293a", "293b", "293c", "293d", "293e", "294a", "294b", "294c", "294d", "294e", "295a", "295b", "295c", "295d", "295e", "296a", "296b", "296c", "296d", "296e", "297a", "297b", "297c", "297d", "297e", "298a", "298b", "298c", "298d", "298e", "299a", "299b", "299c", "299d", "299e", "300a", "300b", "300c", "300d", "300e", "301a", "301b", "301c", "301d", "301e", "302a", "302b", "302c", "302d", "302e", "303a", "303b", "303c", "303d", "303e", "304a", "304b", "304c", "304d", "304e"]
}))
plato.addWork(utils.TextSpec("Lesser Hippias", "1999.01.0179", 1, "%3Atext%3DHipp.+Min.%3Asection%3D", {
    "multi": False,
    "suffixes": ["363a", "363b", "363c", "363d", "364a", "364b", "364c", "364d", "364e", "365a", "365b", "365c", "365d", "365e", "366a", "366b", "366c", "366d", "366e", "367a", "367b", "367c", "367d", "367e", "368a", "368b", "368c", "368d", "368e", "369a", "369b", "369c", "369d", "369e", "370a", "370b", "370c", "370d", "370e", "371a", "371b", "371c", "371d", "371e", "372a", "372b", "372c", "372d", "372e", "373a", "373b", "373c", "373d", "373e", "374a", "374b", "374c", "374d", "374e", "375a", "375b", "375c", "375d", "375e", "376a", "376b", "376c"]
}))
plato.addWork(utils.TextSpec("Ion", "1999.01.0179", 1, "%3Atext%3DIon%3Asection%3D", {
    "multi": False,
    "suffixes": ["530a", "530b", "530c", "530d", "531a", "531b", "531c", "531d", "531e", "532a", "532b", "532c", "532d", "532e", "533a", "533b", "533c", "533d", "533e", "534a", "534b", "534c", "534d", "534e", "535a", "535b", "535c", "535d", "535e", "536a", "536b", "536c", "536d", "536e", "537a", "537b", "537d", "537e", "538a", "538b", "538c", "538d", "538e", "539a", "539b", "539c", "539d", "539e", "540a", "540b", "540c", "540d", "540e", "541a", "541b", "541c", "541d", "541e", "542a", "542b"]
}))
plato.addWork(utils.TextSpec("Menexenus", "1999.01.0179", 1, "%3Atext%3DMenex.%3Asection%3D", {
    "multi": False,
    "suffixes": ["234a", "234b", "234c", "235a", "235b", "235c", "235d", "235e", "236a", "236b", "236c", "236d", "236e", "237a", "237b", "237c", "237d", "237e", "238a", "238b", "238c", "238d", "238e", "239a", "239b", "239c", "239d", "239e", "240a", "240b", "240c", "240d", "240e", "241a", "241b", "241c", "241d", "241e", "242a", "242b", "242c", "242d", "242e", "243a", "243b", "243c", "243d", "243e", "244a", "244b", "244c", "244d", "244e", "245a", "245b", "245c", "245d", "245e", "246a", "246b", "246c", "246d", "246e", "247a", "247b", "247c", "247d", "247e", "248a", "248b", "248c", "248d", "248e", "249a", "249b", "249c", "249d", "249e"]
}))
plato.addWork(utils.TextSpec("Cleitophon", "1999.01.0179", 1, "%3Atext%3DCleit.%3Asection%3D", {
    "multi": False,
    "suffixes": ["406a", "407a", "407b", "407c", "407d", "407e", "408a", "408b", "408c", "408d", "408e", "409a", "409b", "409c", "409d", "409e", "410a", "410b", "410c", "410d", "410e"]
}))
plato.addWork(utils.TextSpec("Timaeus", "1999.01.0179", 1, "%3Atext%3DTim.%3Asection%3D", {
    "multi": False,
    "suffixes": ["17a", "17b", "17c", "17d", "18a", "18b", "18c", "18d", "18e", "19a", "19b", "19c", "19d", "19e", "20a", "20b", "20c", "20d", "20e", "21a", "21b", "21c", "21d", "21e", "22a", "22b", "22c", "22d", "22e", "23a", "23b", "23c", "23d", "23e", "24a", "24b", "24c", "24d", "24e", "25a", "25b", "25c", "25d", "25e", "26a", "26b", "26c", "26d", "26e", "27a", "27b", "27c", "27d", "28a", "28b", "28c", "29a", "29b", "29c", "29d", "29e", "30a", "30b", "30c", "30d", "31a", "31b", "31c", "32a", "32b", "32c", "32d", "33a", "33b", "33c", "33d", "34a", "34b", "34c", "35a", "35b", "35c", "36a", "36b", "36c", "36d", "36e", "37a", "37b", "37c", "37d", "37e", "38a", "38b", "38c", "38d", "38e", "39a", "39b", "39c", "39d", "39e", "40a", "40b", "40c", "40d", "40e", "41a", "41b", "41c", "41d", "41e", "42a", "42b", "42c", "42d", "42e", "43a", "43b", "43c", "43d", "43e", "44a", "44b", "44c", "44d", "44e", "45a", "45b", "45c", "45d", "45e", "46a", "46b", "46c", "46d", "46e", "47a", "47b", "47c", "47d", "47e", "48a", "48b", "48c", "48d", "48e", "49a", "49b", "49c", "49d", "49e", "50a", "50b", "50c", "50d", "50e", "51a", "51b", "51c", "51d", "51e", "52a", "52b", "52c", "52d", "52e", "53a", "53b", "53c", "53d", "53e", "54a", "54b", "54c", "54d", "54e", "55a", "55b", "55c", "55d", "55e", "56a", "56b", "56c", "56d", "56e", "57a", "57b", "57c", "57d", "57e", "58a", "58b", "58c", "58d", "58e", "59a", "59b", "59c", "59d", "59e", "60a", "60b", "60c", "60d", "60e", "61a", "61b", "61c", "61d", "61e", "62a", "62b", "62c", "62d", "63a", "63b", "63c", "63d", "63e", "64a", "64b", "64c", "64d", "64e", "65a", "65b", "65c", "65d", "65e", "66a", "66b", "66c", "66d", "66e", "67a", "67b", "67c", "67d", "67e", "68a", "68b", "68c", "68d", "68e", "69a", "69b", "69c", "69d", "69e", "70a", "70b", "70c", "70d", "70e", "71a", "71b", "71c", "71d", "71e", "72a", "72b", "72c", "72d", "72e", "73a", "73b", "73c", "73d", "73e", "74a", "74b", "74c", "74d", "74e", "75a", "75b", "75c", "75d", "75e", "76a", "76b", "76c", "76d", "76e", "77a", "77b", "77c", "77d", "77e", "78a", "78b", "78c", "78d", "78e", "79a", "79b", "79c", "79d", "79e", "80a", "80b", "80c", "80d", "80e", "81a", "81b", "81c", "81d", "81e", "82a", "82b", "82c", "82d", "82e", "83a", "83b", "83c", "83d", "83e", "84a", "84b", "84c", "84d", "84e", "85a", "85b", "85c", "85d", "85e", "86a", "86b", "86c", "86d", "86e", "87a", "87b", "87c", "87d", "87e", "88a", "88b", "88c", "88d", "88e", "89a", "89b", "89c", "89d", "89e", "90a", "90b", "90c", "90d", "90e", "91a", "91b", "91c", "91d", "91e", "92a", "92b", "92c"]
}))
plato.addWork(utils.TextSpec("Critias", "1999.01.0179", 1, "%3Atext%3DCriti.%3Asection%3D", {
    "multi": False,
    "suffixes": ["106a", "106b", "106c", "107a", "107b", "107c", "107d", "107e", "108a", "108b", "108c", "108d", "108e", "109a", "109b", "109c", "109d", "109e", "110a", "110b", "110c", "110d", "110e", "111a", "111b", "111c", "111d", "111e", "112a", "112b", "112c", "112d", "112e", "113a", "113b", "113c", "113d", "113e", "114a", "114b", "114c", "114d", "114e", "115a", "115b", "115c", "115d", "115e", "116a", "116b", "116c", "116d", "116e", "117a", "117b", "117c", "117d", "117e", "118a", "118b", "118c", "118d", "118e", "119a", "119b", "119c", "119d", "119e", "120a", "120b", "120c", "120d", "120e", "121a", "121b", "121c"]
}))
plato.addWork(utils.TextSpec("Minos", "1999.01.0179", 1, "%3Atext%3DMinos%3Asection%3D", {
    "multi": False,
    "suffixes": ["313a", "313b", "313c", "314a", "314b", "314c", "314d", "314e", "315a", "315b", "315c", "315d", "315e", "316a", "316b", "316c", "316d", "316e", "317a", "317b", "317c", "317d", "317e", "318a", "318b", "318c", "318d", "318e", "319a", "319b", "319c", "319d", "319e", "320a", "320b", "320c", "320d", "320e", "321a", "321b", "321c", "321d"]
}))
plato.addWork(utils.TextSpec("Epinomis", "1999.01.0179", 1, "%3Atext%3DEpin.%3Asection%3D", {
    "multi": False,
    "suffixes": ["973a", "973b", "973c", "973d", "974a", "974b", "974c", "974d", "974e", "975a", "975b", "975c", "975d", "975e", "976a", "976b", "976c", "976d", "976e", "977a", "977b", "977c", "977d", "977e", "978a", "978b", "978c", "978d", "978e", "979a", "979b", "979c", "979d", "979e", "980a", "980b", "980c", "980d", "980e", "981a", "981b", "981c", "981d", "981e", "982a", "982b", "982c", "982d", "982e", "983a", "983b", "983c", "983d", "983e", "984a", "984b", "984c", "984d", "984e", "985a", "985b", "985c", "985d", "985e", "986a", "986b", "986c", "986d", "986e", "987a", "987b", "987c", "987d", "987e", "988a", "988b", "988c", "988d", "988e", "989a", "989b", "989c", "989d", "989e", "990a", "990b", "990c", "990d", "990e", "991a", "991b", "991c", "991d", "991e", "992a", "992b", "992c", "992d", "992e"]
}))
plato.addWork(utils.TextSpec("Laws", "1999.01.0165", 12, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
plato.addWork(utils.TextSpec("Parmenides", "1999.01.0173", 1, "%3Atext%3DParm.%3Asection%3D", {
    "multi": False,
    "suffixes": ["126a", "126b", "126c", "127a", "127b", "127c", "127d", "127e", "128a", "128b", "128c", "128d", "128e", "129a", "129b", "129c", "129d", "129e", "130a", "130b", "130c", "130d", "130e", "131a", "131b", "131c", "131d", "131e", "132a", "132b", "132c", "132d", "132e", "133a", "133b", "133c", "133d", "133e", "134a", "134b", "134c", "134d", "134e", "135a", "135b", "135c", "135d", "135e", "136a", "136b", "136c", "136d", "136e", "137a", "137b", "137c", "137d", "137e", "138a", "138b", "138c", "138d", "138e", "139a", "139b", "139c", "139d", "139e", "140a", "140b", "140c", "140d", "140e", "141a", "141b", "141c", "141d", "141e", "142a", "142b", "142c", "142d", "142e", "143a", "143b", "143c", "143d", "143e", "144a", "144b", "144c", "144d", "144e", "145a", "145b", "145c", "145d", "145e", "146a", "146b", "146c", "146d", "146e", "147a", "147b", "147c", "147d", "147e", "148a", "148b", "148c", "148d", "148e", "149a", "149b", "149c", "149d", "149e", "150a", "150b", "150c", "150d", "150e", "151a", "151b", "151c", "151d", "151e", "152a", "152b", "152c", "152d", "152e", "153a", "153b", "153c", "153d", "153e", "154a", "154b", "154c", "154d", "154e", "155a", "155b", "155c", "155d", "155e", "156a", "156b", "156c", "156d", "156e", "157a", "157b", "157c", "157d", "157e", "158a", "158b", "158c", "158d", "158e", "159a", "159b", "159c", "159d", "159e", "160a", "160b", "160c", "160d", "160e", "161a", "161b", "161c", "161d", "161e", "162a", "162b", "162c", "162d", "162e", "163a", "163b", "163c", "163d", "163e", "164a", "164b", "164c", "164d", "164e", "165a", "165b", "165c", "165d", "165e", "166a", "166b", "166c"]
}))
plato.addWork(utils.TextSpec("Philebus", "1999.01.0173", 1, "%3Atext%3DPhileb.%3Asection%3D", {
    "multi": False,
    "suffixes": ["11a", "11b", "11c", "11d", "11e", "12a", "12b", "12c", "12d", "12e", "13a", "13b", "13c", "13d", "13e", "14a", "14b", "14c", "14d", "14e", "15a", "15b", "15c", "15d", "15e", "16a", "16b", "16c", "16d", "16e", "17a", "17b", "17c", "17d", "17e", "18a", "18b", "18c", "18d", "18e", "19a", "19b", "19c", "19d", "19e", "20a", "20b", "20c", "20d", "20e", "21a", "21b", "21c", "21d", "21e", "22a", "22b", "22c", "22d", "22e", "23a", "23b", "23c", "23d", "23e", "24a", "24b", "24c", "24d", "24e", "25a", "25b", "25c", "25d", "25e", "26a", "26b", "26c", "26d", "26e", "27a", "27b", "27c", "27d", "27e", "28a", "28b", "28c", "28d", "28e", "29a", "29b", "29c", "29d", "29e", "30a", "30b", "30c", "30d", "30e", "31a", "31b", "31c", "31d", "31e", "32a", "32b", "32c", "32d", "32e", "33a", "33b", "33c", "33d", "33e", "34a", "34b", "34c", "34d", "34e", "35a", "35b", "35c", "35d", "35e", "36a", "36b", "36c", "36d", "36e", "37a", "37b", "37c", "37d", "37e", "38a", "38b", "38c", "38d", "38e", "39a", "39b", "39c", "39d", "39e", "40a", "40b", "40c", "40d", "40e", "41a", "41b", "41c", "41d", "41e", "42a", "42b", "42c", "42d", "42e", "43a", "43b", "43c", "43d", "43e", "44a", "44b", "44c", "44d", "44e", "45a", "45b", "45c", "45d", "45e", "46a", "46b", "46c", "46d", "46e", "47a", "47b", "47c", "47d", "47e", "48a", "48b", "48c", "48d", "48e", "49a", "49b", "49c", "49d", "49e", "50a", "50b", "50c", "50d", "50e", "51a", "51b", "51c", "51d", "51e", "52a", "52b", "52c", "52d", "52e", "53a", "53b", "53c", "53d", "53e", "54a", "54b", "54c", "54d", "54e", "55a", "55b", "55c", "55d", "55e", "56a", "56b", "56c", "56d", "56e", "57a", "57b", "57c", "57d", "57e", "58a", "58b", "58c", "58d", "58e", "59a", "59b", "59c", "59d", "59e", "60a", "60b", "60c", "60d", "60e", "61a", "61b", "61c", "61d", "61e", "62a", "62b", "62c", "62d", "62e", "63a", "63b", "63c", "63d", "63e", "64a", "64b", "64c", "64d", "64e", "65a", "65b", "65c", "65d", "65e", "66a", "66b", "66c", "66d", "66e", "67a", "67b"]
}))
plato.addWork(utils.TextSpec("Symposium", "1999.01.0173", 1, "%3Atext%3DSym.%3Asection%3D", {
    "multi": False,
    "suffixes": ["172a", "172b", "172c", "173a", "173b", "173c", "173d", "173e", "174a", "174b", "174c", "174d", "174e", "175a", "175b", "175c", "175d", "175e", "176a", "176b", "176c", "176d", "176e", "177a", "177b", "177c", "177d", "177e", "178a", "178b", "178c", "178d", "178e", "179a", "179b", "179c", "179d", "179e", "180a", "180b", "180c", "180d", "180e", "181a", "181b", "181c", "181d", "181e", "182a", "182b", "182c", "182d", "182e", "183a", "183b", "183c", "183d", "183e", "184a", "184b", "184c", "184d", "184e", "185a", "185b", "185c", "185d", "185e", "186a", "186b", "186c", "186d", "186e", "187a", "187b", "187c", "187d", "187e", "188a", "188b", "188c", "188d", "188e", "189a", "189b", "189c", "189d", "189e", "190a", "190b", "190c", "190d", "190e", "191a", "191b", "191c", "191d", "191e", "192a", "192b", "192c", "192d", "192e", "193a", "193b", "193c", "193d", "193e", "194a", "194b", "194c", "194d", "194e", "195a", "195b", "195c", "195d", "195e", "196a", "196b", "196c", "196d", "196e", "197a", "197b", "197c", "197d", "197e", "198a", "198b", "198c", "198d", "198e", "199a", "199b", "199c", "199d", "199e", "200a", "200b", "200c", "200d", "200e", "201a", "201b", "201c", "201d", "201e", "202a", "202b", "202c", "202d", "202e", "203a", "203b", "203c", "203d", "203e", "204a", "204b", "204c", "204d", "204e", "205a", "205b", "205c", "205d", "205e", "206a", "206b", "206c", "206d", "206e", "207a", "207b", "207c", "207d", "207e", "208a", "208b", "208c", "208d", "208e", "209a", "209b", "209c", "209d", "209e", "210a", "210b", "210c", "210d", "210e", "211a", "211b", "211c", "211d", "211e", "212a", "212b", "212c", "212d", "212e", "213a", "213b", "213c", "213d", "213e", "214a", "214b", "214c", "214d", "214e", "215a", "215b", "215c", "215d", "215e", "216a", "216b", "216c", "216d", "216e", "217a", "217b", "217c", "217d", "217e", "218a", "218b", "218c", "218d", "218e", "219a", "219b", "219c", "219d", "219e", "220a", "220b", "220c", "220d", "220e", "221a", "221b", "221c", "221d", "221e", "222a", "222b", "222c", "222d", "222e", "223a", "223b", "223c", "223d"]
}))
plato.addWork(utils.TextSpec("Phaedrus", "1999.01.0173", 1, "%3Atext%3DPhaedrus%3Asection%3D", {
    "multi": False,
    "suffixes": ["227a", "227b", "227c", "227d", "228a", "228b", "228c", "228d", "228e", "229a", "229b", "229c", "229d", "229e", "230a", "230b", "230c", "230d", "230e", "231a", "231b", "231c", "231d", "231e", "232a", "232b", "232c", "232d", "232e", "233a", "233b", "233c", "233d", "233e", "234a", "234b", "234c", "234d", "234e", "235a", "235b", "235c", "235d", "235e", "236a", "236b", "236c", "236d", "236e", "237a", "237b", "237c", "237d", "237e", "238a", "238b", "238c", "238d", "238e", "239a", "239b", "239c", "239d", "239e", "240a", "240b", "240c", "240d", "240e", "241a", "241b", "241c", "241d", "241e", "242a", "242b", "242c", "242d", "242e", "243a", "243b", "243c", "243d", "243e", "244a", "244b", "244c", "244d", "244e", "245a", "245b", "245c", "245d", "245e", "246a", "246b", "246c", "246d", "246e", "247a", "247b", "247c", "247d", "247e", "248a", "248b", "248c", "248d", "248e", "249a", "249b", "249c", "249d", "249e", "250a", "250b", "250c", "250d", "250e", "251a", "251b", "251c", "251d", "251e", "252a", "252b", "252c", "252d", "252e", "253a", "253b", "253c", "253d", "253e", "254a", "254b", "254c", "254d", "254e", "255a", "255b", "255c", "255d", "255e", "256a", "256b", "256c", "256d", "256e", "257a", "257b", "257c", "257d", "257e", "258a", "258b", "258c", "258d", "258e", "259a", "259b", "259c", "259d", "259e", "260a", "260b", "260c", "260d", "260e", "261a", "261b", "261c", "261d", "261e", "262a", "262b", "262c", "262d", "262e", "263a", "263b", "263c", "263d", "263e", "264a", "264b", "264c", "264d", "264e", "265a", "265b", "265c", "265d", "265e", "266a", "266b", "266c", "266d", "266e", "267a", "267b", "267c", "267d", "268a", "268b", "268c", "268d", "268e", "269a", "269b", "269c", "269d", "269e", "270a", "270b", "270c", "270d", "270e", "271a", "271b", "271c", "271d", "271e", "272a", "272b", "272c", "272d", "272e", "273a", "273b", "273c", "273d", "273e", "274a", "274b", "274c", "274d", "274e", "275a", "275b", "275c", "275d", "275e", "276a", "276b", "276c", "276d", "276e", "277a", "277b", "277c", "277d", "277e", "278a", "278b", "278c", "278d", "278e", "279a", "279b", "279c"]
}))
plato.addWork(utils.TextSpec("Republic", "1999.01.0167", 10, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(plato)

plutarch = utils.Author("Plutarch")
plutarch.addWork(utils.TextSpec("Ad principem ineruditum", "2008.01.0324", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["779d", "779e", "779f", "780a", "780b", "780c", "780d", "780e", "780f", "781a", "781b", "781c", "781d", "781e", "781f", "782a", "782b", "782c", "782d", "782e", "782f"]
}))
plutarch.addWork(utils.TextSpec("Adversus Colotem", "2008.01.0396", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["1107d", "1107e", "1107f", "1108a", "1108b", "1108c", "1108d", "1108e", "1108f", "1109a", "1109b", "1109c", "1109d", "1109e", "1109f", "1110a", "1110b", "1110c", "1110d", "1110e", "1110f", "1111a", "1111b", "1111c", "1111d", "1111e", "1111f", "1112a", "1112b", "1112c", "1112d", "1112e", "1112f", "1113a", "1113b", "1113c", "1113d", "1113e", "1113f", "1114a", "1114b", "1114c", "1114d", "1114e", "1114f", "1115a", "1115b", "1115c", "1115d", "1115e", "1115f", "1116a", "1116b", "1116c", "1116d", "1116e", "1116f", "1117a", "1117b", "1117c", "1117d", "1117e", "1117f", "1118a", "1118b", "1118c", "1118d", "1118e", "1118f", "1119a", "1119b", "1119c", "1119d", "1119e", "1119f", "1120a", "1120b", "1120c", "1120d", "1120e", "1120f", "1121a", "1121b", "1121c", "1121d", "1121e", "1121f", "1122a", "1122b", "1122c", "1122d", "1122e", "1122f", "1123a", "1123b", "1123c", "1123d", "1123e", "1123f", "1124a", "1124b", "1124c", "1124d", "1124e", "1124f", "1125a", "1125b", "1125c", "1125d", "1125e", "1125f", "1126a", "1126b", "1126c", "1126d", "1126e", "1126f", "1127a", "1127b", "1127c", "1127d", "1127e"]
}))
plutarch.addWork(utils.TextSpec("Aemilius Paulus", "2008.01.0080", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39"]
}))
plutarch.addWork(utils.TextSpec("Agesilaus", "2008.01.0081", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40"]
}))
plutarch.addWork(utils.TextSpec("Agis", "2008.01.0082", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"]
}))
plutarch.addWork(utils.TextSpec("Alcibiades", "1999.01.0181", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39"]
}))
plutarch.addWork(utils.TextSpec("Alexander", "2008.01.0129", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77"]
}))
plutarch.addWork(utils.TextSpec("Amatoriae narrationes", "2008.01.0316", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["771f", "772a", "772b", "772c", "772d", "772e", "772f", "773a", "773b", "773c", "773d", "773e", "773f", "774a", "774b", "774c", "774d", "774e", "774f", "775a", "775b", "775c", "775d", "775e"]
}))
plutarch.addWork(utils.TextSpec("Amatorius", "2008.01.0313", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["748e", "748f", "749a", "749b", "749c", "749d", "749e", "749f", "750a", "750b", "750c", "750d", "750e", "750f", "751a", "751b", "751c", "751d", "751e", "751f", "752a", "752b", "752c", "752d", "752e", "752f", "753a", "753b", "753c", "753d", "753e", "753f", "754a", "754b", "754c", "754d", "754e", "754f", "755a", "755b", "755c", "755d", "755e", "755f", "756a", "756b", "756c", "756d", "756e", "756f", "757a", "757b", "757c", "757d", "757e", "757f", "758a", "758b", "758c", "758d", "758e", "758f", "759a", "759b", "759c", "759d", "759e", "759f", "760a", "760b", "760c", "760d", "760e", "760f", "761a", "761b", "761c", "761d", "761e", "761f", "762a", "762b", "762c", "762d", "762e", "762f", "763a", "763b", "763c", "763d", "763e", "763f", "764a", "764b", "764c", "764d", "764e", "764f", "765a", "765b", "765c", "765d", "765e", "765f", "766a", "766b", "766c", "766d", "766e", "766f", "767a", "767b", "767c", "767d", "767e", "767f", "768a", "768b", "768c", "768d", "768e", "768f", "769a", "769b", "769c", "769d", "769e", "769f", "770a", "770b", "770c", "770d", "770e", "770f", "771a", "771b", "771c", "771d", "771e"]
}))
plutarch.addWork(utils.TextSpec("Animine an corporis affectiones sint peiores", "2008.01.0282", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["500b", "500c", "500d", "500e", "500f", "501a", "501b", "501c", "501d", "501e", "501f", "502a"]
}))
plutarch.addWork(utils.TextSpec("Antony", "2008.01.0077", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87"]
}))
plutarch.addWork(utils.TextSpec("Apophthegmata Laconica", "2008.01.0195", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["208b", "208c", "208d", "208e", "208f", "209a", "209b", "209c", "209d", "209e", "209f", "210a", "210b", "210c", "210d", "210e", "210f", "211a", "211b", "211c", "211d", "211e", "211f", "212a", "212b", "212c", "212d", "212e", "212f", "213a", "213b", "213c", "213d", "213e", "213f", "214a", "214b", "214c", "214d", "214e", "214f", "215a", "215b", "215c", "215d", "215e", "215f", "216a", "216b", "216c", "216d", "216e", "216f", "217a", "217b", "217c", "217d", "217e", "217f", "218a", "218b", "218c", "218d", "218e", "218f", "219a", "219b", "219c", "219d", "219e", "219f", "220a", "220b", "220c", "220d", "220e", "220f", "221a", "221b", "221c", "221d", "221e", "221f", "222a", "222b", "222c", "222d", "222e", "222f", "223a", "223b", "223c", "223d", "223e", "223f", "224a", "224b", "224c", "224d", "224e", "224f", "225a", "225b", "225c", "225d", "225e", "225f", "226a", "226b", "226c", "226d", "226e", "226f", "227a", "227b", "227c", "227d", "227e", "227f", "228a", "228b", "228c", "228d", "228e", "228f", "229a", "229b", "229c", "229d", "229e", "229f", "230a", "230b", "230c", "230d", "230e", "230f", "231a", "231b", "231c", "231d", "231e", "231f", "232a", "232b", "232c", "232d", "232e", "232f", "233a", "233b", "233c", "233d", "233e", "233f", "234a", "234b", "234c", "234d", "234e", "234f", "235a", "235b", "235c", "235d", "235e", "235f", "236a", "236b", "236c", "236d", "236e"]
}))
plutarch.addWork(utils.TextSpec("Aquane an ignis sit utilior", "2008.01.0364", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["955d", "955e", "955f", "956a", "956b", "956c", "956d", "956e", "956f", "957a", "957b", "957c", "957d", "957e", "957f", "958a", "958b", "958c", "958d", "958e"]
}))
plutarch.addWork(utils.TextSpec("Aratus", "2008.01.0083", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54"]
}))
plutarch.addWork(utils.TextSpec("Aristides", "1999.01.0182", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27"]
}))
plutarch.addWork(utils.TextSpec("Artaxerxes", "2008.01.0084", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
}))
plutarch.addWork(utils.TextSpec("Bruta animalia ratione uti", "2008.01.0372", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["985d", "985e", "985f", "986a", "986b", "986c", "986d", "986e", "986f", "987a", "987b", "987c", "987d", "987e", "987f", "988a", "988b", "988c", "988d", "988e", "988f", "989a", "989b", "989c", "989d", "989e", "989f", "990a", "990b", "990c", "990d", "990e", "990f", "991a", "991b", "991c", "991d", "991e", "991f", "992a", "992b", "992c", "992d", "992e"]
}))
plutarch.addWork(utils.TextSpec("Brutus", "2008.01.0085", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53"]
}))
plutarch.addWork(utils.TextSpec("Caesar", "2008.01.0130", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69"]
}))
plutarch.addWork(utils.TextSpec("Caius Gracchus", "2008.01.0089", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]
}))
plutarch.addWork(utils.TextSpec("Caius Marcius Coriolanus", "2008.01.0109", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39"]
}))
plutarch.addWork(utils.TextSpec("Caius Marius", "2008.01.0132", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46"]
}))
plutarch.addWork(utils.TextSpec("Camillus", "2008.01.0086", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43"]
}))
plutarch.addWork(utils.TextSpec("Cato the Younger", "2008.01.0088", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73"]
}))
plutarch.addWork(utils.TextSpec("Cicero", "2008.01.0090", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49"]
}))
plutarch.addWork(utils.TextSpec("Cimon", "2008.01.0069", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]
}))
plutarch.addWork(utils.TextSpec("Cleomenes", "2008.01.0091", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39"]
}))
plutarch.addWork(utils.TextSpec("Comparationis Aristophanis et Menandri compendium", "2008.01.0348", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["853a", "853b", "853c", "853d", "853e", "853f", "854a", "854b", "854c", "854d"]
}))
plutarch.addWork(utils.TextSpec("Comparison of Agesilaus and Pompey", "2008.01.0092", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5"]
}))
plutarch.addWork(utils.TextSpec("Comparison of Agis and Cleomenes and the Gracchi", "2008.01.0093", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5"]
}))
plutarch.addWork(utils.TextSpec("Comparison of Alcibiades and Coriolanus", "2008.01.0094", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5"]
}))
plutarch.addWork(utils.TextSpec("Comparison of Aristides with Marcus Cato", "2008.01.0095", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6"]
}))
plutarch.addWork(utils.TextSpec("Comparison of Demetrius and Antony", "2008.01.0078", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6"]
}))
plutarch.addWork(utils.TextSpec("Comparison of Demosthenes with Cicero", "2008.01.0096", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5"]
}))
plutarch.addWork(utils.TextSpec("Comparison of Dion and Brutus", "2008.01.0097", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5"]
}))
plutarch.addWork(utils.TextSpec("Comparison of Lucullus and Cimon", "2008.01.0098", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3"]
}))
plutarch.addWork(utils.TextSpec("Comparison of Lycurgus and Numa", "2008.01.0099", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4"]
}))
plutarch.addWork(utils.TextSpec("Comparison of Lysander and Sulla", "2008.01.0100", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5"]
}))
plutarch.addWork(utils.TextSpec("Comparison of Nicias and Crassus", "2008.01.0101", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5"]
}))
plutarch.addWork(utils.TextSpec("Comparison of Pelopidas and Marcellus", "2008.01.0102", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3"]
}))
plutarch.addWork(utils.TextSpec("Comparison of Pericles and Fabius Maximus", "2008.01.0103", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3"]
}))
plutarch.addWork(utils.TextSpec("Comparison of Philopoemen and Titus", "2008.01.0104", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3"]
}))
plutarch.addWork(utils.TextSpec("Comparison of Sertorius and Eumenes", "2008.01.0105", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2"]
}))
plutarch.addWork(utils.TextSpec("Comparison of Solon and Publicola", "2008.01.0106", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4"]
}))
plutarch.addWork(utils.TextSpec("Comparison of Theseus and Romulus", "2008.01.0107", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6"]
}))
plutarch.addWork(utils.TextSpec("Comparison of Timoleon and Aemilius", "2008.01.0108", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2"]
}))
plutarch.addWork(utils.TextSpec("Compendium Argumenti Stoicos absurdiora poetis dicere", "2008.01.0390", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["1057d", "1057e", "1057f", "1058a", "1058b", "1058c", "1058d", "1058e"]
}))
plutarch.addWork(utils.TextSpec("Compendium libri de animae procreatione in Timaeo", "2008.01.0387", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["1030d", "1030e", "1030f", "1031a", "1031b", "1031c", "1031d", "1031e", "1031f", "1032a", "1032b", "1032c", "1032d", "1032e", "1032f"]
}))
plutarch.addWork(utils.TextSpec("Conjugalia Praecepta", "2008.01.0180", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["138a", "138b", "138c", "138d", "138e", "138f", "139a", "139b", "139c", "139d", "139e", "139f", "140a", "140b", "140c", "140d", "140e", "140f", "141a", "141b", "141c", "141d", "141e", "141f", "142a", "142b", "142c", "142d", "142e", "142f", "143a", "143b", "143c", "143d", "143e", "143f", "144a", "144b", "144c", "144d", "144e", "144f", "145a", "145b", "145c", "145d", "145e", "145f", "146a"]
}))
plutarch.addWork(utils.TextSpec("Consolatio ad Apollonium", "2008.01.0172", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["101f", "102a", "102b", "102c", "102d", "102e", "102f", "103a", "103b", "103c", "103d", "103e", "103f", "104a", "104b", "104c", "104d", "104e", "104f", "105a", "105b", "105c", "105d", "105e", "105f", "106a", "106b", "106c", "106d", "106e", "106f", "107a", "107b", "107c", "107d", "107e", "107f", "108a", "108b", "108c", "108d", "108e", "108f", "109a", "109b", "109c", "109d", "109e", "109f", "110a", "110b", "110c", "110d", "110e", "110f", "111a", "111b", "111c", "111d", "111e", "111f", "112a", "112b", "112c", "112d", "112e", "112f", "113a", "113b", "113c", "113d", "113e", "113f", "114a", "114b", "114c", "114d", "114e", "114f", "115a", "115b", "115c", "115d", "115e", "115f", "116a", "116b", "116c", "116d", "116e", "116f", "117a", "117b", "117c", "117d", "117e", "117f", "118a", "118b", "118c", "118d", "118e", "118f", "119a", "119b", "119c", "119d", "119e", "119f", "120a", "120b", "120c", "120d", "120e", "120f", "121a", "121b", "121c", "121d", "121e", "121f", "122a"]
}))
plutarch.addWork(utils.TextSpec("Consolatio ad uxorem", "2008.01.0309", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["608b", "608c", "608d", "608e", "608f", "609a", "609b", "609c", "609d", "609e", "609f", "610a", "610b", "610c", "610d", "610e", "610f", "611a", "611b", "611c", "611d", "611e", "611f", "612a", "612b"]
}))
plutarch.addWork(utils.TextSpec("Crassus", "2008.01.0110", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33"]
}))
plutarch.addWork(utils.TextSpec("De Alexandri magni fortuna aut virtute", "2008.01.0229", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["326d", "326e", "326f", "327a", "327b", "327c", "327d", "327e", "327f", "328a", "328b", "328c", "328d", "328e", "328f", "329a", "329b", "329c", "329d", "329e", "329f", "330a", "330b", "330c", "330d", "330e", "330f", "331a", "331b", "331c", "331d", "331e", "331f", "332a", "332b", "332c", "332d", "332e", "332f", "333a", "333b", "333c", "333e", "333f", "334a", "334b", "334c", "334d", "334e", "334f", "335a", "335b", "335c", "335d", "335e", "335f", "336a", "336b", "336c", "336d", "336e", "336f", "337a", "337b", "337c", "337d", "337e", "337f", "338a", "338b", "338c", "338d", "338e", "338f", "339a", "339b", "339c", "339d", "339e", "339f", "340a", "340b", "340c", "340d", "340e", "340f", "341a", "341b", "341c", "341d", "341e", "341f", "342a", "342b", "342c", "342d", "342e", "342f", "343a", "343b", "343c", "343d", "343e", "343f", "344a", "344b", "344c", "344d", "344e", "344f", "345a", "345b"]
}))
plutarch.addWork(utils.TextSpec("De amicorum multitudine", "2008.01.0160", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["93b", "93c", "93d", "93e", "93f", "94a", "94b", "94c", "94d", "94e", "94f", "95a", "95b", "95c", "95d", "95e", "95f", "96a", "96b", "96c", "96d", "96e", "96f", "97a", "97b"]
}))
plutarch.addWork(utils.TextSpec("De amore prolis", "2008.01.0274", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["493a", "493b", "493c", "493d", "493e", "493f", "494a", "494b", "494c", "494d", "494e", "494f", "495a", "495b", "495c", "495d", "495e", "495f", "496a", "496c", "496d", "496e", "496f", "497a", "497b", "497c", "497d", "497e"]
}))
plutarch.addWork(utils.TextSpec("De animae procreatione in Timaeo", "2008.01.0385", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["1012b", "1012c", "1012d", "1012e", "1012f", "1013a", "1013b", "1013c", "1013d", "1013e", "1013f", "1014a", "1014b", "1014c", "1014d", "1014e", "1014f", "1015a", "1015b", "1015c", "1015d", "1015e", "1015f", "1016a", "1016b", "1016c", "1016d", "1016e", "1016f", "1017a", "1017b", "1017c", "1022e1", "1022f", "1023a", "1023b", "1023c", "1023d", "1023e", "1023f", "1024a", "1024b", "1024c", "1024d", "1024e", "1024f", "1025a", "1025b", "1025c", "1025d", "1025e", "1025f", "1026a", "1026b", "1026c", "1026d", "1026e", "1026f", "1027a", "1027b", "1027c", "1027d", "1027e", "1027f", "1017c2", "1017d", "1017e", "1017f", "1018a", "1018b", "1018c", "1018d", "1018e", "1018f", "1019a", "1019b", "1019c", "1019d", "1019e", "1019f", "1020a", "1020b", "1020c", "1020d", "1020e", "1020f", "1021a", "1021b", "1021c", "1021d", "1021e", "1021f", "1022a", "1022b", "1022c", "1022d", "1022e", "1027f2", "1028a", "1028b", "1028c", "1028d", "1028e", "1028f", "1029a", "1029b", "1029c", "1029d", "1029e", "1029f", "1030a", "1030b", "1030c"]
}))
plutarch.addWork(utils.TextSpec("De capienda ex inimicis utilitate", "2008.01.0156", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["86b", "86c", "86d", "86e", "86f", "87a", "87b", "87c", "87d", "87e", "87f", "88a", "88b", "88c", "88d", "88e", "88f", "89a", "89b", "89c", "89d", "89e", "89f", "90a", "90b", "90c", "90d", "90e", "90f", "91a", "91b", "91c", "91d", "91e", "91f", "92a", "92b", "92c", "92d", "92e", "92f"]
}))
plutarch.addWork(utils.TextSpec("De cohibenda ira", "2008.01.0262", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["452f", "453a", "453b", "453c", "453d", "453e", "453f", "454a", "454b", "454c", "454d", "454e", "454f", "455a", "455b", "455c", "455d", "455e", "455f", "456a", "456b", "456c", "456d", "456e", "456f", "457a", "457b", "457c", "457d", "457e", "457f", "458a", "458b", "458c", "458d", "458e", "458f", "459a", "459b", "459c", "459d", "459e", "459f", "460a", "460b", "460c", "460d", "460e", "460f", "461a", "461b", "461c", "461d", "461e", "461f", "462a", "462b", "462c", "462d", "462e", "462f", "463a", "463b", "463c", "463d", "463e", "463f", "464a", "464b", "464c", "464d"]
}))
plutarch.addWork(utils.TextSpec("De communibus notitiis adversus Stoicos", "2008.01.0392", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["1058f", "1059a", "1059b", "1059c", "1059d", "1059e", "1059f", "1060a", "1060b", "1060c", "1060d", "1060e", "1060f", "1061a", "1061b", "1061c", "1061d", "1061e", "1061f", "1062a", "1062b", "1062c", "1062d", "1062e", "1062f", "1063a", "1063b", "1063c", "1063d", "1063e", "1063f", "1064a", "1064b", "1064c", "1064d", "1064e", "1064f", "1065a", "1065b", "1065c", "1065d", "1065e", "1065f", "1066a", "1066b", "1066c", "1066d", "1066e", "1066f", "1067a", "1067b", "1067c", "1067d", "1067e", "1067f", "1068a", "1068b", "1068c", "1068d", "1068e", "1068f", "1069a", "1069b", "1069c", "1069d", "1069e", "1069f", "1070a", "1070b", "1070c", "1070d", "1070e", "1070f", "1071a", "1071b", "1071c", "1071d", "1071e", "1071f", "1072a", "1072b", "1072c", "1072d", "1072e", "1072f", "1073a", "1073b", "1073c", "1073d", "1073e", "1073f", "1074a", "1074b", "1074c", "1074d", "1074e", "1074f", "1075a", "1075b", "1075c", "1075d", "1075e", "1075f", "1076a", "1076b", "1076c", "1076d", "1076e", "1076f", "1077a", "1077b", "1077c", "1077d", "1077e", "1077f", "1078a", "1078b", "1078c", "1078d", "1078e", "1078f", "1079a", "1079b", "1079c", "1079d", "1079e", "1079f", "1080a", "1080b", "1080c", "1080d", "1080e", "1080f", "1081a", "1081b", "1081c", "1081d", "1081e", "1081f", "1082a", "1082b", "1082c", "1082d", "1082e", "1082f", "1083a", "1083b", "1083c", "1083d", "1083e", "1083f", "1084a", "1084b", "1084c", "1084d", "1084e", "1084f", "1085a", "1085b", "1085c", "1085d", "1085e", "1085f", "1086a", "1086b"]
}))
plutarch.addWork(utils.TextSpec("De cupiditate divitiarum", "2008.01.0293", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["523c", "523d", "523e", "523f", "524a", "524b", "524c", "524d", "524e", "524f", "525a", "525b", "525c", "525d", "525e", "525f", "526a", "526b", "526c", "526d", "526e", "526f", "527a", "527b", "527c", "527d", "527e", "527f", "528a", "528b"]
}))
plutarch.addWork(utils.TextSpec("De curiositate", "2008.01.0290", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["515b", "515c", "515d", "515e", "515f", "516a", "516b", "516c", "516d", "516e", "516f", "517a", "517b", "517c", "517d", "517e", "517f", "518a", "518b", "518c", "518d", "518e", "518f", "519a", "519b", "519c", "519d", "519e", "519f", "520a", "520b", "520c", "520d", "520e", "520f", "521a", "521b", "521c", "521d", "521e", "521f", "522a", "522b", "522c", "522d", "522e", "522f", "523a", "523b"]
}))
plutarch.addWork(utils.TextSpec("De defectu oraculorum", "2008.01.0250", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["409e", "409f", "410a", "410b", "410c", "410d", "410e", "410f", "411a", "411b", "411c", "411d", "411e", "411f", "412a", "412b", "412c", "412d", "412e", "412f", "413a", "413b", "413c", "413d", "413e", "413f", "414a", "414b", "414c", "414d", "414e", "414f", "415a", "415b", "415c", "415d", "415e", "415f", "416a", "416b", "416c", "416d", "416e", "416f", "417a", "417b", "417c", "417d", "417e", "417f", "418a", "418b", "418c", "418d", "418e", "418f", "419a", "419b", "419c", "419d", "419e", "419f", "420a", "420b", "420c", "420d", "420e", "420f", "421a", "421b", "421c", "421d", "421e", "421f", "422a", "422b", "422c", "422d", "422e", "422f", "423a", "423b", "423c", "423d", "423e", "423f", "424a", "424b", "424c", "424d", "424e", "425a", "425b", "425c", "425d", "425e", "425f", "426a", "426b", "426c", "426d", "426e", "426f", "427a", "427b", "427c", "427d", "427e", "427f", "428a", "428b", "428c", "428d", "428e", "428f", "429a", "429b", "429c", "429d", "429e", "429f", "430a", "430b", "430c", "430d", "430e", "430f", "431a", "431b", "431c", "431d", "431e", "431f", "432a", "432b", "432c", "432d", "432e", "432f", "433a", "433b", "433c", "433d", "433e", "433f", "434a", "434b", "434c", "434d", "434e", "434f", "435a", "435b", "435c", "435d", "435e", "435f", "436a", "436b", "436c", "436d", "436e", "436f", "437a", "437b", "437c", "437d", "437e", "437f", "438a", "438b", "438c", "438d", "438e"]
}))
plutarch.addWork(utils.TextSpec("De E apud Delphos", "2008.01.0242", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["384d", "384e", "384f", "385a", "385b", "385c", "385d", "385e", "385f", "386a", "386b", "386c", "386d", "386e", "386f", "387a", "387b", "387c", "387d", "387e", "387f", "388a", "388b", "388c", "388d", "388e", "388f", "389a", "389b", "389c", "389d", "389e", "389f", "390a", "390b", "390c", "390d", "390e", "390f", "391a", "391b", "391c", "391d", "391e", "391f", "392a", "392b", "392c", "392d", "392e", "392f", "393a", "393b", "393c", "393d", "393e", "393f", "394a", "394b", "394c"]
}))
plutarch.addWork(utils.TextSpec("De esu carnium I", "2008.01.0376", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["993a", "993b", "993c", "993d", "993e", "993f", "994a", "994b", "994c", "994d", "994e", "994f", "995a", "995b", "995c", "995d", "995e", "995f", "996a", "996b", "996c"]
}))
plutarch.addWork(utils.TextSpec("De esu carnium II", "2008.01.0380", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["966d", "966e", "996f", "997a", "997b", "997c", "997d", "997e", "997f", "998a", "998b", "998c", "998d", "998e", "998f", "999a", "999b"]
}))
plutarch.addWork(utils.TextSpec("De exilio", "2008.01.0307", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["599a", "599b", "599c", "599d", "599e", "599f", "600a", "600b", "600c", "600d", "600e", "600f", "601a", "601b", "601c", "601d", "601e", "601f", "602a", "602b", "602c", "602d", "602e", "602f", "603a", "603b", "603c", "603d", "603e", "603f", "604a", "604b", "604c", "604d", "604e", "604f", "605a", "605b", "605c", "605d", "606b", "606c", "606d", "606e", "606f", "607a", "607b", "607c", "607d", "607e", "607f"]
}))
plutarch.addWork(utils.TextSpec("De faciae quae in orbe lunae apparet", "2008.01.0356", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["920b", "920c", "920d", "920e", "920f", "921a", "921b", "921c", "921d", "921e", "921f", "922a", "922b", "922c", "922d", "922e", "922f", "923a", "923b", "923c", "923d", "923e", "923f", "924a", "924b", "924c", "924d", "924e", "924f", "925a", "925b", "925c", "925d", "925e", "925f", "926a", "926b", "926c", "926d", "926e", "926f", "927a", "927b", "927c", "927d", "927e", "927f", "928a", "928b", "928c", "928d", "928e", "928f", "929a", "929b", "929c", "929d", "929e", "929f", "930a", "930b", "930c", "930d", "930e", "930f", "931a", "931b", "931c", "931d", "931e", "931f", "932a", "932b", "932c", "932d", "932e", "932f", "933a", "933b", "933c", "933d", "933e", "933f", "934a", "934b", "934c", "934d", "934e", "934f", "935a", "935b", "935c", "935d", "935e", "935f", "936a", "936b", "936c", "936d", "936e", "936f", "937a", "937b", "937c", "937d", "937e", "937f", "938a", "938b", "938c", "938d", "938e", "938f", "939a", "939b", "939c", "939d", "939e", "939f", "940a", "940b", "940c", "940d", "940e", "940f", "941a", "941b", "941c", "941d", "941e", "941f", "942a", "942b", "942c", "942d", "942e", "942f", "943a", "943b", "943c", "943d", "943e", "943f", "944a", "944b", "944c", "944d", "944e", "944f", "945a", "945b", "945c", "945d"]
}))
plutarch.addWork(utils.TextSpec("De fato", "2008.01.0303", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["568b", "568c", "568d", "568e", "568f", "569a", "569b", "569c", "569d", "569e", "569f", "570a", "570b", "570c", "570d", "570e", "570f", "571a", "571b", "571c", "571d", "571e", "571f", "572a", "572b", "572c", "572d", "572e", "572f", "573a", "573b", "573c", "573d", "573e", "573f", "574a", "574b", "574c", "574d", "574e", "574f"]
}))
plutarch.addWork(utils.TextSpec("De fortuna", "2008.01.0164", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["97c", "97d", "97e", "97f", "98a", "98b", "98c", "98d", "98e", "98f", "99a", "99b", "99c", "99d", "99e", "99f", "100a"]
}))
plutarch.addWork(utils.TextSpec("De fortuna Romanorum", "2008.01.0221", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["316c", "316d", "316e", "316f", "317a", "317b", "317c", "317d", "317e", "317f", "318a", "318b", "318c", "318d", "318e", "318f", "319a", "319b", "319c", "319d", "319e", "319f", "320a", "320b", "320c", "320d", "320e", "320f", "321a", "321b", "321c", "321d", "321e", "321f", "322a", "322b", "322c", "322f", "323a", "323b", "323c", "323d", "323e", "323f", "324a", "324b", "324c", "324d", "324e", "324f", "325a", "325b", "325c", "325d", "325e", "325f", "326a", "326b", "326c"]
}))
plutarch.addWork(utils.TextSpec("De fraterno amore", "2008.01.0270", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["478a", "478b", "478c", "478d", "478e", "478f", "479a", "479b", "479c", "479d", "479e", "479f", "480a", "480b", "480c", "480d", "480e", "480f", "481a", "481b", "481c", "481d", "481e", "481f", "482a", "482b", "482c", "482d", "482e", "482f", "483a", "483b", "483c", "483d", "483e", "483f", "484a", "484b", "484c", "484d", "484e", "484f", "485a", "485b", "485c", "485d", "485e", "485f", "486a", "486b", "486c", "486d", "486e", "486f", "487a", "487b", "487c", "487d", "487e", "487f", "488a", "488b", "488c", "488d", "488e", "488f", "489a", "489b", "489c", "489d", "489e", "489f", "490a", "490b", "490c", "490d", "490e", "490f", "491a", "491b", "491c", "491d", "491e", "491f", "492a", "492b", "492c", "492d"]
}))
plutarch.addWork(utils.TextSpec("De garrulitate", "2008.01.0286", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["502b", "502c", "502d", "502e", "502f", "503a", "503b", "503c", "503d", "503e", "503f", "504a", "504b", "504c", "504d", "504e", "504f", "505a", "505b", "505c", "505d", "505e", "505f", "506a", "506b", "506c", "506d", "506e", "506f", "507a", "507b", "507c", "507d", "507e", "507f", "508a", "508b", "508c", "508d", "508e", "508f", "509a", "509b", "509c", "509e", "509f", "510a", "510b", "510c", "510d", "510e", "510f", "511a", "511b", "511c", "511d", "511e", "511f", "512a", "512b", "512c", "512d", "512e", "512f", "513a", "513b", "513c", "513d", "513e", "513f", "514a", "514b", "514c", "514d", "514e", "514f", "515a"]
}))
plutarch.addWork(utils.TextSpec("De genio Socratis", "2008.01.0305", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["575a", "575b", "575c", "575d", "575e", "575f", "576a", "576b", "576c", "576d", "576e", "576f", "577a", "577b", "577c", "577d", "577e", "577f", "578a", "578b", "578c", "578d", "578e", "578f", "579a", "579b", "579c", "579d", "579e", "579f", "580a", "580b", "580c", "580d", "580e", "580f", "581a", "581b", "581c", "581d", "581e", "581f", "582a", "582b", "582c", "582d", "582e", "582f", "583a", "583b", "583c", "583d", "583e", "583f", "584a", "584b", "584c", "584d", "584e", "584f", "585a", "585b", "585c", "585d", "585e", "585f", "586a", "586b", "586c", "586d", "586e", "586f", "587a", "587b", "587c", "587d", "587e", "587f", "588a", "588b", "588c", "588d", "588e", "588f", "589a", "589b", "589c", "589d", "589e", "589f", "590a", "590b", "590c", "590d", "590e", "590f", "591a", "591b", "591c", "591d", "591e", "591f", "592a", "592b", "592c", "592d", "592e", "592f", "593a", "593b", "593c", "593d", "593e", "593f", "594a", "594b", "594c", "594d", "594e", "594f", "595a", "595b", "595c", "595d", "595e", "595f", "596a", "596b", "596c", "596d", "596e", "596f", "597a", "597b", "597c", "597d", "597e", "597f", "598a", "598b", "598c", "598d", "598e", "598f"]
}))
plutarch.addWork(utils.TextSpec("De gloria Atheniensium", "2008.01.0233", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["345c", "345d", "345e", "345f", "346a", "346b", "346c", "346d", "346e", "346f", "347a", "347b", "347c", "347d", "347e", "347f", "348a", "348b", "348c", "348d", "348f", "349a", "349b", "349c", "349d", "349e", "349f", "350a", "350b", "350c", "350d", "350e", "350f", "351a", "351b"]
}))
plutarch.addWork(utils.TextSpec("De Herodoti malignitate", "2008.01.0351", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["854e", "854f", "855a", "855b", "855c", "855d", "855e", "855f", "856a", "856b", "856c", "856d", "856e", "856f", "857a", "857b", "857c", "857d", "857e", "857f", "858a", "858b", "858c", "858d", "858e", "858f", "859a", "859b", "859c", "859d", "859e", "859f", "860a", "860b", "860c", "860d", "860e", "860f", "861a", "861b", "861c", "861d", "861e", "861f", "862a", "862b", "862c", "862d", "862e", "862f", "863a", "863b", "863c", "863d", "863e", "863f", "864a", "864b", "864c", "864d", "864e", "864f", "865a", "865b", "865c", "865d", "865e", "865f", "866a", "866b", "866c", "866d", "866e", "866f", "867a", "867b", "867c", "867d", "867e", "867f", "868a", "868b", "868c", "868d", "868e", "868f", "869a", "869b", "869c", "869d", "869e", "869f", "870a", "870b", "870c", "870d", "870e", "870f", "871a", "871b", "871c", "871d", "871e", "871f", "872a", "872b", "872c", "872d", "872e", "872f", "873a", "873b", "873c", "873d", "873e", "873f", "874a", "874b", "874c"]
}))
plutarch.addWork(utils.TextSpec("De invidia et odio", "2008.01.0297", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["536e", "536f", "537a", "537b", "537c", "537d", "537e", "537f", "538a", "538b", "538c", "538d", "538e"]
}))
plutarch.addWork(utils.TextSpec("De Iside et Osiride", "2008.01.0238", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["351c", "351d", "351e", "351f", "352a", "352b", "352c", "352d", "352e", "352f", "353a", "353b", "353c", "353d", "353e", "353f", "354a", "354b", "354c", "354d", "354e", "354f", "355a", "355b", "355c", "355d", "355e", "355f", "356a", "356b", "356c", "356d", "356e", "356f", "357a", "357b", "357c", "357d", "357e", "357f", "358a", "358b", "358c", "358d", "358e", "358f", "359a", "359b", "359c", "359d", "359e", "359f", "360a", "360b", "360c", "360d", "360e", "360f", "361a", "361b", "361c", "361d", "361e", "361f", "362a", "362b", "362c", "362d", "362e", "362f", "363a", "363b", "363c", "363d", "363e", "363f", "364a", "364b", "364c", "364d", "364e", "364f", "365a", "365b", "365c", "365d", "365e", "365f", "366a", "366b", "366c", "366d", "366e", "366f", "367a", "367b", "367c", "367d", "367e", "367f", "368a", "368b", "368c", "368d", "368e", "368f", "369a", "369b", "369c", "369d", "369e", "369f", "370a", "370b", "370c", "370d", "370e", "370f", "371a", "371b", "371c", "371d", "371e", "371f", "372a", "372b", "372c", "372d", "372e", "372f", "373a", "373b", "373c", "373d", "373e", "373f", "374a", "374b", "374c", "374d", "374e", "374f", "375a", "375b", "375c", "375d", "375e", "375f", "376a", "376b", "376c", "376d", "376e", "376f", "377a", "377b", "377c", "377d", "377e", "377f", "378a", "378b", "378c", "378d", "378e", "378f", "379a", "379b", "379c", "379d", "379e", "379f", "380a", "380b", "380c", "380d", "380e", "380f", "381a", "381b", "381d", "381e", "381f", "382a", "382b", "382c", "382d", "382e", "382f", "383a", "383b", "383c", "383d", "383e", "383f", "384a", "384b", "384c"]
}))
plutarch.addWork(utils.TextSpec("De liberis educandis", "2008.01.0136", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["1a", "1b", "1c", "1d", "2a", "2b", "2c", "2d", "2e", "2f", "3a", "3b", "3c", "3d", "3e", "3f", "4a", "4b", "4c", "4d", "4e", "4f", "5a", "5b", "5c", "5d", "5e", "5f", "6a", "6b", "6c", "6d", "6e", "6f", "7a", "7b", "7c", "7d", "7e", "7f", "8a", "8b", "8c", "8d", "8e", "8f", "9a", "9b", "9c", "9d", "9e", "9f", "10a", "10b", "10c", "10d", "10e", "10f", "11a", "11b", "11c", "11d", "11e", "11f", "12a", "12b", "12c", "12d", "12e", "12f", "13a", "13b", "13c", "13d", "13e", "13f", "14a", "14b", "14c"]
}))
plutarch.addWork(utils.TextSpec("De primo frigido", "2008.01.0360", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["945f", "946a", "946b", "946c", "946d", "946e", "946f", "947a", "947b", "947c", "947d", "947e", "947f", "948a", "948b", "948c", "948d", "948e", "948f", "949a", "949b", "949c", "949d", "949e", "949f", "950a", "950b", "950c", "950d", "950e", "950f", "951a", "951b", "951c", "951d", "951e", "951f", "952a", "952b", "952c", "952d", "952e", "952f", "953a", "953b", "953c", "953d", "953e", "953f", "954a", "954b", "954c", "954d", "954e", "954f", "955a", "955b", "955c"]
}))
plutarch.addWork(utils.TextSpec("De Pythiae oraculis", "2008.01.0246", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["394d", "394e", "394f", "395a", "395b", "395c", "395d", "395e", "395f", "396a", "396b", "396c", "396d", "396e", "396f", "397a", "397b", "397c", "397d", "397e", "397f", "398a", "398b", "398c", "398d", "398e", "398f", "399a", "399b", "399c", "399d", "399e", "399f", "400a", "400b", "400c", "400d", "400e", "400f", "401a", "401b", "401c", "401d", "401e", "401f", "402a", "402b", "402c", "402d", "402e", "402f", "403a", "403b", "403c", "403d", "403e", "403f", "404a", "404b", "404c", "404d", "404e", "404f", "405a", "405b", "405c", "405d", "405e", "405f", "406a", "406b", "406c", "406d", "406e", "406f", "407a", "407b", "407c", "407d", "407e", "407f", "408a", "408b", "408c", "408d", "408e", "408f", "409a", "409b", "409c", "409d"]
}))
plutarch.addWork(utils.TextSpec("De Recta Ratione Audiendi", "2008.01.0144", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["37c", "37d", "37e", "37f", "38a", "38b", "38c", "38d", "38e", "38f", "39a", "39b", "39c", "39d", "39e", "39f", "40a", "40b", "40c", "40d", "40e", "40f", "41a", "41b", "41c", "41d", "41e", "41f", "42a", "42b", "42c", "42d", "42e", "42f", "43a", "43b", "43c", "43d", "43e", "43f", "44a", "44b", "44c", "44d", "44e", "44f", "45a", "45b", "45c", "45d", "45e", "45f", "46a", "46b", "46c", "46d", "46e", "46f", "47a", "47b", "47c", "47d", "47e", "47f", "48a", "48b", "48c", "48d"]
}))
plutarch.addWork(utils.TextSpec("De Se Ipsum Citra Invidiam Laudando", "2008.01.0299", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["539a", "539b", "539c", "539d", "539e", "539f", "540a", "540b", "540c", "540d", "540e", "540f", "541a", "541b", "541c", "541d", "541e", "541f", "542a", "542b", "542c", "542d", "542e", "542f", "543a", "543b", "543c", "543d", "543e", "543f", "544a", "544b", "544c", "544d", "544e", "544f", "545a", "545b", "545c", "545d", "545e", "545f", "546a", "546b", "546c", "546d", "546e", "546f", "547a", "547b", "547c", "547d", "547e", "547f"]
}))
plutarch.addWork(utils.TextSpec("De sera numinis vindicta", "2008.01.0301", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["548a", "548b", "548c", "548d", "548e", "548f", "549a", "549b", "549c", "549d", "549e", "549f", "550a", "550b", "550c", "550d", "550e", "550f", "551a", "551b", "551c", "551d", "551e", "551f", "552a", "552b", "552c", "552d", "552e", "552f", "553a", "553b", "553c", "553d", "553e", "553f", "554a", "554b", "554c", "554d", "554e", "554f", "555a", "555b", "555c", "555d", "555e", "555f", "556a", "556b", "556c", "556d", "556e", "556f", "557a", "557b", "557c", "557d", "557e", "557f", "558a", "558b", "558c", "558d", "558e", "558f", "559a", "559b", "559c", "559d", "559e", "559f", "560a", "560b", "560c", "560d", "560e", "560f", "561a", "561b", "561c", "561d", "561e", "561f", "562a", "562b", "562c", "562d", "562e", "562f", "563a", "563b", "563c", "563d", "563e", "563f", "564a", "564b", "564c", "564d", "564e", "564f", "565a", "565b", "565c", "565d", "565e", "565f", "566a", "566b", "566c", "566d", "566e", "566f", "567a", "567b", "567c", "567d", "567e", "567f", "568a"]
}))
plutarch.addWork(utils.TextSpec("De sollertia animalium", "2008.01.0368", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["959a", "959b", "959c", "959d", "959e", "959f", "960a", "960b", "960c", "960d", "960e", "960f", "961a", "961b", "961c", "961d", "961e", "961f", "962a", "962b", "962c", "962d", "962e", "962f", "963a", "964a", "964b", "964c", "964d", "964e", "964f", "965a", "965b", "965c", "965d", "965e", "965f", "966a", "966b", "966c", "966d", "966e", "966f", "967a", "967b", "967c", "967d", "967e", "967f", "968a", "968b", "968c", "968d", "968e", "968f", "969a", "969b", "969c", "969f", "970a", "970b", "970c", "970d", "970e", "970f", "971a", "971b", "971c", "971d", "971e", "971f", "972a", "972b", "972c", "972d", "972e", "972f", "973a", "973b", "973c", "973d", "973e", "973f", "974a", "974b", "974c", "974d", "974e", "974f", "975a", "975b", "975c", "975d", "975e", "975f", "976a", "976b", "976c", "976d", "976e", "976f", "977a", "977b", "977c", "977d", "977e", "977f", "978a", "978b", "978c", "978d", "978e", "978f", "979a", "979b", "979c", "979d", "979e", "979f", "980a", "980b", "980c", "980d", "980e", "980f", "981a", "981b", "981c", "981d", "981e", "981f", "982a", "982b", "982c", "982d", "982e", "982f", "983a", "983b", "983c", "983d", "983e", "983f", "984a", "984b", "984c", "984d", "984e", "984f", "985a", "985b", "985c"]
}))
plutarch.addWork(utils.TextSpec("De Stoicorum repugnantiis", "2008.01.0388", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["1033a", "1033b", "1033c", "1033d", "1033e", "1033f", "1034a", "1034b", "1034c", "1034d", "1034e", "1034f", "1035a", "1035b", "1035c", "1035d", "1035e", "1035f", "1036a", "1036b", "1036c", "1036d", "1036e", "1036f", "1037a", "1037b", "1037c", "1037d", "1037e", "1037f", "1038a", "1038b", "1038c", "1038d", "1038e", "1038f", "1039a", "1039b", "1039c", "1039d", "1039e", "1039f", "1040a", "1040b", "1040c", "1040d", "1040e", "1040f", "1041a", "1041b", "1041c", "1041d", "1041e", "1041f", "1042a", "1042b", "1042c", "1042d", "1042e", "1042f", "1043a", "1043b", "1043c", "1043d", "1043e", "1043f", "1044a", "1044b", "1044c", "1044d", "1044e", "1044f", "1045a", "1045b", "1045c", "1045d", "1045e", "1045f", "1046a", "1046b", "1046c", "1046d", "1046e", "1046f", "1047a", "1047b", "1047c", "1047d", "1047e", "1047f", "1048a", "1048b", "1048c", "1048d", "1048e", "1048f", "1049a", "1049b", "1049c", "1049d", "1049e", "1049f", "1050a", "1050b", "1050c", "1050d", "1050e", "1050f", "1051a", "1051b", "1051c", "1051d", "1051e", "1051f", "1052a", "1052b", "1052c", "1052d", "1052e", "1052f", "1053a", "1053b", "1053c", "1053e", "1053f", "1054a", "1054b", "1054c", "1054d", "1054e", "1054f", "1055a", "1055b", "1055c", "1055d", "1055e", "1055f", "1056a", "1056b", "1056c", "1056d", "1056e", "1056f", "1057a", "1057b", "1057c"]
}))
plutarch.addWork(utils.TextSpec("De superstitione", "2008.01.0188", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["164e", "164f", "165a", "165b", "165c", "165d", "165e", "165f", "166a", "166b", "166c", "166d", "166e", "166f", "167a", "167b", "167c", "167d", "167e", "167f", "168a", "168b", "168c", "168d", "168e", "168f", "169a", "169b", "169c", "169d", "169e", "169f", "170a", "170b", "170c", "170d", "170e", "170f", "171a", "171b", "171c", "171d", "171e", "171f"]
}))
plutarch.addWork(utils.TextSpec("De tranquilitate animi", "2008.01.0266", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["464e", "464f", "465a", "465b", "465c", "465d", "465e", "465f", "466a", "466b", "466c", "466d", "466e", "466f", "467a", "467b", "467c", "467d", "467e", "467f", "468a", "468b", "468c", "468d", "468e", "468f", "469a", "469b", "469c", "469d", "469e", "469f", "470a", "470b", "470c", "470d", "470e", "470f", "471a", "471b", "471c", "471d", "471e", "471f", "472a", "472b", "472c", "472d", "472e", "472f", "473a", "473b", "473c", "473d", "473e", "473f", "474a", "474b", "474c", "474d", "474e", "474f", "475a", "475b", "475c", "475d", "475e", "475f", "476a", "476b", "476c", "476d", "476e", "476f", "477a", "477b", "477c", "477d", "477e", "477f"]
}))
plutarch.addWork(utils.TextSpec("De tuenda sanitate praecepta", "2008.01.0176", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["122b", "122c", "122d", "122e", "122f", "123a", "123b", "123c", "123d", "123e", "123f", "124a", "124b", "124c", "124d", "124e", "124f", "125a", "125b", "125c", "125d", "125e", "125f", "126a", "126b", "126c", "126d", "126e", "126f", "127a", "127b", "127c", "127d", "127e", "127f", "128a", "128b", "128c", "128d", "128e", "128f", "129a", "129b", "129c", "129d", "129e", "129f", "130a", "130b", "130c", "130d", "130e", "130f", "131a", "131b", "131c", "131d", "131e", "131f", "132a", "132b", "132c", "132d", "132e", "132f", "133a", "133b", "133c", "133d", "133e", "133f", "134a", "134b", "134c", "134d", "134e", "134f", "135a", "135b", "135c", "135d", "135e", "135f", "136a", "136b", "136c", "136d", "136e", "136f", "137a", "137b", "137c", "137d", "137e"]
}))
plutarch.addWork(utils.TextSpec("De unius in republica dominatione", "2008.01.0336", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["826a", "826b", "826c", "826d", "826e", "826f", "827a", "827b", "827c"]
}))
plutarch.addWork(utils.TextSpec("De virtute et vitio", "2008.01.0168", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["100b", "100c", "100d", "100e", "100f", "101a", "101b", "101c", "101d", "101e"]
}))
plutarch.addWork(utils.TextSpec("De virtute morali", "2008.01.0258", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["440d", "440e", "440f", "441a", "441b", "441c", "441d", "441e", "441f", "442a", "442b", "442c", "442d", "442e", "442f", "443a", "443b", "443c", "443d", "443e", "443f", "444a", "444b", "444c", "444d", "444e", "444f", "445a", "445b", "445c", "445d", "445e", "445f", "446a", "446b", "446c", "446d", "446e", "446f", "447a", "447b", "447c", "447d", "447e", "447f", "448a", "448b", "448c", "448d", "448e", "448f", "449a", "449b", "449c", "449d", "449e", "449f", "450a", "450b", "450c", "450d", "450e", "450f", "451a", "451b", "451c", "451d", "451e", "451f", "452a", "452b", "452c", "452d", "452e"]
}))
plutarch.addWork(utils.TextSpec("De vitando aere alieno", "2008.01.0340", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["827d", "827e", "827f", "828a", "828b", "828c", "828d", "828e", "828f", "829a", "829b", "829c", "829d", "829e", "829f", "830a", "830b", "830c", "830d", "830e", "830f", "831a", "831b", "831c", "831d", "831e", "831f", "832a"]
}))
plutarch.addWork(utils.TextSpec("De vitioso pudore", "2008.01.0295", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["528c", "528d", "528e", "528f", "529a", "529b", "529c", "529d", "529e", "529f", "530a", "530b", "530c", "530d", "530e", "530f", "531a", "531b", "531c", "531d", "531e", "531f", "532a", "532b", "532c", "532d", "532e", "532f", "533a", "533b", "533c", "533d", "533e", "533f", "534a", "534b", "534c", "534d", "534e", "534f", "535a", "535b", "535c", "535d", "535e", "535f", "536a", "536b", "536c", "536d"]
}))
plutarch.addWork(utils.TextSpec("Demetrius", "2008.01.0076", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53"]
}))
plutarch.addWork(utils.TextSpec("Demosthenes", "2008.01.0111", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
}))
plutarch.addWork(utils.TextSpec("Dion", "2008.01.0112", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58"]
}))
plutarch.addWork(utils.TextSpec("Eumenes", "2008.01.0113", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]
}))
plutarch.addWork(utils.TextSpec("Fabius Maximus", "2008.01.0114", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27"]
}))
plutarch.addWork(utils.TextSpec("Galba", "2008.01.0116", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29"]
}))
plutarch.addWork(utils.TextSpec("Instituta Laconica", "2008.01.0199", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["236f", "237a", "237b", "237c", "237d", "237e", "237f", "238a", "238b", "238c", "238d", "238e", "238f", "239a", "239b", "239c", "239d", "239e", "239f", "240a", "240b"]
}))
plutarch.addWork(utils.TextSpec("Lacaenarum Apophthegmata", "2008.01.0202", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["240c", "240d", "240e", "240f", "241a", "241b", "241c", "241d", "241e", "241f", "242a", "242b", "242c", "242d"]
}))
plutarch.addWork(utils.TextSpec("Lucullus", "2008.01.0117", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43"]
}))
plutarch.addWork(utils.TextSpec("Lycurgus", "2008.01.0131", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
}))
plutarch.addWork(utils.TextSpec("Lysander", "2008.01.0070", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
}))
plutarch.addWork(utils.TextSpec("Marcellus", "2008.01.0118", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
}))
plutarch.addWork(utils.TextSpec("Marcus Cato", "2008.01.0087", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27"]
}))
plutarch.addWork(utils.TextSpec("Maxime cum principbus philosopho esse diserendum", "2008.01.0320", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["776a", "776b", "776c", "776d", "776e", "776f", "777a", "777b", "777c", "777d", "777e", "777f", "778a", "778b", "778c", "778d", "778e", "778f", "779a", "779b", "779c"]
}))
plutarch.addWork(utils.TextSpec("Mulierum virtutes", "2008.01.0205", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["242e", "242f", "243a", "243b", "243c", "243d", "243e", "243f", "244a", "244b", "244c", "244d", "244e", "244f", "245a", "245b", "245c", "245d", "245e", "245f", "246a", "246b", "246c", "246d", "246e", "246f", "247a", "247b", "247c", "247d", "247e", "247f", "248a", "248b", "248c", "248d", "248e", "248f", "249a", "249b", "249c", "249d", "249e", "249f", "250a", "250b", "250c", "250d", "250e", "250f", "251a", "251b", "251c", "251d", "251e", "251f", "252a", "252b", "252c", "252d", "252e", "252f", "253a", "253b", "253c", "253d", "253e", "253f", "254a", "254b", "254c", "254d", "254e", "254f", "255a", "255b", "255c", "255d", "255e", "255f", "256a", "256b", "256c", "256d", "256e", "256f", "257a", "257b", "257c", "257d", "257e", "257f", "258a", "258b", "258c", "258d", "258e", "258f", "259a", "259b", "259c", "259d", "259e", "259f", "260a", "260b", "260c", "260d", "260e", "260f", "261a", "261b", "261c", "261d", "261e", "261f", "262a", "262b", "262c", "262d", "262e", "262f", "263a", "263b", "263c"]
}))
plutarch.addWork(utils.TextSpec("Nicias", "2008.01.0071", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
}))
plutarch.addWork(utils.TextSpec("Non posse suaviter vivi secundum Epicurum", "2008.01.0394", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["1086c", "1086d", "1086e", "1086f", "1087a", "1087b", "1087c", "1087d", "1087e", "1087f", "1088a", "1088b", "1088c", "1088d", "1088e", "1088f", "1089a", "1089b", "1089c", "1089d", "1089e", "1089f", "1090a", "1090b", "1090c", "1090d", "1090e", "1090f", "1091a", "1091b", "1091c", "1091d", "1091e", "1091f", "1092a", "1092b", "1092c", "1092d", "1092e", "1092f", "1093a", "1093b", "1093c", "1093d", "1093e", "1093f", "1094a", "1094b", "1094c", "1094d", "1094e", "1094f", "1095a", "1095b", "1095c", "1095d", "1095e", "1095f", "1096a", "1096b", "1096c", "1096d", "1096e", "1096f", "1097a", "1097b", "1097c", "1097d", "1097e", "1097f", "1098a", "1098b", "1098c", "1098d", "1098e", "1098f", "1099a", "1099b", "1099c", "1099d", "1099e", "1099f", "1100a", "1100b", "1100c", "1100d", "1100e", "1100f", "1101a", "1101b", "1101c", "1101d", "1101e", "1101f", "1102a", "1102b", "1102c", "1102d", "1102e", "1102f", "1103a", "1103b", "1103c", "1103d", "1103e", "1103f", "1104a", "1104b", "1104c", "1104d", "1104e", "1104f", "1105a", "1105b", "1105c", "1105d", "1105e", "1105f", "1106a", "1106b", "1106c", "1106d", "1106e", "1106f", "1107a", "1107b", "1107c"]
}))
plutarch.addWork(utils.TextSpec("Numa", "2008.01.0133", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"]
}))
plutarch.addWork(utils.TextSpec("Otho", "2008.01.0119", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"]
}))
plutarch.addWork(utils.TextSpec("Parallela minora", "2008.01.0217", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["305a", "305b", "305c", "305d", "305e", "305f", "306a", "306b", "306c", "306d", "306e", "306f", "307a", "307b", "307c", "307d", "307e", "307f", "308a", "308b", "308c", "308d", "308e", "308f", "309a", "309b", "309c", "309d", "309e", "309f", "310a", "310b", "310c", "310d", "310e", "310f", "311a", "311b", "311c", "311d", "311e", "311f", "312a", "312b", "312c", "312d", "312e", "312f", "313a", "313b", "313c", "313d", "313e", "313f", "314a", "314b", "314c", "314d", "314e", "314f", "315a", "315b", "315c", "315d", "315e", "315f", "316a", "316b"]
}))
plutarch.addWork(utils.TextSpec("Pelopidas", "2008.01.0120", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35"]
}))
plutarch.addWork(utils.TextSpec("Pericles", "2008.01.0072", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39"]
}))
plutarch.addWork(utils.TextSpec("Philopoemen", "2008.01.0121", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"]
}))
plutarch.addWork(utils.TextSpec("Phocion", "2008.01.0122", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38"]
}))
plutarch.addWork(utils.TextSpec("Platonicae quaestiones", "2008.01.0383", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["999c", "999d", "999e", "999f", "1000a", "1000b", "1000c", "1000d", "1000e", "1000f", "1001a", "1001b", "1001c", "1001d", "1001e", "1001f", "1002a", "1002b", "1002c", "1002d", "1002e", "1002f", "1003a", "1003b", "1003c", "1003d", "1003e", "1003f", "1004a", "1004b", "1004c", "1004d", "1004e", "1004f", "1005a", "1005b", "1005c", "1005d", "1005e", "1005f", "1006a", "1006b", "1006c", "1006d", "1006e", "1006f", "1007a", "1007b", "1007c", "1007d", "1007e", "1007f", "1008a", "1008b", "1008c", "1008d", "1008e", "1008f", "1009a", "1009b", "1009c", "1009d", "1009e", "1009f", "1010a", "1010b", "1010c", "1010d", "1010e", "1010f", "1011a", "1011b", "1011c", "1011d", "1011e", "1011f"]
}))
plutarch.addWork(utils.TextSpec("Pompey", "2008.01.0123", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80"]
}))
plutarch.addWork(utils.TextSpec("Praecepta gerendae reipublicae", "2008.01.0332", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["798a", "798b", "798c", "798d", "798e", "798f", "799a", "799b", "799c", "799d", "799e", "799f", "800a", "800b", "800c", "800d", "800e", "800f", "801a", "801b", "801c", "801d", "801e", "801f", "802a", "802b", "802c", "802d", "802e", "802f", "803a", "803b", "803c", "803d", "803e", "803f", "804a", "804b", "804c", "804d", "804e", "804f", "805a", "805b", "805c", "805d", "805e", "805f", "806a", "806b", "806c", "806d", "806e", "806f", "807a", "807b", "807c", "807d", "807e", "807f", "808a", "808b", "808c", "808d", "808e", "808f", "809a", "809b", "809c", "809d", "809e", "809f", "810a", "810b", "810c", "810d", "810e", "810f", "811a", "811b", "811c", "811d", "811e", "811f", "812a", "812b", "812c", "812d", "812e", "812f", "813a", "813b", "813c", "813d", "813e", "813f", "814a", "814b", "814c", "814d", "814e", "814f", "815a", "815b", "815c", "815d", "815e", "815f", "816a", "816b", "816c", "816d", "816e", "816f", "817a", "817b", "817c", "817d", "817e", "817f", "818a", "818b", "818c", "818d", "818e", "818f", "819a", "819b", "819c", "819d", "819e", "819f", "820a", "820b", "820c", "820d", "820e", "820f", "821a", "821b", "821c", "821d", "821e", "822a", "822b", "822c", "822d", "822e", "822f", "823a", "823b", "823c", "823d", "823e", "823f", "824a", "824b", "824c", "824d", "824e", "824f", "825a", "825b", "825c", "825d", "825e", "825f"]
}))
plutarch.addWork(utils.TextSpec("Publicola", "2008.01.0124", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
}))
plutarch.addWork(utils.TextSpec("Pyrrhus", "2008.01.0134", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34"]
}))
plutarch.addWork(utils.TextSpec("Quaestiones Convivales", "2008.01.0311", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["612c", "612d", "612e", "612f", "613a", "613b", "613c", "613d", "613e", "613f", "614a", "614b", "614c", "614d", "614e", "614f", "615a", "615b", "615c", "615d", "615e", "615f", "616a", "616b", "616c", "616d", "616e", "616f", "617a", "617b", "617c", "617d", "617e", "617f", "618a", "618b", "618c", "618d", "618e", "618f", "619a", "619b", "619c", "619d", "619e", "619f", "620a", "620b", "620c", "620d", "620e", "620f", "621a", "621b", "621c", "621d", "621e", "621f", "622a", "622c", "622d", "622e", "622f", "623a", "623b", "623c", "623d", "623e", "623f", "624a", "624b", "624c", "624d", "624e", "624f", "625a", "625b", "625c", "625d", "625e", "625f", "626a", "626b", "626c", "626d", "626e", "626f", "627a", "627b", "627c", "627d", "627e", "627f", "628a", "628b", "628c", "628d", "628e", "628f", "629a", "629c", "629d", "629e", "629f", "630a", "630b", "630c", "630d", "630e", "630f", "631a", "631b", "631c", "631d", "631e", "631f", "632a", "632b", "632c", "632d", "632e", "632f", "633a", "633b", "633c", "633d", "633e", "633f", "634a", "634b", "634c", "634d", "634e", "634f", "635a", "635b", "635c", "635d", "635e", "635f", "636a", "636b", "636c", "636d", "636e", "636f", "637a", "637b", "637c", "637d", "637e", "637f", "638a", "638b", "638c", "638d", "638e", "638f", "639a", "639b", "639c", "639d", "639e", "639f", "640a", "640b", "640c", "640d", "640e", "640f", "641a", "641b", "641c", "641d", "641e", "641f", "642a", "642b", "642c", "642d", "642e", "642f", "643a", "643b", "643c", "643d", "643e", "643f", "644a", "644b", "644c", "644d", "644f", "645a", "645b", "645c", "645d", "645e", "645f", "646a", "646b", "646c", "646d", "646e", "646f", "647a", "647b", "647c", "647d", "647e", "647f", "648a", "648b", "648c", "648e", "648f", "649a", "649b", "649c", "649d", "649e", "649f", "650a", "650b", "650c", "650d", "650e", "650f", "651a", "651b", "651c", "651d", "651e", "651f", "652a", "652b", "652c", "652d", "652e", "652f", "653a", "653b", "653c", "653d", "653e", "653f", "654a", "654b", "654c", "654d", "654e", "654f", "655a", "655b", "655c", "655d", "655e", "655f", "656a", "656b", "656c", "656d", "656e", "656f", "657a", "657b", "657c", "657d", "657e", "657f", "658a", "658b", "658c", "658d", "658e", "658f", "659a", "659b", "659c", "659d", "659e", "659f", "660a", "660b", "660c", "660d", "660e", "660f", "661a", "661b", "661c", "661d", "661e", "661f", "662a", "662b", "662c", "662d", "662e", "662f", "663a", "663b", "663c", "663d", "663e", "663f", "664a", "664b", "664c", "664d", "664e", "664f", "665a", "665b", "665c", "665d", "665e", "665f", "666a", "666b", "666c", "666d", "666e", "666f", "667a", "667b", "667c", "667d", "667e", "667f", "668a", "668b", "668c", "668d", "668e", "668f", "669a", "669b", "669c", "669d", "669e", "669f", "670a", "670b", "670c", "670e", "670f", "671a", "671b", "671c", "671d", "671e", "671f", "672a", "672b", "672c", "672d", "672e", "672f", "673a", "673b", "673c", "673d", "673e", "673f", "674a", "674b", "674c", "674d", "674e", "674f", "675a", "675b", "675c", "675d", "675e", "675f", "676a", "676b", "676c", "676d", "676e", "676f", "677a", "677b", "677c", "677d", "677e", "677f", "678a", "678b", "678c", "678d", "678e", "678f", "679a", "679b", "679c", "679d", "679e", "679f", "680a", "680b", "680c", "680d", "680e", "680f", "681a", "681b", "681c", "681d", "681e", "681f", "682a", "682b", "682c", "682d", "682e", "682f", "683a", "683b", "683c", "683d", "683e", "683f", "684a", "684b", "684c", "684d", "684e", "684f", "685a", "685b", "685c", "685e", "685f", "686a", "686b", "686c", "686d", "686e", "686f", "687a", "687b", "687c", "687d", "687e", "687f", "688a", "688b", "688c", "688d", "688e", "688f", "689a", "689b", "689c", "689d", "689e", "689f", "690a", "690b", "690c", "690d", "690e", "690f", "691a", "691b", "691c", "691d", "691e", "691f", "692a", "692b", "692c", "692d", "692e", "692f", "693a", "693b", "693c", "693d", "693e", "694a", "694b", "694c", "694d", "694e", "694f", "695a", "695b", "695c", "695d", "695e", "695f", "696a", "696b", "696c", "696d", "696e", "696f", "697a", "697b", "697c", "697d", "697e", "697f", "698a", "698b", "698c", "698d", "698e", "698f", "699a", "699b", "699c", "699d", "699e", "700a", "700b", "700d", "700e", "700f", "701a", "701c", "701d", "701e", "701f", "702a", "702b", "702c", "702d", "702e", "702f", "703a", "703b", "703c", "703d", "703e", "703f", "704a", "704b", "704c", "704d", "704e", "704f", "705a", "705b", "705d", "705e", "705f", "706a", "706b", "706c", "706d", "706e", "707a", "707b", "707c", "707d", "707e", "707f", "708a", "708b", "708c", "708d", "708e", "708f", "709a", "709b", "709c", "709d", "709e", "709f", "710a", "710b", "710c", "710d", "710e", "710f", "711a", "711b", "711c", "711d", "711e", "711f", "712a", "712b", "712c", "712d", "712e", "712f", "713a", "713b", "713c", "713d", "713e", "713f", "714a", "714b", "714c", "714d", "714e", "714f", "715a", "715b", "715c", "715d", "715e", "715f", "716a", "716b", "716c", "716e", "716f", "717a", "717b", "717c", "717d", "717e", "717f", "718a", "718b", "718c", "718d", "718e", "718f", "719a", "719b", "719c", "719d", "719e", "719f", "720a", "720b", "720c", "720d", "720e", "720f", "721a", "721b", "721c", "721d", "721e", "721f", "722a", "722b", "722c", "722d", "722e", "722f", "723a", "723b", "723c", "723d", "723e", "723f", "724a", "724b", "724c", "724d", "724e", "724f", "725a", "725b", "725c", "725d", "725e", "725f", "726a", "726b", "726c", "726d", "726e", "726f", "727a", "727b", "727c", "727d", "727e", "727f", "728a", "728c", "728d", "728e", "728f", "729a", "729b", "729c", "729d", "729e", "729f", "730a", "730b", "730c", "730d", "730e", "730f", "731a", "731b", "731c", "731d", "731e", "731f", "732a", "732b", "732c", "732d", "732e", "732f", "733a", "733b", "733c", "733d", "733e", "733f", "734a", "734b", "734c", "734d", "734e", "734f", "735a", "735b", "735c", "735d", "735e", "735f", "736a", "736b", "736d", "736e", "736f", "737a", "737b", "737c", "737d", "737e", "737f", "738a", "738b", "738c", "738d", "738e", "738f", "739a", "739b", "739c", "739d", "739e", "739f", "740a", "740b", "740c", "740d", "740e", "740f", "741a", "741b", "741c", "741d", "741e", "741f", "742a", "742b", "742c", "742d", "742e", "742f", "743a", "743b", "743c", "743d", "743e", "743f", "744a", "744b", "744c", "744d", "744e", "744f", "745a", "745b", "745c", "745d", "745e", "745f", "746a", "746b", "746c", "746d", "746e", "746f", "747a", "747b", "747c", "747d", "747e", "747f", "748a", "748b", "748c", "748d"]
}))
plutarch.addWork(utils.TextSpec("Quaestiones Graecae", "2008.01.0213", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["291d", "291e", "291f", "292a", "292b", "292c", "292d", "292e", "292f", "293a", "293b", "293c", "293d", "293e", "293f", "294a", "294b", "294c", "294d", "294e", "294f", "295a", "295b", "295c", "295d", "295e", "295f", "296a", "296b", "296c", "296d", "296e", "296f", "297a", "297b", "297c", "297d", "297e", "297f", "298a", "298b", "298c", "298d", "298e", "298f", "299a", "299b", "299c", "299d", "299e", "299f", "300a", "300b", "300c", "300d", "300e", "300f", "301a", "301b", "301c", "301d", "301e", "301f", "302a", "302b", "302c", "302d", "302e", "302f", "303a", "303b", "303c", "303d", "303e", "303f", "304a", "304b", "304c", "304d", "304e", "304f"]
}))
plutarch.addWork(utils.TextSpec("Quaestiones Naturales", "2008.01.0353", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["911d", "911e", "911f", "912a", "912b", "912c", "912d", "912e", "912f", "913a", "913b", "913c", "913d", "913e", "913f", "914a", "914b", "914c", "914d", "914e", "914f", "915a", "915b", "915c", "915d", "915e", "915f", "916a", "916b", "916c", "916d", "916e", "916f", "917a", "917b", "917c", "917d", "917e", "917f", "918a", "918b", "918c", "918d", "918e", "918f", "919a", "919b", "919c", "919d"]
}))
plutarch.addWork(utils.TextSpec("Quaestiones Romanae", "2008.01.0209", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["263a", "263e", "263f", "264a", "264b", "264c", "264d", "264e", "264f", "265a", "265b", "265c", "265d", "265e", "265f", "266a", "266b", "266c", "266d", "266e", "266f", "267a", "267b", "267c", "267d", "267e", "267f", "268a", "268b", "268c", "268d", "268e", "268f", "269a", "269b", "269c", "269d", "269e", "269f", "270a", "270b", "270c", "270d", "270e", "270f", "271a", "271b", "271c", "271d", "271e", "271f", "272a", "272b", "272c", "272d", "272e", "272f", "273a", "273b", "273c", "273d", "273e", "273f", "274a", "274b", "274c", "274d", "274e", "274f", "275a", "275b", "275c", "275d", "275e", "275f", "276a", "276b", "276c", "276d", "276e", "276f", "277a", "277b", "277c", "277d", "277e", "277f", "278a", "278b", "278c", "278d", "278e", "278f", "279a", "279b", "279c", "279d", "279e", "279f", "280a", "280b", "280c", "280d", "280e", "280f", "281a", "281b", "281c", "281d", "281e", "282a", "282b", "282c", "282d", "282e", "282f", "283a", "283b", "283c", "283d", "283e", "283f", "284a", "284b", "284c", "284d", "284e", "284f", "285a", "285b", "285c", "285d", "285e", "285f", "286a", "286b", "286c", "286d", "286e", "286f", "287a", "287b", "287c", "287d", "287e", "287f", "288a", "288b", "288c", "288d", "288e", "288f", "289a", "289b", "289c", "289d", "289e", "289f", "290a", "290b", "290c", "290d", "290e", "290f", "291a", "291b", "291c"]
}))
plutarch.addWork(utils.TextSpec("Quomodo adolescens poetas audire debeat", "2008.01.0140", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["14d", "14e", "14f", "15a", "15b", "15c", "15d", "15e", "15f", "16a", "16b", "16c", "16d", "16e", "16f", "17a", "17b", "17c", "17d", "17e", "17f", "18a", "18b", "18c", "18d", "18e", "18f", "19a", "19b", "19c", "19d", "19e", "19f", "20a", "20b", "20c", "20d", "20e", "20f", "21a", "21b", "21c", "21d", "21e", "21f", "22a", "22b", "22c", "22d", "22e", "22f", "23a", "23b", "23c", "23d", "23e", "23f", "24a", "24b", "24c", "24d", "24e", "24f", "25a", "25b", "25c", "25d", "25e", "25f", "26a", "26b", "26c", "26d", "26e", "26f", "27a", "27b", "27c", "27d", "27e", "27f", "28a", "28b", "28c", "28d", "28e", "28f", "29a", "29b", "29c", "29d", "29e", "29f", "30a", "30b", "30c", "30d", "30e", "30f", "31a", "31b", "31c", "31d", "31e", "31f", "32a", "32b", "32c", "32d", "32e", "32f", "33a", "33b", "33c", "33d", "33e", "33f", "34a", "34b", "34c", "34d", "34e", "34f", "35a", "35b", "35c", "35d", "35e", "35f", "36a", "36b", "36c", "36d", "36e", "36f", "37a", "37b"]
}))
plutarch.addWork(utils.TextSpec("Quomodo adulator ab amico internoscatur", "2008.01.0148", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["48e", "48f", "49a", "49b", "49c", "49d", "49e", "49f", "50a", "50b", "50c", "50d", "50e", "50f", "51a", "51b", "51c", "51d", "51e", "51f", "52a", "52b", "52c", "52d", "52e", "52f", "53a", "53b", "53c", "53d", "53e", "53f", "54a", "54b", "54c", "54d", "54e", "54f", "55a", "55b", "55c", "55d", "55e", "55f", "56a", "56b", "56c", "56d", "56e", "56f", "57a", "57b", "57c", "57d", "57e", "57f", "58a", "58b", "58c", "58d", "58e", "58f", "59a", "59b", "59c", "59d", "59e", "59f", "60a", "60b", "60c", "60d", "60e", "60f", "61a", "61b", "61c", "61d", "61e", "61f", "62a", "62b", "62c", "62d", "62e", "62f", "63a", "63b", "63c", "63d", "63e", "63f", "64a", "64b", "64c", "64d", "64e", "64f", "65a", "65b", "65c", "65d", "65e", "65f", "66a", "66b", "66c", "66d", "66e", "66f", "67a", "67b", "67c", "67d", "67e", "67f", "68a", "68b", "68c", "68d", "68e", "68f", "69a", "69b", "69c", "69d", "69e", "69f", "70a", "70b", "70c", "70d", "70e", "70f", "71a", "71b", "71c", "71d", "71e", "71f", "72a", "72b", "72c", "72d", "72e", "72f", "73a", "73b", "73c", "73d", "73e", "73f", "74a", "74b", "74c", "74d", "74e"]
}))
plutarch.addWork(utils.TextSpec("Quomodo quis suos in virtute sentiat profectus", "2008.01.0152", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["75b", "75c", "75d", "75e", "75f", "76a", "76b", "76c", "76d", "76e", "76f", "77a", "77b", "77c", "77d", "77e", "77f", "78a", "78b", "78c", "78d", "78e", "78f", "79a", "79b", "79c", "79d", "79e", "79f", "80a", "80b", "80c", "80d", "80e", "80f", "81a", "81b", "81c", "81d", "81e", "81f", "82a", "82b", "82c", "82d", "82e", "82f", "83a", "83b", "83c", "83d", "83e", "83f", "84a", "84b", "84c", "84d", "84e", "84f", "85a", "85b", "85c", "85d", "85e", "85f", "86a"]
}))
plutarch.addWork(utils.TextSpec("An Recte Dictum Sit Latenter Esse Vivendum", "2008.01.0398", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["1128a", "1128b", "1128c", "1128d", "1128e", "1128f", "1129a", "1129b", "1129c", "1129d", "1129e", "1129f", "1130a", "1130b", "1130c", "1130d", "1130e"]
}))
plutarch.addWork(utils.TextSpec("Regum et imperatorum apophthegmata", "2008.01.0191", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["172b", "172c", "172d", "172e", "172f", "173a", "173b", "173c", "173d", "173e", "173f", "174a", "174b", "174c", "174d", "174e", "174f", "175a", "175b", "175c", "175d", "175e", "175f", "176a", "176b", "176c", "176d", "176e", "176f", "177a", "177b", "177c", "177d", "177e", "177f", "178a", "178b", "178c", "178d", "178e", "178f", "179a", "179b", "179c", "179d", "179e", "179f", "180a", "180b", "180c", "180d", "180e", "180f", "181a", "181b", "181c", "181d", "181e", "181f", "182a", "182b", "182c", "182d", "182e", "182f", "183a", "183b", "183c", "183d", "183e", "183f", "184a", "184b", "184c", "184d", "184e", "184f", "185a", "185b", "185c", "185d", "185e", "185f", "186a", "186b", "186c", "186d", "186e", "186f", "187a", "187b", "187c", "187d", "187e", "187f", "188a", "188b", "188c", "188d", "188e", "188f", "189a", "189b", "189c", "189d", "189e", "189f", "190a", "190b", "190c", "190d", "190e", "190f", "191a", "191b", "191c", "191d", "191e", "191f", "192a", "192b", "192c", "192d", "192e", "192f", "193a", "193b", "193c", "193d", "193e", "193f", "194a", "194b", "194c", "194d", "194e", "194f", "195a", "195b", "195c", "195d", "195e", "195f", "196a", "196b", "196c", "196d", "196e", "196f", "197a", "197b", "197c", "197d", "197e", "197f", "198a", "198b", "198c", "198d", "198e", "198f", "199a", "199b", "199c", "199d", "199e", "199f", "200a", "200b", "200c", "200d", "200e", "200f", "201a", "201b", "201c", "201d", "201e", "201f", "202a", "202b", "202c", "202d", "202e", "202f", "203a", "203b", "203c", "203d", "203e", "203f", "204a", "204b", "204c", "204d", "204e", "204f", "205a", "205b", "205c", "205d", "205e", "205f", "206a", "206b", "206c", "206d", "206e", "206f", "207a", "207b", "207c", "207d", "207e", "207f", "208a"]
}))
plutarch.addWork(utils.TextSpec("Romulus", "2008.01.0079", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29"]
}))
plutarch.addWork(utils.TextSpec("An seni respublica gerenda sit", "2008.01.0328", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["783b", "783c", "783d", "783e", "783f", "784a", "784b", "784c", "784d", "784e", "784f", "785a", "785b", "785c", "785d", "785e", "785f", "786a", "786b", "786c", "786d", "786e", "786f", "787a", "787b", "787c", "787d", "787e", "787f", "788a", "788b", "788c", "788d", "788e", "788f", "789a", "789b", "789c", "789d", "789e", "789f", "790a", "790b", "790c", "790d", "790e", "790f", "791a", "791b", "791c", "791d", "791e", "791f", "792a", "792b", "792c", "792d", "792e", "792f", "793a", "793b", "793c", "793d", "793e", "793f", "794a", "794b", "794c", "794d", "794e", "794f", "795a", "795b", "795c", "795d", "795e", "795f", "796a", "796b", "796c", "796d", "796e", "796f", "797a", "797b", "797c", "797d", "797e", "797f"]
}))
plutarch.addWork(utils.TextSpec("Septem sapientium convivium", "2008.01.0184", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["146b", "146c", "146d", "146e", "146f", "147a", "147b", "147c", "147d", "147e", "147f", "148a", "148b", "148c", "148d", "148e", "148f", "149a", "149b", "149c", "149d", "149e", "149f", "150a", "150b", "150c", "150d", "150e", "150f", "151a", "151b", "151c", "151d", "151e", "151f", "152a", "152b", "152c", "152d", "152e", "152f", "153a", "153b", "153c", "153d", "153e", "153f", "154a", "154b", "154c", "154d", "154e", "154f", "155a", "155b", "155c", "155d", "155e", "155f", "156a", "156b", "156c", "156d", "156e", "156f", "157a", "157b", "157c", "157d", "157e", "157f", "158a", "158b", "158c", "158d", "158e", "158f", "159a", "159b", "159c", "159d", "159e", "159f", "160a", "160b", "160c", "160d", "160e", "160f", "161a", "161b", "161c", "161d", "161e", "161f", "162a", "162b", "162c", "162d", "162e", "162f", "163a", "163b", "163c", "163d", "163e", "163f", "164a", "164b", "164c", "164d"]
}))
plutarch.addWork(utils.TextSpec("Sertorius", "2008.01.0125", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27"]
}))
plutarch.addWork(utils.TextSpec("Solon", "2008.01.0073", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32"]
}))
plutarch.addWork(utils.TextSpec("Sulla", "2008.01.0126", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38"]
}))
plutarch.addWork(utils.TextSpec("Themistocles", "2008.01.0074", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32"]
}))
plutarch.addWork(utils.TextSpec("Theseus", "2008.01.0075", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36"]
}))
plutarch.addWork(utils.TextSpec("Tiberius Gracchus", "2008.01.0127", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"]
}))
plutarch.addWork(utils.TextSpec("Timoleon", "2008.01.0128", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39"]
}))
plutarch.addWork(utils.TextSpec("Titus Flamininus", "2008.01.0115", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"]
}))
plutarch.addWork(utils.TextSpec("An virtus doceri possit", "2008.01.0254", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["439a", "439b", "439c", "439d", "439e", "439f", "440a", "440b", "440c"]
}))
plutarch.addWork(utils.TextSpec("Vitae decem oratorum", "2008.01.0344", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["832b", "832c", "832d", "832e", "832f", "833a", "833b", "833c", "833d", "833e", "833f", "834a", "834b", "834c", "834d", "834e", "834f", "835a", "835b", "835c", "835d", "835e", "835f", "836a", "836b", "836c", "836d", "836e", "836f", "837a", "837b", "837c", "837d", "837e", "837f", "838a", "838b", "838c", "838d", "838e", "838f", "839a", "839b", "839c", "839d", "839f", "840a", "840b", "840c", "840d", "840e", "840f", "841a", "841b", "841c", "841d", "841e", "841f", "842a", "842b", "842c", "842d", "842e", "842f", "843a", "843b", "843c", "843d", "843e", "843f", "844a", "844b", "844c", "844d", "844e", "844f", "845a", "845b", "845c", "845d", "845e", "845f", "846a", "846b", "846c", "846d", "846e", "846f", "847a", "847b", "847c", "847d", "847e", "847f", "848a", "848b", "848c", "848d", "848e", "848f", "849a", "849b", "849c", "849d", "849e", "849f", "850a", "850b", "850c", "850d", "850e", "850f", "851a", "851b", "851c", "851d", "851e", "851f", "852a", "852b", "852c", "852d", "852e"]
}))
plutarch.addWork(utils.TextSpec("An vitiositas ad infelicitatem sufficia", "2008.01.0278", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["498a", "498b", "498c", "498d", "498e", "498f", "499a", "499b", "499c", "499d", "499e", "499f", "500a"]
}))
authors.append(plutarch)

polybius = utils.Author("Polybius")
polybius.addWork(utils.TextSpec("Histories", "1999.01.0233", 39, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(polybius)

procopius = utils.Author("Procopius")
procopius.addWork(utils.TextSpec("De Bellis", "2008.01.0670", 8, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
procopius.addWork(utils.TextSpec("Historia Arcana", "2008.01.0669", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 30+1)
}))
authors.append(procopius)

pseudoPlutarch = utils.Author("PseudoPlutarch")
pseudoPlutarch.addWork(utils.TextSpec("De Musica", "2008.01.0401", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["1131b", "1131c", "1131d", "1131e", "1131f", "1132a", "1132b", "1132c", "1132d", "1132e", "1132f", "1133a", "1133b", "1133c", "1133d", "1133e", "1133f", "1134a", "1134b", "1134c", "1134d", "1134e", "1134f", "1135a", "1135b", "1135c", "1135d", "1135e", "1135f", "1136a", "1136b", "1136c", "1136d", "1136e", "1136f", "1137a", "1137b", "1137c", "1137d", "1137e", "1137f", "1138a", "1138b", "1138c", "1138d", "1138e", "1138f", "1139a", "1139b", "1139c", "1139d", "1139e", "1139f", "1140a", "1140b", "1140c", "1140d", "1140e", "1140f", "1141a", "1141b", "1141c", "1141d", "1141e", "1141f", "1142a", "1142b", "1142c", "1142d", "1142e", "1142f", "1143a", "1143b", "1143c", "1143d", "1143e", "1143f", "1144a", "1144b", "1144c", "1144d", "1144e", "1144f", "1145a", "1145b", "1145c", "1145d", "1145e", "1145f", "1146a", "1146b", "1146c", "1146d", "1146e", "1146f", "1147a"]
}))
pseudoPlutarch.addWork(utils.TextSpec("Placita Philosophorum", "2008.01.0403", 1, "%3Astephpage%3D", {
    "multi": False,
    "suffixes": ["874d", "874e", "874f", "875a", "875b", "875c", "875d", "875e", "875f", "876a", "876b", "876c", "876d", "876e", "876f", "877a", "877b", "877c", "877d", "877e", "877f", "878a", "878b", "878c", "878d", "878e", "878f", "879a", "879b", "879c", "879d", "879e", "879f", "880a", "880b", "880c", "880d", "880e", "880f", "881a", "881b", "881c", "881d", "881e", "881f", "882a", "882b", "882c", "882d", "882e", "882f", "883a", "883b", "883c", "883d", "883e", "883f", "884a", "884b", "884c", "884d", "884e", "884f", "885a", "885b", "885c", "885d", "886b", "886c", "886d", "886e", "886f", "887a", "887b", "887c", "887d", "887e", "887f", "888a", "888b", "888c", "888d", "888e", "888f", "889a", "889b", "889c", "889d", "889e", "889f", "890a", "890b", "890c", "890d", "890e", "890f", "891a", "891b", "891c", "891d", "891e", "891f", "892a", "892b", "892c", "892d", "892e", "892f", "893a", "893b", "893c", "893d", "893e", "893f", "894a", "894b", "894c", "894d", "894e", "894f", "895a", "895b", "895c", "895d", "895e", "895f", "896a", "896b", "896c", "896d", "896e", "896f", "897a", "897b", "897c", "897d", "897e", "897f", "898a", "898b", "898c", "898d", "898e", "898f", "899a", "899b", "899c", "899d", "899e", "899f", "900a", "900b", "900c", "900d", "900e", "900f", "901a", "901b", "901c", "901d", "901e", "901f", "902a", "902b", "902c", "902d", "902e", "902f", "903a", "903b", "903c", "903d", "903e", "903f", "904a", "904b", "904c", "904d", "904e", "904f", "905a", "905b", "905c", "905d", "905e", "905f", "906a", "906b", "906c", "906d", "906e", "906f", "907a", "907b", "907c", "907d", "907e", "907f", "908a", "908b", "908c", "908d", "908e", "908f", "909a", "909b", "909c", "909d", "909e", "909f", "910a", "910b", "910c", "910d", "910e", "910f", "911a", "911b", "911c"]
}))
authors.append(pseudoPlutarch)

pseudoXenophon = utils.Author("PseudoXenophon")
pseudoXenophon.addWork(utils.TextSpec("Constituion of the Athenians", "1999.01.0157", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 3+1)
}))
authors.append(pseudoXenophon)

claudiusPtolemy = utils.Author("ClaudiusPtolemy")
claudiusPtolemy.addWork(utils.TextSpec("Tetrabiblos", "2008.01.0636", 4, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(claudiusPtolemy)

quintusSmyrnaeus = utils.Author("QuintusSmyrnaeus")
quintusSmyrnaeus.addWork(utils.TextSpec("Fall of Troy", "2008.01.0490", 14, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(quintusSmyrnaeus)

sophocles = utils.Author("Sophocles")
sophocles.addWork(utils.TextSpec("Ajax", "1999.01.0183", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "36", "74", "101", "134", "172", "182", "193", "201", "221", "231", "245", "257", "263", "284", "331", "348", "356", "364", "377", "379", "392", "394", "410", "412", "428", "430", "481", "525", "545", "583", "596", "609", "622", "635", "646", "693", "707", "719", "748", "784", "815", "866", "879", "915", "926", "961", "992", "1040", "1091", "1120", "1150", "1163", "1168", "1185", "1192", "1199", "1211", "1223", "1264", "1290", "1316", "1346", "1376"]
}))
sophocles.addWork(utils.TextSpec("Antigone", "1999.01.0185", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "39", "69", "100", "110", "117", "127", "134", "141", "148", "155", "162", "211", "237", "278", "315", "332", "343", "354", "365", "376", "384", "407", "441", "471", "499", "526", "531", "556", "583", "593", "605", "615", "626", "631", "681", "724", "758", "781", "791", "801", "806", "817", "823", "834", "839", "853", "858", "872", "876", "883", "929", "944", "955", "966", "977", "988", "1033", "1064", "1091", "1115", "1126", "1137", "1146", "1155", "1183", "1219", "1244", "1257", "1261", "1270", "1278", "1281", "1284", "1293", "1294", "1306", "1317", "1328", "1334", "1339", "1347"]
}))
sophocles.addWork(utils.TextSpec("Electra", "1999.01.0187", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "23", "51", "77", "86", "103", "121", "137", "154", "174", "193", "213", "233", "251", "282", "310", "341", "369", "385", "415", "431", "464", "472", "488", "504", "516", "552", "558", "610", "634", "660", "680", "731", "764", "788", "804", "823", "836", "849", "860", "871", "892", "920", "947", "990", "1015", "1050", "1058", "1070", "1082", "1090", "1098", "1126", "1160", "1171", "1200", "1232", "1253", "1273", "1288", "1322", "1339", "1354", "1372", "1384", "1391", "1398", "1422", "1442", "1466", "1491", "1508"]
}))
sophocles.addWork(utils.TextSpec("Ichneutae", "1999.01.0220", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "64", "79", "100", "124", "145", "176", "203", "221", "243", "251", "290", "298", "329", "338", "352", "371", "378"]
}))
sophocles.addWork(utils.TextSpec("Oedipus at Colonus", "1999.01.0189", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "33", "75", "118", "149", "176", "192", "207", "254", "296", "337", "385", "421", "461", "510", "521", "534", "542", "549", "579", "607", "642", "668", "681", "694", "707", "720", "761", "800", "848", "897", "939", "960", "1014", "1044", "1059", "1074", "1085", "1099", "1139", "1181", "1211", "1225", "1239", "1249", "1284", "1346", "1397", "1431", "1448", "1463", "1477", "1491", "1500", "1556", "1568", "1579", "1620", "1670", "1699", "1723", "1737", "1751"]
}))
sophocles.addWork(utils.TextSpec("Oedipus Tyrannus", "1999.01.0191", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "14", "58", "78", "102", "132", "151", "159", "169", "179", "190", "203", "216", "255", "276", "300", "330", "354", "380", "408", "429", "447", "463", "473", "483", "496", "513", "543", "583", "616", "634", "649", "660", "679", "700", "726", "750", "771", "800", "834", "863", "873", "884", "897", "911", "950", "977", "1000", "1026", "1054", "1086", "1098", "1110", "1141", "1171", "1186", "1196", "1204", "1212", "1223", "1237", "1285", "1297", "1313", "1321", "1329", "1349", "1367", "1416", "1446", "1478", "1516"]
}))
sophocles.addWork(utils.TextSpec("Philoctetes", "1999.01.0193", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "26", "54", "86", "123", "135", "144", "150", "159", "169", "180", "191", "201", "210", "219", "255", "285", "317", "343", "391", "403", "441", "468", "507", "519", "557", "591", "628", "676", "691", "707", "718", "730", "782", "806", "827", "839", "843", "855", "865", "893", "927", "963", "1004", "1045", "1081", "1101", "1123", "1146", "1170", "1218", "1258", "1288", "1314", "1348", "1380", "1402", "1408", "1445"]
}))
sophocles.addWork(utils.TextSpec("Trachiniae", "1999.01.0195", 1, "%3Acard%3D", {
    "multi": False,
    "suffixes": ["1", "49", "61", "79", "94", "103", "112", "122", "132", "141", "180", "pos", "205", "225", "248", "270", "291", "314", "335", "351", "375", "393", "436", "470", "497", "507", "517", "531", "588", "600", "620", "633", "640", "647", "655", "663", "672", "705", "723", "749", "783", "813", "821", "831", "841", "852", "863", "896", "947", "950", "953", "965", "972", "1004", "1017", "1024", "1044", "1076", "1112", "1143", "1157", "1179", "1203", "1221", "1230", "1259"]
}))
authors.append(sophocles)

strabo = utils.Author("Strabo")
strabo.addWork(utils.TextSpec("Geography", "1999.01.0197", 17, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(strabo)

theocritus = utils.Author("Theocritus")
theocritus.addWork(utils.TextSpec("Idylls", "1999.01.0228", 1, "%3Atext%3DId.%3Apoem%3D", {
    "multi": False,
    "suffixes": range(1, 30+1)
}))
theocritus.addWork(utils.TextSpec("Epigrams", "1999.01.0228", 1, "%3Atext%3DEp.%3Apoem%3D", {
    "multi": False,
    "suffixes": range(1, 24+1)
}))
theocritus.addWork(utils.TextSpec("Epigrams", "1999.01.0228", 1, "%3Atext%3DEp.%3Apoem%3D", {
    "multi": False,
    "suffixes": range(1, 24+1)
}))
authors.append(theocritus)

theophrastus = utils.Author("Theophrastus")
theophrastus.addWork(utils.TextSpec("Characters", "1999.01.0225", 1, "%3Achapter%3D", {
    "multi": False,
    "suffixes": range(1, 30+1)
}))
authors.append(theophrastus)

thucydides = utils.Author("Thucydides")
thucydides.addWork(utils.TextSpec("The Peloponnesian War", "1999.01.0199", 8, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(thucydides)

tryphiodorus = utils.Author("Tryphiodorus")
tryphiodorus.addWork(utils.TextSpec("The Taking of Ilios", "2008.01.0491", 1, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(tryphiodorus)

xenophonOfEphesus = utils.Author("XenophonOfEphesus")
xenophonOfEphesus.addWork(utils.TextSpec("Ephesiaca", "2008.01.0649", 5, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
authors.append(xenophonOfEphesus)

xenophon = utils.Author("Xenophon")
xenophon.addWork(utils.TextSpec("Anabasis", "1999.01.0201", 7, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
xenophon.addWork(utils.TextSpec("Cyropaedia", "1999.01.0203", 8, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
xenophon.addWork(utils.TextSpec("Hellenica", "1999.01.0205", 7, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
xenophon.addWork(utils.TextSpec("Memorabilia", "1999.01.0207", 4, "%3Abook%3D", {
    "multi": False,
    "suffixes": []
}))
xenophon.addWork(utils.TextSpec("Agesilaus", "1999.01.0209", 1, "%3Atext%3DAges.%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
}))
xenophon.addWork(utils.TextSpec("On the Cavalry Commander", "1999.01.0209", 1, "%3Atext%3DCav.%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
}))
xenophon.addWork(utils.TextSpec("Constitution of the Lacedaimonians", "1999.01.0209", 1, "%3Atext%3DConst.+Lac.%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
}))
xenophon.addWork(utils.TextSpec("Hiero", "1999.01.0209", 1, "%3Atext%3DHiero%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
}))
xenophon.addWork(utils.TextSpec("On the Art of Horsemanship", "1999.01.0209", 1, "%3Atext%3DHorse.%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
}))
xenophon.addWork(utils.TextSpec("On Hunting", "1999.01.0209", 1, "%3Atext%3DHunt.%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
}))
xenophon.addWork(utils.TextSpec("Ways and Means", "1999.01.0209", 1, "%3Atext%3DWays%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6"]
}))
xenophon.addWork(utils.TextSpec("Apology", "1999.01.0211", 1, "%3Atext%3DApol.%3Asection%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34"]
}))
xenophon.addWork(utils.TextSpec("Economics", "1999.01.0211", 1, "%3Atext%3DEc.%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"]
}))
xenophon.addWork(utils.TextSpec("Symposium", "1999.01.0211", 1, "%3Atext%3DSym.%3Achapter%3D", {
    "multi": False,
    "suffixes": ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
}))
authors.append(xenophon)
