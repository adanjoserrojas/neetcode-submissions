class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        matching = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack:
                    return False
                
                opening = stack.pop()

                if opening != matching[ch]:
                    return False
            
        if len(stack):
            return False
        
        return True
        