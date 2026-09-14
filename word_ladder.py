import math
from typing import List, Mapping, cast


# NOTE: DFS solution is suboptimal for this problem: many redundant branches are explored.
# Instead, one should rely on BFS wave-like nature.


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        begin_word = beginWord
        end_word = endWord

        if end_word not in word_set:
            return 0

        adj_mapping = {
            w: self.within_distance_at_most_one(w, word_set)
            for w in {begin_word, end_word, *wordList}
        }
        visited = set()
        visited.add(begin_word)

        dfs_result = self.dfs(
            begin_word,
            end_word,
            adj_mapping,
            word_set,
            visited,
            0,
            float("+inf"),
        )

        if math.isinf(dfs_result):
            return 0

        return cast(int, dfs_result)

    def dfs(
        self,
        initial_word: str,
        end_word: str,
        adj_mapping: Mapping[str, set[str]],
        word_set: set[str],
        visited: set[str],
        current_depth: int,
        min_depth: float | int,
    ) -> int | float:
        if current_depth >= min_depth:
            # NOTE: There is no need to explore this dfs branch further since clearly min_depth won't be reduced.
            return min_depth

        if initial_word == end_word:
            return current_depth + 1

        hop_words = adj_mapping[initial_word]

        for hop_word in hop_words:
            if hop_word not in visited:
                visited.add(hop_word)
                min_depth = min(
                    self.dfs(
                        hop_word,
                        end_word,
                        adj_mapping,
                        word_set,
                        visited,
                        current_depth + 1,
                        min_depth,
                    ),
                    min_depth,
                )
                visited.remove(hop_word)

        return min_depth

    def within_distance_at_most_one(
        self,
        initial_word: str,
        word_set: set[str],
    ) -> set[str]:
        """Given `initial_word`, find all words which are within one hop from the `initial_word`."""
        output = set()

        for word in word_set:
            replace_counter = 0

            for a, b in zip(initial_word, word):
                if a != b:
                    replace_counter += 1

                if replace_counter >= 2:
                    # NOTE: The `initial_word` differs from `word` by at least two characters.
                    break
            else:
                output.add(word)

        return output


import math
from collections import deque
from typing import List, Mapping, cast


# NOTE: A BFS solution.


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        begin_word = beginWord
        end_word = endWord

        if end_word not in word_set:
            return 0

        bfs_result = self.bfs(
            begin_word,
            end_word,
            word_set,
        )

        if math.isinf(bfs_result):
            return 0

        return cast(int, bfs_result)

    def bfs(
        self,
        initial_word: str,
        end_word: str,
        word_set: set[str],
    ) -> int | float:
        visited = set()
        visited.add(initial_word)
        current_depth = 0
        d = deque()
        d.append((initial_word, current_depth))

        while d:
            for _ in range(len(d)):
                current_word, current_depth = d.popleft()
                current_depth += 1

                if current_word == end_word:
                    return current_depth

                hop_words = self.within_distance_at_most_one(current_word, word_set)

                for hop_word in hop_words:
                    if hop_word not in visited:
                        visited.add(hop_word)
                        d.append((hop_word, current_depth))

        return float("+inf")

    def within_distance_at_most_one(
        self,
        initial_word: str,
        word_set: set[str],
    ) -> set[str]:
        """Given `initial_word`, find all words which are within one hop from the `initial_word`."""
        output = set()

        for word in word_set:
            replace_counter = 0

            for a, b in zip(initial_word, word):
                if a != b:
                    replace_counter += 1

                if replace_counter >= 2:
                    # NOTE: The `initial_word` differs from `word` by at least two characters.
                    break
            else:
                output.add(word)

        return output


import math
from collections import deque
from typing import List, Mapping, cast


# NOTE: An optimized BFS solution.


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        begin_word = beginWord
        end_word = endWord

        if end_word not in word_set:
            return 0

        pattern_to_words: Mapping[str, set[str]] = {}
        word_set.add(begin_word)

        for w in word_set:
            for pattern in self.obtain_word_patterns(w):
                if pattern not in pattern_to_words:
                    pattern_to_words[pattern] = set()
                pattern_to_words[pattern].add(w)

        bfs_result = self.bfs(
            begin_word,
            end_word,
            pattern_to_words,
        )

        if math.isinf(bfs_result):
            return 0

        return cast(int, bfs_result)

    def bfs(
        self,
        initial_word: str,
        end_word: str,
        pattern_to_words: Mapping[str, set[str]],
    ) -> int | float:
        visited = set()
        visited.add(initial_word)
        current_depth = 1
        d = deque()
        d.append(initial_word)

        while d:
            for _ in range(len(d)):
                current_word = d.popleft()

                if current_word == end_word:
                    return current_depth

                current_word_patterns = self.obtain_word_patterns(current_word)

                for p in current_word_patterns:
                    for hop_word in pattern_to_words[p]:
                        if hop_word not in visited:
                            visited.add(hop_word)
                            d.append(hop_word)

            current_depth += 1

        return float("+inf")

    def obtain_word_patterns(self, word: str) -> set[str]:
        return {word[:i] + "*" + word[i + 1 :] for i in range(len(word))}


def test() -> None:
    sol = Solution()
    print(
        sol.ladderLength(
            beginWord="cat", endWord="sag", wordList=["bat", "bag", "sag", "dag", "dot"]
        )
    )

    sol = Solution()
    print(
        sol.ladderLength(
            beginWord="cat", endWord="sag", wordList=["bat", "bag", "sat", "dag", "dot"]
        )
    )


if __name__ == "__main__":
    test()
