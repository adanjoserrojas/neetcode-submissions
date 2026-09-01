class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        target_len = len(s1)
        big_len = len(s2)

        if target_len > big_len:
            return False

        target_counts = {}
        for char in s1:
            target_counts[char] = target_counts.get(char, 0) + 1
        
        window_counts = {}
        for i in range(target_len):
            char = s2[i]
            window_counts[char] = window_counts.get(char, 0) + 1
        
        if window_counts == target_counts:
            return True
        
        for j in range(target_len, big_len):

            new_char = s2[j]
            window_counts[new_char] = window_counts.get(new_char, 0) + 1

            old_char = s2[j - target_len]
            window_counts[old_char] -= 1
            if window_counts[old_char] == 0:
                del window_counts[old_char]

            if window_counts == target_counts:
                return True
        
        return False