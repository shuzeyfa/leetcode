# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        l= [root]
        l3 = [root.val]
        while l:
            l2 = []
            maxx = float("-inf")
            for i in range(len(l)-1,-1,-1):
                if l[i].right:
                    if l[i].right.val> maxx:
                        maxx = l[i].right.val
                    l2.append(l[i].right)
                if l[i].left:
                    if l[i].left.val> maxx:
                        maxx = l[i].left.val
                    l2.append(l[i].left)
                
                l.pop()
            
            if maxx != float("-inf"):
                l3.append(maxx)
           
            l += l2
        return l3
                    
