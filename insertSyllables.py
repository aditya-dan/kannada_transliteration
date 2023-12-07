from trie import *
from symbolMaps import *

trieObject = Trie()


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
