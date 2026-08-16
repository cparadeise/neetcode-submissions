class Solution:
    def isValid(self, s: str) -> bool:
        bracks = { '}': '{', ']': '[', ')': '(' }
        stack = []

        for char in s:
            if char in bracks:
                if stack and stack[-1] == bracks[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
            
        return True if not stack else False