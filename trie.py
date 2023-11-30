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

    def search(self, word: str) -> bool:
        current = self.root

        for character in word:
            if character not in current.children:
                return False
            current = current.children[character]
        return current.isLeaf

    def starts_with(self, prefix: str) -> bool:
        current = self.root

        for character in prefix:
            if character not in current.children:
                return False
            current = current.children[character]
        return True

    def return_map(self, word: str) -> str:
        current = self.root

        for character in word:
            if character not in current.children:
                return ""
            current = current.children[character]
        return current.mapping
