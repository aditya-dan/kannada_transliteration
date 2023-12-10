from trieNode import *
from symbolMaps import latinCharacterSet


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, mapping: str) -> None:
        current = self.root

        for character in word:
            if character not in current.children:
                current.children[character] = TrieNode()
            current = current.children[character]
        current.isLeaf = True
        current.mapping = mapping

    def process(self, word: str):
        current = self.root
        length = len(word)

        for counter in range(0, length):
            character = word[counter]
            if character in current.children:
                current = current.children[character]
            else:
                print(current.mapping, end="")
                if character in latinCharacterSet:
                    self.process(word[counter:])
                else:
                    self.process(word[counter+1:])
                return
        print(current.mapping)
