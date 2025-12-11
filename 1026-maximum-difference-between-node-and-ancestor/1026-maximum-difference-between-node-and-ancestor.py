# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxx = 0
        de = deque()
        de.append((root,root.val,root.val))
        while de:
            node, max2, min2 = de.popleft()
            maxx = max(maxx, abs(max2-node.val),abs(min2-node.val))

            if node.left:
                de.append((node.left,max(node.val,max2),min(node.val,min2)))
            if node.right:
                de.append((node.right,max(node.val,max2),min(node.val,min2)))
        return maxx
