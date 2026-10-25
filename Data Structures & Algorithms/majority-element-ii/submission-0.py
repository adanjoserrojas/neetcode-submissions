class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        res = []
        table = {}

        for num in nums:

            if num in table:
                table[num] += 1
            else:
                table.setdefault(num, 1)
            
            if num not in res and table[num] > len(nums)/3:
                res.append(num)
        return res

        