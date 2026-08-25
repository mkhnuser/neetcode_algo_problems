import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counting_mapping = {}
        counting_mapping["a"] = a
        counting_mapping["b"] = b
        counting_mapping["c"] = c

        # NOTE: max heap of (counter, char).
        max_heap = []

        for item in counting_mapping.items():
            char, counter = item

            if counter == 0:
                continue

            heapq.heappush(max_heap, (-counter, char))

        output_string_list = []

        while max_heap:
            counter, char = heapq.heappop(max_heap)
            counter *= -1

            last_ones = output_string_list[-2:]

            if len(last_ones) >= 2 and last_ones[-2] == char and last_ones[-1] == char:
                if not max_heap:
                    break

                another_counter, another_char = heapq.heappop(max_heap)
                another_counter *= -1
                output_string_list.append(another_char)
                another_counter -= 1

                if another_counter != 0:
                    heapq.heappush(max_heap, (-another_counter, another_char))

                heapq.heappush(max_heap, (-counter, char))
            else:
                output_string_list.append(char)
                counter -= 1
                if counter != 0:
                    heapq.heappush(max_heap, (-counter, char))

        return "".join(output_string_list)


def test() -> None:
    sol = Solution()
    print(sol.longestDiverseString(3, 4, 2))
    sol = Solution()
    print(sol.longestDiverseString(0, 1, 5))


if __name__ == "__main__":
    test()
