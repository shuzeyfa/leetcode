n = input()
t=False

for i in n:
    if i != "1" and i != "4":
        t=True
        break
if t==True:
    print("NO")
else:
    if n[0] == "4":
        print("NO")
    else:
        if "444" in n:
            print("NO")
        else:
            print("YES")