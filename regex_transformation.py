import re

consonant = "[bcdfghjklmnprstvwyz]"
vowel = "[aeiou]"

regexTransformationMap = {
    "aa": f"((?<={consonant})|^)aa?(?={consonant}|$)",
    "ii": f"((?<={consonant})|^)(ii?|ee)(?={consonant}|$)",
    "uu": f"((?<={consonant})|^)(uu?|oo)(?={consonant}|$)",
    "R": f"((?<={consonant})|^)ru(?={consonant}|$)",
    "e": f"(((?<={consonant})|^)e|^ye)(?={consonant}|$)",
    "ee": f"(((?<={consonant})|^)e|^ye)(?={consonant}|$)",
    "o": f"(((?<={consonant})|^)o|^wo)(?={consonant}|$)",
    "oo": f"(((?<={consonant})|^)o|^wo)(?={consonant}|$)",
    "ai": f"(((?<={consonant})|^)ai|(?<={consonant})y)(?={consonant}|$)",
    "au": f"(((?<={consonant})|^)au|(?<={consonant})ow)(?={consonant}|$)",
    "M": f"(?<={vowel})[nm](?={consonant}|$)",
    "H": f"(?<={vowel})ha?(?={consonant}|$)"
}

inputWord = input("Enter word: ")

for normalisedForm in regexTransformationMap:
    regex = regexTransformationMap[normalisedForm]
    search_result = re.search(regex, inputWord)
    if search_result:
        print(normalisedForm + ": " + str(search_result))
