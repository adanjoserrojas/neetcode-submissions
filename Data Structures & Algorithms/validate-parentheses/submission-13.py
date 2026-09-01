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
                # A closing bracket cannot appear without an opener
                if not stack:
                    return False

                opening = stack.pop()

                if opening != matching[ch]:
                    return False

        # Any remaining opening brackets are unmatched
        return len(stack) == 0