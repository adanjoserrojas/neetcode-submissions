class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        productOfAll = 1
        zeroInThere = False
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroInThere = True
                count += 1
                continue
            productOfAll *= nums[i]
        
        newArray = [0] * len(nums)
        if count >= 2:
            return newArray
        
        for j in range(len(nums)):
            if nums[j] == 0:
                newArray[j] = productOfAll
            elif zeroInThere == True:
                newArray[j] = 0
            else:
                newArray[j] = productOfAll // nums[j]
        
        return newArray
