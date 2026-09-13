from typing import MutableMapping


class TrieNode:
    def __init__(self) -> None:
        self.children: MutableMapping[str, "TrieNode"] = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.is_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        i = 0
        return self.recurse_search(cur, i, word)

    def recurse_search(self, cur: TrieNode, i: int, word: str) -> bool:
        for c in word:
            if c == ".":
                for child in cur.children:
                    if self.recurse_search(cur.children[child], 0, word[i + 1 :]):
                        return True

            if c not in cur.children:
                return False

            cur = cur.children[c]
            i += 1

        return cur.is_word


def test() -> None:
    word_dict = WordDictionary()
    word_dict.addWord("day")
    word_dict.addWord("bay")
    word_dict.addWord("may")
    word_dict.addWord("complex")
    print(word_dict.search("say"))
    print(word_dict.search("day"))
    print(word_dict.search(".ay"))
    print(word_dict.search("b.."))
    print(word_dict.search("c.mpl.x"))


if __name__ == "__main__":
    test()
