class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        table = {}

        for i in range(len(nums)):
            if nums[i] in table:
                return True
            table[nums[i]] = 0
            
        return False