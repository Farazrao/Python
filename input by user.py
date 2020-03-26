def count(lst):
    for i in range(len(lst)):
        if len(lst[i])>=5:
            print(lst[i])



namelst=[]
for i in range(4):
    name=str(input("enter the names"))
    namelst.append(name)
count(namelst)