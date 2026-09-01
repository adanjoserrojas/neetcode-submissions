class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # NGE needs a monotonic --------- stack
        # track the indexes of the bext greater element for the numbers in array nums1
        # so the size of array nums1 is the size of res array
        # O(n) 0(n), time and space worse case
        res = {}
        stack = []
        final = []
        for i in range(len(nums2)):
            
            while stack and nums2[i] > stack[-1]:
                popped = stack.pop()
                res[popped] = nums2[i]

            stack.append(nums2[i])

        for num in stack:
            res[num] = -1
        
        for value in nums1:
            final.append(res[value])
        
        return final
                
                

            
        