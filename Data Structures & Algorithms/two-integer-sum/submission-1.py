class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        for index, number in enumerate(nums):
            complement = target - number
            if complement in hashMap:
                return [hashMap[complement], index]
            hashMap[number] = index
        