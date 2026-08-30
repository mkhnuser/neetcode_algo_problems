class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        n = len(num1)
        m = len(num2)
        res = [0] * (n + m)
        num1, num2 = num1[::-1], num2[::-1]

        for i in range(n):
            for j in range(m):
                multiplication_result = int(num1[i]) * int(num2[j])
                res[i + j] += multiplication_result
                res[i + j + 1] += res[i + j] // 10
                res[i + j] = res[i + j] % 10

        res.reverse()
        beg = 0

        while beg < len(res):
            if res[beg] != 0:
                break
            beg += 1

        res = map(str, res[beg:])
        return "".join(res)
