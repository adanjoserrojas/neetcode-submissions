class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        
        nums.sort()
        res = []

        for k, num in enumerate(nums):
            if num > 0:
                break
            
            if k > 0 and num == nums[k - 1]:
                continue

            l, r = k + 1, len(nums) - 1

            while l < r:

                threeSum = num + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[r], num])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res



            



        





        