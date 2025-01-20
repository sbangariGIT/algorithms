class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        valid = [True] * len(s) 
        result = ""
        for i in range(len(s)):
            if s[i] == ")" and len(stack) == 0:
                valid[i] = False
            elif s[i] == ")":
                j = stack.pop()
                valid[j] = True
                valid[i] = True
            elif s[i] == "(":
                stack.append(i)
                valid[i] = False
            else:
                valid[i] = True
        for i in range(len(s)):
            if valid[i]:
                result += s[i]
        return result