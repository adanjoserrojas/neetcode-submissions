from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        # Required frequency of each character in t
        need = Counter(t)

        # Frequency of required characters in the current window
        window = defaultdict(int)

        # Number of distinct characters whose required frequency is satisfied
        formed = 0
        required = len(need)

        left = 0

        best_start = 0
        best_length = float("inf")

        for right, right_char in enumerate(s):
            # Expand the window
            if right_char in need:
                window[right_char] += 1

                # Only increment formed when we reach the exact requirement
                if window[right_char] == need[right_char]:
                    formed += 1

            # The window contains every required character
            while formed == required:
                current_length = right - left + 1

                # Save the smallest valid window found
                if current_length < best_length:
                    best_start = left
                    best_length = current_length

                left_char = s[left]

                # Shrink the window from the left
                if left_char in need:
                    # If this character was exactly satisfied, removing it
                    # make the window invalid
                    if window[left_char] == need[left_char]:
                        formed -= 1

                    window[left_char] -= 1

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_start:best_start + best_length]