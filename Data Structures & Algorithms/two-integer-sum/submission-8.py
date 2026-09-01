class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        has = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in has:
                return [has[complement], i]

            has[nums[i]] = i