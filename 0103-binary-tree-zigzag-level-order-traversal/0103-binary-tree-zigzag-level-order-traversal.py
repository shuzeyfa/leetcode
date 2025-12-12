# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        l = deque()
        l.append(root)
        l3 = [[root.val]]
        t = True
        while l:
            l4 = []
            l2 = []
            while l:
                if l[-1].right:
                    l4.append(l[-1].right.val)
                    l2.append(l[-1].right)
                if l[-1].left:
                    l4.append(l[-1].left.val)
                    l2.append(l[-1].left)
                l.pop()
            if t == True and l4:
                l3.append(l4)
                t = False
            elif t == False and l4:
                l3.append(l4[::-1])
                t = True
            l = deque()
            for i in l2:
                l.appendleft(i)
        return l3
            
            
