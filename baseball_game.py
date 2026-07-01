from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == "+":
                last = record.pop()
                prev_last = record.pop()
                res = int(prev_last) + int(last)
                record.append(prev_last)
                record.append(last)
                record.append(res)
            elif op == "D":
                last = record.pop()
                res = int(last) * 2
                record.append(last)
                record.append(res)
            elif op == "C":
                last = record.pop()
            else:
                record.append(op)

        return sum(int(char) for char in record)
