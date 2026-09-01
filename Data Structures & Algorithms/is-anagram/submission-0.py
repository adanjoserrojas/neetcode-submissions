class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashS = {}
        hashT = {}

        if len(s) != len(t):
            return False

        for ch in s:

            if ch in hashS:
                hashS[ch] += 1
            else:
                hashS[ch] = 1
        for ch in t:
            
            if ch in hashT:
                hashT[ch] += 1
            else:
                hashT[ch] = 1
           
        if hashS.keys() != hashT.keys():
            return False
        
        for key in hashS:
            if hashS[key] != hashT[key]:
                return False

        return True

            