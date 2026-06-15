class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        L = 0
        R = 0

        output_list = []
        while L < len(word1) and R < len(word2):
            output_list.append(word1[L])
            output_list.append(word2[R])
            L += 1
            R += 1

        while L < len(word1):
            output_list.append(word1[L])
            L += 1

        while R < len(word2):
            output_list.append(word2[R])
            R += 1

        return "".join(output_list)


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output_list = []
        n = len(word1)
        m = len(word2)

        for p in range(max(n, m)):
            if p < n:
                output_list.append(word1[p])
            if p < m:
                output_list.append(word2[p])

        return "".join(output_list)
