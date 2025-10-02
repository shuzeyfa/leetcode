# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        memo = {}

        def dp(node):
            if not node:
                return 0
            
            if node not in memo:
                include = node.val
                if node.right:
                    include += dp(node.right.right) + dp(node.right.left)
                if node.left:
                    include += dp(node.left.right) + dp(node.left.left)
                exclude = dp(node.right) + dp(node.left)
                memo[node] = max(include, exclude)
            return memo[node]
        
        return dp(root)