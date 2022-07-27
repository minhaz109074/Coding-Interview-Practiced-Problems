# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None: return ans
        stack = [(root,0)]
        mapp = defaultdict(int)
        while len(stack):
            node, line = stack.pop()
            if line not in mapp: 
                mapp[line] = node.val
            if node.left:
                stack.append((node.left, line+1))
            if node.right:
                stack.append((node.right, line+1))
        for y in mapp.values():
            ans.append(y)
            
        return ans
                
        