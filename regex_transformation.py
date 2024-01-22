import re

consonant = "[bcdfghjklmnprstvwyz]"

regexTransformationMap = {
    "aa": "aa?",
    "ii": "ii?|ee",
    "uu": "uu?|oo",
    "R": "ru",
    "e": "e|^ye",
    "ee": "e|^ye",
    "o": "o|^wo",
    "oo": "o|^wo",
    "ai": "ai|y",
    "au": "ai|ow",
    "M": "[nm]",
    "H": "ha?"
}

inputWord = input("Enter word: ")

for normalisedForm in regexTransformationMap:
    regex = regexTransformationMap[normalisedForm]
    if re.search(regex, normalisedForm):
        normalisedInput = re.sub(regex, normalisedForm, inputWord)
        print(normalisedInput)
