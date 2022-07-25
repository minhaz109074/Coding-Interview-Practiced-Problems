# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def checkHeight(root):
            if root is None:
                return 0

            lh = checkHeight(root.left)
            rh = checkHeight(root.right)
            if lh == -1 or rh == -1 or abs(rh-lh) > 1: return -1

            return max(lh,rh) + 1
        
        return checkHeight(root) != -1
        