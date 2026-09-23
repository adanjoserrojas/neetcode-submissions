class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # sort array
        # two pointer solution, pointers move towards each other
        # equation = nums[i] + nums[j] = -nums[k]
        # If we need a bigger number to satisfy the equation left pointer forward
        # If we need a smaller number to satisfy the equation right pointer backward
        # If equation is satisfied, append the triple to the res array

        #Outer loop at k
        #Inner loop => while left > right

        # O(n^2)
        # I need to handle duplicates

        
        nums = sorted(nums)
        res = []
        for j in range(len(nums)):
            left, right = j + 1, len(nums) - 1

            if j > 0 and nums[j] == nums[j - 1]:
                continue

            while left < right:
                
                if nums[left] + nums[right] > -nums[j]:
                    right -= 1

                elif nums[left] + nums[right] < -nums[j]:
                    left += 1

                elif nums[left] + nums[right] == -nums[j]:                   
                    res.append([nums[left], nums[right], nums[j]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1 

        return res




        





        