from trieNode import *


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
        pointer = 0

        while pointer < length:
            character = word[pointer]
            if character not in current.children:
                print(current.mapping, end="")
                self.process(word[pointer:])
                return
            current = current.children[character]
            pointer += 1
        print(current.mapping)
