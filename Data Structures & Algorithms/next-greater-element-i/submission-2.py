class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # NGE needs a monotonic --------- stack
        # track the indexes of the bext greater element for the numbers in array nums1
        # so the size of array nums1 is the size of res array
        # O(n) 0(n), time and space worse case
        
        hmap = {}
        stack = []
        res = []

        for num in nums2:

            while stack and num > stack[-1]:
                popped = stack.pop()
                hmap[popped] = num

            stack.append(num)
        
        for rem in stack:
            hmap[rem] = -1
        
        for i in nums1:
            print(i)
            res.append(hmap[i])

        return res 
                

            
        