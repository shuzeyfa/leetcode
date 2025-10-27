# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def tr(root,l):
            l.append(root.val)
            if root.left:
                tr(root.left,l)
            if root.right:
                tr(root.right,l)

            return l
            
        
        res = tr(root,[])
        res.sort()
        return res[k-1]