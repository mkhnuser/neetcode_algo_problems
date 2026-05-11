from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [None] * n
        for i in range(n):
            res = 1
            for j in range(n):
                if j == i:
                    continue
                res *= nums[j]
            output[i] = res
        return output


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # NOTE: 0 is the problem, it has always been.
        n = len(nums)
        output = [0] * n

        zero_counter = 0
        for num in nums:
            if num == 0:
                zero_counter += 1

        if zero_counter >= 2:
            return output

        # NOTE: At this point, there is zero or one zeros.

        all_prod = 1
        for num in nums:
            all_prod *= num

        all_prod_except_zero = 1
        for num in nums:
            if num != 0:
                all_prod_except_zero *= num

        for i in range(n):
            num = nums[i]
            if num != 0:
                output[i] = int(all_prod / num)
            else:
                # NOTE: OK, num == 0 at this point.
                # Since this zero is the only possible zero, just store the constant.
                output[i] = all_prod_except_zero

        return output


def test():
    sol = Solution()
    print(sol.productExceptSelf([1, 2, 4, 6]))
    print(sol.productExceptSelf([1, 0, 2, 1]))
    print(sol.productExceptSelf([0, 0]))
    print(sol.productExceptSelf([0, 8, 0]))
    print(sol.productExceptSelf([0, 8, 1]))


if __name__ == "__main__":
    test()
