from collections import deque


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # NOTE: You can jump from `i` to `j` <=>
        # s[j] == '0' and `j` is within `i + minJump` and `i + maxJump`.
        # The question, can we reach `n - 1` starting from `0`?
        n = len(s)

        if s[n - 1] != "0":
            return False

        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]

            L = i + minJump
            R = i + maxJump + 1

            for j in range(L, R):
                if j > n - 1:
                    return False

                if j == n - 1:
                    return True

                if s[j] == "0":
                    if dfs(j):
                        return True

            cache[i] = False
            return cache[i]

        return dfs(0)


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        farthest = 0

        while q:
            i = q.popleft()
            start = max(i + minJump, farthest + 1)
            for j in range(start, min(i + maxJump + 1, len(s))):
                if s[j] == "0":
                    q.append(j)
                    if j == len(s) - 1:
                        return True
            farthest = i + maxJump

        return False


def test():
    s = "00110010"
    minJump = 2
    maxJump = 4
    sol = Solution()
    print(sol.canReach(s, minJump, maxJump))

    s = "0010"
    minJump = 1
    maxJump = 1
    sol = Solution()
    print(sol.canReach(s, minJump, maxJump))

    s = "0100000000"
    minJump = 2
    maxJump = 8
    sol = Solution()
    print(sol.canReach(s, minJump, maxJump))


if __name__ == "__main__":
    test()
