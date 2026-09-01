class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        # Now I am doing characterReplacement.
        # My approach is having a sliding window that grows as it finds new characters
        # Right always += 1, and left too because my window length has to compare characters
        # by window length 2
        # example: "YXXY" and k = 2 first 2 YX diff = k -= 1
        # second XX perfect move on
        # thrid XY diff k -= 1, k == 0... right + 1 = length of longest possible substring
        # if k -= 1 when a the characters of s[left] and s[right] are different

        # There is a pit fall here... What if the first longest substring we find
        # is not the longest one possible... I need to make a copy of k so I do not lose that original value
        # and keep a longest res varaible that can be larger and larger everytime
        # Once I scanned a whole zone, I can move the pointers left = right, and right = left + 1
        # Hopefully that does not break my loop though... Let's try

        # Ok I have a bug that basically is makeing my outputs wrong. I have spotted the bug
        # What happens is that when right and left have different characters in the middle of the string
        # it discounts from cur_k
        # but when I move the window forward by 1, then left and right have different characters again
        # which means that now I have substracted from cur_k twice... Making my output wrong. I am stuck
        
        left = 0
        right = left + 1
        freq = {}
        res = 0
        maxF = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            maxF = max(maxF, freq[s[right]])

            if (right - left + 1) - maxF > k:
                freq[s[left]] -= 1
                left += 1

            res = max(maxF, right - left + 1)
        return res
            