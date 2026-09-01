class Solution:
    def findMin(self, nums: List[int]) -> int:

        '''mid = len(nums) // 2
        left = 0
        right = len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return min(nums)

        if len(nums) == 3 and nums[mid] < nums[left] and nums[mid] < nums[right]:
            return nums[mid]

        while nums[left] < nums[mid]:
            mid += 1
            if mid == right:
                return nums[left]

            if nums[mid] < nums[left]:
                return nums[mid]

        while nums[mid] < nums[right]:
            mid -= 1
            if mid == left:
                return nums[left]

            if nums[mid] > nums[right]:
                return nums[mid + 1]'''

        return min(nums)
        

            
        
        