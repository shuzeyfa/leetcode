# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = root.left
        right = root.right
        if not left and not right:
            return True
        
        def first(temp,l):
            if not temp:
                return []

            l.append(temp.val)
            if temp.left:
                first(temp.left,l)
            else:
                l.append(None)
            if temp.right:
                first(temp.right,l)
            else:
                l.append(None)
            return l
        def sec(temp2,l2):
            if not temp2:
                return []

            l2.append(temp2.val)
            if temp2.right:
                sec(temp2.right,l2)
            else:
                l2.append(None)
            if temp2.left:
                sec(temp2.left,l2)
            else:
                l2.append(None)
            return l2

        a = sec(left,[]) 
        b = first(right,[])
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True