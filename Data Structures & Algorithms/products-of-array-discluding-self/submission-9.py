class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []
        total = 1
        zero = False
        hashMap = {}
        counter = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero = True
                counter += 1
                continue
            total *= nums[i]

        if counter >= 2:
            return [0] * len(nums)
    
        for i in range(len(nums)):
            if nums[i] == 0:
                hashMap[i] = total
                continue
            hashMap[i] = 0


        if zero == True:
            for j in range(len(nums)):
                if hashMap[j] == total:
                    res.append(total)
                    continue
                res.append(0)
            return res

        for z in range(len(nums)):
            if zero == True:
                pass
            res.append(total//nums[z])

        return res