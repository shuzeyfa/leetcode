# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        l = []
        l.append(root)
        ind = 1
        while l:
            l2 = []
            for i in range(len(l)):
                if l[i].right:
                    l2.append(l[i].left)
                    l2.append(l[i].right)
            if ind%2 == 1 and l2:
                ind2 = len(l2)-1
                l3 = []
                for i in l2:
                    l3.append(i.val)
                for i in range(len(l)):
                    l[i].left.val = l3[ind2]

                    ind2 -= 1
                    l[i].right.val = l3[ind2]

                    ind2 -= 1
            # print(l2)
            l = []
            l += l2
            ind += 1
        return root


