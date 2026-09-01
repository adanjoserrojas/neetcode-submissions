class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        target_len = len(s1)
        big_len = len(s2)
        
        # Quick exit if the target is bigger than the text
        if target_len > big_len:
            return False

        # 1. Count characters in the target word
        target_counts = {}
        for char in s1:
            target_counts[char] = target_counts.get(char, 0) + 1

        # 2. Setup the initial window counts for the start of the big string
        window_counts = {}
        for i in range(target_len):
            char = s2[i]
            window_counts[char] = window_counts.get(char, 0) + 1

        # Check if the very first window is a match
        if window_counts == target_counts:
            return True

        # 3. Slide the window across the rest of the big string
        for i in range(target_len, big_len):
            # Add the new character entering the window from the right
            new_char = s2[i]
            window_counts[new_char] = window_counts.get(new_char, 0) + 1

            # Remove the old character leaving the window on the left
            old_char = s2[i - target_len]
            window_counts[old_char] -= 1
            if window_counts[old_char] == 0:
                del window_counts[old_char] # Clean up empty keys to keep comparisons accurate

            # Check if the current window matches the target
            if window_counts == target_counts:
                return True

        return False


            






        return True
        