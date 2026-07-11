from collections import defaultdict
from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.components = n

    def find(self, x: int) -> int:
        p = x
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, x: int, y: int) -> bool:
        root_one = self.find(x)
        root_two = self.find(y)

        if root_one == root_two:
            return False

        if self.rank[root_one] > self.rank[root_two]:
            self.parent[root_two] = root_one
        elif self.rank[root_two] > self.rank[root_one]:
            self.parent[root_one] = root_two
        else:
            self.parent[root_two] = root_one
            self.rank[root_one] += 1

        self.components -= 1
        return True

    def get_the_number_of_components(self) -> int:
        return self.components

    def are_in_the_same_component(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


# NOTE: The first attempt.
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsu = DSU(n)

        for i in range(len(accounts)):
            for j in range(i + 1, len(accounts)):
                acc_one = accounts[i]
                acc_two = accounts[j]

                name_one, emails_one = acc_one[0], set(acc_one[1:])
                name_two, emails_two = acc_two[0], set(acc_two[1:])

                if emails_one.intersection(emails_two):
                    dsu.union(i, j)

        merged_accounts = [[] for _ in range(n)]

        for i in range(len(accounts)):
            representative_index = dsu.find(i)
            merged_accounts[representative_index].append(accounts[i])

        merged_accounts = [acc for acc in merged_accounts if acc]

        output = []

        for account_group in merged_accounts:
            t = []
            emails = set()

            for acc in account_group:
                acc_name = acc[0]
                acc_emails = set(acc[1:])

                if not t:
                    t.append(acc_name)

                emails.update(acc_emails)

            emails = sorted(list(emails))
            t[1:] = emails
            output.append(t)

        return output


# NOTE: The second, a more clean, version.
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsu = DSU(n)
        email_to_acc_mapping = {}

        # NOTE: Given account ids, union them if they have common emails.
        for i, acc in enumerate(accounts):
            for e in acc[1:]:
                if e not in email_to_acc_mapping:
                    email_to_acc_mapping[e] = i
                else:
                    dsu.union(i, email_to_acc_mapping[e])

        # NOTE: Create an account id -> emails mapping.
        email_group = defaultdict(list)
        for e, a in email_to_acc_mapping.items():
            representative = dsu.find(a)
            email_group[representative].append(e)

        # NOTE: Prepare the output.
        output = []
        for i, emails in email_group.items():
            name = accounts[i][0]
            output.append([name] + sorted(emails))

        return output


def test() -> None:
    accounts = [
        ["neet", "neet@gmail.com", "neet_dsa@gmail.com"],
        ["alice", "alice@gmail.com"],
        ["neet", "bob@gmail.com", "neet@gmail.com"],
        ["neet", "neetcode@gmail.com"],
    ]
    sol = Solution()
    print(sol.accountsMerge(accounts))

    accounts = [["James", "james@mail.com"], ["James", "james@mail.co"]]
    sol = Solution()
    print(sol.accountsMerge(accounts))


if __name__ == "__main__":
    test()
