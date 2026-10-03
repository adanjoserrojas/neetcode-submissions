class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m]
        p1 = 0
        while p1 < len(nums1) and nums2:
            
            if nums1[p1] > nums2[0]:
                nums1.insert(p1, nums2[0])
                del nums2[0]
            
            p1 += 1
        
        nums1.extend(nums2)
        
        return nums1