class Solution:
    def isValid(self, s: str) -> bool:

        combs = {
            "}":"{",
            "]":"[",
            ")":"("
        }

        storage = []

        for char in s:
            storage.append(char)
            if len(storage) >= 2 and char in combs and combs[char] == storage[-2]:
                storage.pop()
                storage.pop()
        
        if storage:
            return False
        
        return True



        