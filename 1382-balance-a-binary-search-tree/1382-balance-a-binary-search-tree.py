# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def tr(node,l):
            if not node:
                return

            tr(node.left,l)
            l.append(node)
            tr(node.right,l)
            return l
        arr = tr(root,[])

        def b(start,end):
            if start>end:
                return None
            
            
            mid = (start + end) //2
            root = arr[mid]
            root.left = b(start,mid-1)
            root.right = b(mid+1,end)
            return root
        return b(0,len(arr)-1)