class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        stack = []

        for char in path_list:
            if char == "":
                continue
            elif char == ".":
                continue
            elif char == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return "/" + "/".join(stack)


def test() -> None:
    path = "/neetcode/practice//...///../courses"
    sol = Solution()
    print(sol.simplifyPath(path))
    path = "/..//"
    sol = Solution()
    print(sol.simplifyPath(path))
    path = "/..//_home/a/b/..///"
    sol = Solution()
    print(sol.simplifyPath(path))


if __name__ == "__main__":
    test()
