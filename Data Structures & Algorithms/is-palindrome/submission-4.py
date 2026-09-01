class Solution:
    def isPalindrome(self, s: str) -> bool:
 
        s = "".join(filter(str.isalnum, s))
        s = s.lower()
        i = len(s) - 1
        print(s)
        for char in range(len(s)):
            print(f"{s[char]} and {s[i]}")
            if s[char] != s[i]:
                return False
            i -= 1
        return True


        