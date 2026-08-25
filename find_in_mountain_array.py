class MountainArray:
    def get(self, index: int) -> int:
        pass

    def length(self) -> int:
        pass


class Solution:
    def findInMountainArray(self, target: int, mountainArr: "MountainArray") -> int:
        length = mountainArr.length()

        # Find Peak
        L, R = 1, length - 2
        while L <= R:
            m = (L + R) // 2
            left, mid, right = (
                mountainArr.get(m - 1),
                mountainArr.get(m),
                mountainArr.get(m + 1),
            )
            if left < mid < right:
                L = m + 1
            elif left > mid > right:
                R = m - 1
            else:
                break

        peak = m

        # Search left portion
        L, R = 0, peak - 1
        while L <= R:
            m = (L + R) // 2
            val = mountainArr.get(m)
            if val < target:
                L = m + 1
            elif val > target:
                R = m - 1
            else:
                return m

        # Search right portion
        L, R = peak, length - 1
        while L <= R:
            m = (L + R) // 2
            val = mountainArr.get(m)
            if val > target:
                L = m + 1
            elif val < target:
                R = m - 1
            else:
                return m

        return -1
