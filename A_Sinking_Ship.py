n = int(input())
rat = []
woman = []
man = []
captain = []
for i in range(n):
    name,role = input().split()
    if role == "rat":
        rat.append(name)
    elif role == "woman" or role == "child":
        woman.append(name)
    elif role == "man":
        man.append(name)
    else:
        captain.append(name)
# print(woman)
for i in rat:
    print(i)
for i in woman:
    print(i)
for i in man:
    print(i)
for i in captain:
    print(i)