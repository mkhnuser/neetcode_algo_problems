from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0 for _ in range(n)]

        for i in range(n):
            counter = 1

            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    output[i] = counter
                    break

                counter += 1

        return output


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        output = [0 for _ in range(n)]

        for i in range(n):
            current_temp = temperatures[i]

            while stack and current_temp > stack[-1][0]:
                prev_temp_tuple = stack.pop()
                prev_temp, prev_index = prev_temp_tuple
                output[prev_index] = i - prev_index

            stack.append((current_temp, i))

        return output


def test():
    sol = Solution()
    temperatures = [30, 38, 30, 36, 35, 40, 28]
    print(sol.dailyTemperatures(temperatures))

    sol = Solution()
    temperatures = [22, 21, 20]
    print(sol.dailyTemperatures(temperatures))


if __name__ == "__main__":
    test()
