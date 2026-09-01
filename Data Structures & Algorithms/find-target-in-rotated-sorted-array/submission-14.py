class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        if len(nums) == 1 and target == nums[0]:
            return 0

        while left < right:
            if target == nums[left]:
                return left
            elif target == nums[right]:
                return right
            if nums[left] > nums[right] and target < nums[right]:
                right -= 1
            else:
                left += 1

        return -1
                
        
        