from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # NOTE: Assume a judge exists.
        # Then a unique number which satisfies properties 1, 2 exists.
        # 1. There are no arrows coming from this number.
        # 2. Everyone (but not the number) points to this number.

        if not trust:
            return -1

        output = []

        # NOTE: Uniqueness.
        # NOTE: Assume a pair is represented by (a, b).
        for potential_judge in range(1, n + 1):
            res = self.is_judge(trust, potential_judge)
            if res == -1:
                continue
            else:
                output.append(res)

        if len(output) != 1:
            return -1

        return output[0]

    def is_judge(self, trust: List[List[int]], potential_judge: int) -> int:
        # NOTE: Prop 1.
        for a, b in trust:
            if a == potential_judge:
                return -1

        # NOTE: Prop 2.
        trust_mapping: dict[int, set[int]] = {}

        for a, b in trust:
            if a not in trust_mapping:
                trust_mapping[a] = set()
            trust_mapping[a].add(b)

        for trust_set in trust_mapping.values():
            if potential_judge not in trust_set:
                return -1

        return potential_judge
