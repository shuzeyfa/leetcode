# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root,mul):
            nonlocal ans
            if not root.left and not root.right:
                ans += (mul * 10 + root.val)
                return

            if root.left:
                dfs(root.left,mul * 10 + root.val)
            if root.right:
                dfs(root.right,mul * 10 + root.val)
            
        dfs(root,0)
        return ans
            