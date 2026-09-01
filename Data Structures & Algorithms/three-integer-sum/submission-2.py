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
        n = len(nums)
        res = []

        for k in range(n-2):
            right = n - 1 
            left = k + 1

            if k > 0 and nums[k] == nums[k - 1]:
                continue

            while left < right:

                total = nums[k] + nums[left] + nums[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                elif total == 0:
                    res.append([nums[k], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                

        return res





        