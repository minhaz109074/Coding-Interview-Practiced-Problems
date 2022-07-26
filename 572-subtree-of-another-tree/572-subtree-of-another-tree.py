# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
       
        def isIdentical(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False

            return (root1.val == root2.val) and isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)
        
        def dfs(r, s):
            if r is None:
                return False
            if isIdentical(r,s):
                return True
            
            return dfs(r.left, s) or dfs(r.right, s)
        
        return dfs(root, subRoot)
        