from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mapping = {}

        for i, char in enumerate(s):
            mapping[char] = i

        partition_start = 0
        partition_end = -1
        output = []

        for i, char in enumerate(s):
            partition_end = max(partition_end, mapping[char])

            if i >= partition_end:
                output.append(partition_end - partition_start + 1)
                partition_start = i + 1
                partition_end = -1

        return output


def test() -> None:
    sol = Solution()
    print(sol.partitionLabels("xyxxyzbzbbisl"))
    sol = Solution()
    print(sol.partitionLabels("abcabc"))


if __name__ == "__main__":
    test()
