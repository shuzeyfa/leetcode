s="1009998"

def dfs(val,index):
    if index == len(s):
        return True
    
    for j in range(index,len(s)):
        val2 = int(s[index:j+1])
        if val2 + 1 == val and dfs(val2,j+1):
            return True
    return False


t=False
for i in range(len(s) - 1):
    val = int(s[:i+1])
    if dfs(val,i+1):
        print(True)
        t=True
        break
if t==False:
    print(False)