# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None: return ans
        queue = deque([root])

        while len(queue):
            curList = []
            level = len(queue)
            for i in range(level):
                cur = queue.popleft()
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
                
                curList.append(cur.val)
                
                
            ans.append(curList)
        return ans
        
        