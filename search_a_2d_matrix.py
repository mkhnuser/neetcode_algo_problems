from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            for item in row:
                if item == target:
                    return True
        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            search_res = self.bin_search(row, target)
            if search_res != -1:
                return True
        return False

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
