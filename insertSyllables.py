from trie import *

trieObject = Trie()

onsetMap = {"k": "ಕ", "kh": "ಖ", "g": "ಗ", "gh": "ಘ", "c": "ಚ", "ch": "ಛ", "j": "ಜ", "jh": "ಝ", "jn": "ಜ್ಞ", "T": "ಟ",
            "Th": "ಠ", "D": "ಡ", "Dh": "ಢ", "N": "ಣ", "t": "ತ", "th": "ಥ", "d": "ದ", "dh": "ಧ", "n": "ನ", "p": "ಪ",
            "ph": "ಫ", "b": "ಬ", "bh": "ಭ", "m": "ಮ", "y": "ಯ", "r": "ರ", "l": "ಲ", "v": "ವ", "sh": "ಶ", "S": "ಷ",
            "s": "ಸ", "h": "ಹ", "L": "ಳ"}

vowelDiacriticMap = {"aa": "ಾ", "i": "ಿ", "ii": "ೀ", "u": "ು", "uu": "ೂ", "R": "ೃ", "e": "ೆ", "ee": "ೇ", "o": "ೊ",
                     "oo": "ೋ", "ai": "ೈ", "au": "ೌ"}

vowelMap = {"a": "ಅ", "aa": "ಆ", "i": "ಇ", "ii": "ಈ", "u": "ಉ", "uu": "ಊ", "R": "ಋ", "e": "ಎ", "ee": "ಏ", "o": "ಒ",
            "oo": "ಓ", "ai": "ಐ", "au": "ಔ"}

codaMap = {"M": "ಂ", "H": "ಃ"}


def construct_syllable_map(onset_map, vowel_map):
    syllable_map = {}

    for onset in onset_map:
        for vowel in vowel_map:
            syllable = onset + vowel
            syllable_map[syllable] = onset_map[onset] + vowel_map[vowel]
        syllable_map[onset + "a"] = onset_map[onset]

    return syllable_map


def construct_dead_consonant_map(onset_map):
    dead_consonant_map = {}

    for onset in onset_map:
        dead_consonant = onset_map[onset] + "್"
        dead_consonant_map[onset] = dead_consonant

    return dead_consonant_map


syllableMap = construct_syllable_map(onsetMap, vowelDiacriticMap)

deadConsonantMap = construct_dead_consonant_map(onsetMap)

for insertableSyllable in syllableMap:
    trieObject.insert(insertableSyllable, syllableMap[insertableSyllable])

for insertableDeadConsonant in deadConsonantMap:
    trieObject.insert(insertableDeadConsonant, deadConsonantMap[insertableDeadConsonant])

for insertableVowel in vowelMap:
    trieObject.insert(insertableVowel, vowelMap[insertableVowel])

for insertableCoda in codaMap:
    trieObject.insert(insertableCoda, codaMap[insertableCoda])
