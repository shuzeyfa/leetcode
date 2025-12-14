# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def post(root,l):
            if not root:
                return []
            
            if root.left:
                post(root.left,l)
            if root.right:
                post(root.right,l)

            l.append(root.val)
            return l
        return post(root,[])