class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        duplicates = []

        for i in range(len(nums)):

            if nums[i] not in duplicates:
                duplicates.append(nums[i])
                continue
            else:
                return True
        
        return False

        '''seen = set()

        for i in range(len(nums)):
            seen.add(nums[i])

        if len(seen) == len(nums):
            return False
        else:
            return True'''

        