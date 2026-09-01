# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            
            left_Valid = valid(node.left, low, node.val)
            right_Valid = valid(node.right, node.val, high)
                
            return left_Valid and right_Valid

        return valid(root, float('-inf'), float('inf'))
        
        