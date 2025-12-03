# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0
        def ave(root):
            nonlocal count
            if not root:
                return 0,0

            left,ind1 = ave(root.left)
            right, ind2 = ave(root.right)

            node = ind1 + ind2 + 1
            summ = left + right + root.val
            if summ // node == root.val:
                count += 1
            return summ, node
        ave(root)
        return count