class Solution:
    def isPalindrome(self, s: str) -> bool:
 
        # s = [char.lower() for char in s if char.isalnum()]
        clean = "".join(filter(str.isalnum, s))
        extra_clean = list(clean.lower())

        left = 0
        right = len(extra_clean) - 1

        while left < right:
            if extra_clean[left] != extra_clean[right]:
                return False
            left += 1
            right -= 1
        return True


        