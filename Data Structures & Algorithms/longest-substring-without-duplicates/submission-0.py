class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Two pointer solution
        # You just need the length
        # Use a hash table to inser the key = substring , value = frequency of that substring in the array
        # Expand the length of the sliding window until you find a char that is already in the substring
        # that length becomes your window length
        # check for that length to see if the frequency of any substring is increments to > 1 (means there is multiple)
        # then in that hash map of substrings that hold > 1 values, return the substring with the greatest length
        
        # Ok since I missed read the problem this is my new approach

        # We do not care about this string being twice or many times in the array
        # Then all I need to have is two pointers
        # Left starts at 0 and right starts at 1
        # right moves forward until it finds a char that is already in the string, or it hits len(s) - 1
        # if right found that, for that string we insert it as a key with value of its length
        # then left moves forward to the position + 1in which that letter was in the array
        # example: 
                    # yzxox... Initially left at y and right hits x... That means left has to advance until it gets to "o"
                    # and at this point my hash table/ dict must have "yzxo": 4
        
        # Ok I have debugged myself and I think I got it now, instead of using the has table for look ups
        # we are gonna use for removals with a seen dict, or a set, either works
        # we are gonna loop through the string and basically if s[right] catches a dup
        # we enter a loop in which I will delete all the characters before that first "seen char" in my string
        # and then the substring eventually will have no dups and will be shorter, but we have already stored the max value in res atp, and could...
        # move forward trying to find other longer sibtrings

        seen = set()
        left = 0
        res = 0

        for right in range(len(s)):
            
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                
            seen.add(s[right])
            res = max(res, right - left + 1)
        
        return res

        