# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder_index = 0
        
        def Tree(left, right):
            if left > right:
                return None
            root_val = preorder[self.preorder_index]
            node = TreeNode(root_val)
            self.preorder_index += 1
            
            node.left = Tree(left, inorder_map[root_val] - 1)
            node.right = Tree(inorder_map[root_val] + 1, right)
            return node
        
        
        inorder_map = {}
        for i,val in enumerate(inorder):
            inorder_map[val] = i
        return Tree(0, len(preorder)-1)
        