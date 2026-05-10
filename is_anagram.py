class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # NOTE: The two strings are anagrams if:
        # They have the same characters;
        # Character count is the same.
        s_mapping = {}
        t_mapping = {}

        for char in s:
            if char not in s_mapping:
                s_mapping[char] = 0
            s_mapping[char] += 1

        for char in t:
            if char not in t_mapping:
                t_mapping[char] = 0
            t_mapping[char] += 1

        return s_mapping == t_mapping


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # NOTE: The two strings are anagrams if:
        # They have the same characters;
        # Character count is the same.
        if len(s) != len(t):
            return False

        s_mapping = {}
        t_mapping = {}

        for i in range(len(s)):
            s_mapping[s[i]] = s_mapping.get(s[i], 0) + 1
            t_mapping[t[i]] = t_mapping.get(t[i], 0) + 1

        return s_mapping == t_mapping


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # NOTE: The key space is of size 26.
        if len(s) != len(t):
            return False

        counter = [0] * 26
        for i in range(len(s)):
            counter[ord(s[i]) - ord("a")] += 1
            counter[ord(t[i]) - ord("a")] -= 1

        return all(count == 0 for count in counter)
