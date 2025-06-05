def st(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack and stack[-1]=="(":
                stack.pop()
            else:
                stack.append(i)
    return len(stack) == 0
def find(s):
    temp = s.replace("A","(")
    temp = temp.replace("B","(")
    temp = temp.replace("C",")")
    if st(temp):
        return True
    temp2 = s.replace("A","(")
    temp2 = temp2.replace("B",")")
    temp2 = temp2.replace("C","(")
    if st(temp2):
        return True
    temp2 = s.replace("A","(")
    temp2 = temp2.replace("B",")")
    temp2 = temp2.replace("C",")")
    if st(temp2):
        return True
    
    temp3 = s.replace("A",")")
    temp3 = temp3.replace("B","(")
    temp3 = temp3.replace("C",")")
    if st(temp3):
        return True
    temp3 = s.replace("A",")")
    temp3 = temp3.replace("B","(")
    temp3 = temp3.replace("C","(")
    if st(temp3):
        return True
    temp4 = s.replace("A",")")
    temp4 = temp4.replace("B",")")
    temp4 = temp4.replace("C","(")
    if st(temp4):
        return True
    return False
    
for _ in range(int(input())):
    s = input()
    if find(s):
        print("YES")
    else:
        print("NO")