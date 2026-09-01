class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashMapS = {}
        hashMapT = {}

        if len(s) != len(t):
            return False

        for i, ch in enumerate(s):

            if ch in hashMapS:
                hashMapS[ch] += 1
                continue
            hashMapS[ch] = 1
        
        for i, ch in enumerate(t):

            if ch in hashMapT:
                hashMapT[ch] += 1
                continue
            hashMapT[ch] = 1

        
        for key in hashMapS:
            print(key)
            if key not in hashMapT or hashMapS[key] != hashMapT[key]:
                return False
        
        return True


        