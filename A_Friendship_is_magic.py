l = [2,4,3,5,7,8,9,2,3,4,1,1,5,7]

def mergeSort(left_list, right_list):
    len1 , len2 = len(left_list), len(right_list)
    i = j = 0
    merged = []
    while i < len1 and j < len2:
        if left_list[i] <= right_list[j]:
            merged.append(left_list[i])
            i += 1
        else:
            merged.append(right_list[j])
            j += 1
    
    while i < len1:
        merged.append(left_list[i])
        i += 1

    while j < len2:
        merged.append(right_list[j])
        j += 1
    
    return merged


def merge(left,right,l):
    if left == right:
        return [l[left]]
    
    mid = (left + right) // 2
    left_list = merge(left, mid, l)
    right_list = merge(mid+1, right, l)

    return mergeSort(left_list,right_list)

print(merge(0,len(l)-1,l))