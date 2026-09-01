class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        counter = 1
        nums = sorted(nums)
        i = 0
        j = i + 1
        possible_seq = []
        if not nums:
            return 0
        
        print(nums)

        while i < len(nums):
            
            if j < len(nums) and nums[j] - nums[i] == 1:
                counter += 1
            
            elif j < len(nums) and nums[j] - nums[i] > 1:
                counter = 1
            possible_seq.append(counter)
            i += 1
            j += 1

        print(possible_seq)
        
        return max(possible_seq)
        