from insertSyllables import *


def process_word(word):
    word_length = len(word)

    start = 0
    end = 1

    transliterated_word = ""
    buffer = ""

    while end <= word_length:
        word_segment = word[start:end]

        if trieObject.search(word_segment):
            buffer = trieObject.return_map(word_segment)
            end = end + 1
        else:
            start = end - 1
            transliterated_word += buffer

    transliterated_word += buffer

    return transliterated_word


inputWord = input("Enter word: ")
