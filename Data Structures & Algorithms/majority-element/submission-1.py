class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums.sort()
        print(nums)

        counter = 0
        cur = nums[0]
        for num in nums:
            print(counter, cur)
            if counter > len(nums)/2:
                print(counter)
                return cur
            
            if cur == num:
                counter += 1
            else:
                counter = 1
                cur = num
        print(counter)
        return cur 
            



