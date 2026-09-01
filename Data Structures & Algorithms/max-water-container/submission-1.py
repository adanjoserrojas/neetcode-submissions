class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        area = 0
        i = 0

        while left <= right:
            current_area = (right - left) * min(heights[left], heights[right])
            print(f"Current area {area} at iteration: {i}")

            if area < current_area:
                area = current_area

            if heights[left] > heights[right]:
                right -= 1
            
            elif heights[right] > heights[left]:
                left += 1
            
            elif heights[right] == heights[left]:
                left += 1

            i += 1
               
        return area



        