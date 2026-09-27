class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # NGE needs a monotonic --------- stack
        # track the indexes of the bext greater element for the numbers in array nums1
        # so the size of array nums1 is the size of res array
        # O(n) 0(n), time and space worse case
        
        hmap = {n:i for i, n in enumerate(nums1)}
        stack = []
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = hmap[val]
                res[idx] = cur
            if cur in hmap:
                stack.append(cur)

        return res

         
                

            
        