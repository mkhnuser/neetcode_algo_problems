import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        char_to_count_mapping = {}

        for char in s:
            if char not in char_to_count_mapping:
                char_to_count_mapping[char] = 0
            char_to_count_mapping[char] += 1

        max_heap = []
        for char, count in char_to_count_mapping.items():
            # NOTE: Initially, count >= 1.
            heapq.heappush(max_heap, (-count, char))

        output = []

        while max_heap:
            max_element = heapq.heappop(max_heap)
            count, char = max_element
            count = -count

            if output and char == output[-1]:
                on_hold = (-count, char)

                if not max_heap:
                    return ""

                max_element = heapq.heappop(max_heap)
                count, char = max_element
                count = -count

                heapq.heappush(max_heap, on_hold)

            output.append(char)
            count -= 1
            if count > 0:
                heapq.heappush(max_heap, (-count, char))

        string_repr = "".join(output)
        return string_repr


def test():
    sol = Solution()
    print(sol.reorganizeString("aaabb"))
    sol = Solution()
    print(sol.reorganizeString("aaabc"))


if __name__ == "__main__":
    test()
