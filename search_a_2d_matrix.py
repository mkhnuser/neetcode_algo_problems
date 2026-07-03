from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_column_values = [row[0] for row in matrix]
        lower_row_index = self.first_lower_index(first_column_values, target)
        upper_row_index = self.first_upper_index(first_column_values, target)

        lower_res = self.bin_search(matrix[lower_row_index], target)
        upper_res = self.bin_search(matrix[upper_row_index], target)
        return (lower_res != -1) or (upper_res != -1)

    def bin_search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            middle_index = (L + R) // 2
            current = nums[middle_index]
            if current == target:
                return middle_index
            elif current > target:
                R = middle_index - 1
            else:
                L = middle_index + 1

        return -1

    def first_lower_index(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        output = -1

        while L <= R:
            middle_index = (L + R) // 2
            current = nums[middle_index]

            if current >= target:
                R = middle_index - 1
            else:
                output = middle_index
                L = middle_index + 1

        return output

    def first_upper_index(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        output = -1

        while L <= R:
            middle_index = (L + R) // 2
            current = nums[middle_index]

            if current >= target:
                output = middle_index
                R = middle_index - 1
            else:
                L = middle_index + 1

        return output


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        r = 0
        c = m - 1

        while r < n and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r += 1
            else:
                # NOTE: matrix[r][c] > target.
                c -= 1

        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        top = 0
        bot = n - 1

        while top <= bot:
            middle_index = (top + bot) // 2
            row = matrix[middle_index]

            if target > row[-1]:
                # NOTE: Go down.
                top = middle_index + 1
            elif target < row[0]:
                # NOTE: Go up.
                bot = middle_index - 1
            else:
                # NOTE: The appropriate row has been found.
                break

        if top > bot:
            return False

        row = matrix[(top + bot) // 2]
        L = 0
        R = m - 1

        while L <= R:
            middle_index = (L + R) // 2
            middle_value = row[middle_index]
            if middle_value == target:
                return True
            elif middle_value < target:
                L = middle_index + 1
            else:
                R = middle_index - 1

        return False
