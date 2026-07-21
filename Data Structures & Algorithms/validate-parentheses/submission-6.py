class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        dict = {"(" : ")", "{" : "}", "[" : "]"}

        for i in s:
            if i in dict:
                stack.append(i)
            else:
                if len(stack) < 1 or dict[stack[-1]] != i:
                    return False
                else:
                    stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False