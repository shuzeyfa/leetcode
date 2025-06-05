# def merge(left_ele,right_ele):
#     i, j = 0, 0
#     ans = []
#     while i<len(left_ele) and j<len(right_ele):
#         if left_ele[i]<=right_ele[j]:
#             ans.append(left_ele[i])
#             i += 1
#         else:
#             ans.append(right_ele[j])
#             j += 1
#     while i<len(left_ele):
#         ans.append(left_ele[i])
#         i+=1
#     while j<len(right_ele):
#         ans.append(right_ele[j])
#         j+=1
#     return ans


# def merged(l,left,right):
#     if left==right:
#         return [l[left]]
    
#     mid = (left+right) // 2
#     left_ele = merged(l,left,mid)
#     right_ele = merged(l,mid+1,right)
#     return merge(left_ele,right_ele)

l = [6,5,7,8,4,3,1,2]
ans = []
for i in range(0,len(l),2):
    if l[i]>l[i+1]:
        l[i], l[i+1] = l[i+1], l[i]
    ans.append([l[i],l[i+1]])
ans.sort()


