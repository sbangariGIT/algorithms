class Solution:
    def simplifyPath(self, path: str) -> str:
        abs_path = []
        directories = path.split("/")
        for d in directories:
            if d == ".." and len(abs_path) != 0:
                abs_path.pop()
                continue
            if d == "." or d == ".." or d == "":
                continue
            abs_path.append(d)

        if len(abs_path) == 0:
            return '/'

        path = '/'
        for i in range(len(abs_path) - 1):
            path += abs_path[i] + '/'
        path += abs_path[-1]
        return path
