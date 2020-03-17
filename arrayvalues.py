from array import *
rao=array('i',[])
g=int(input("enter the lenght of array"))
for i in range(g):
     f=int(input("enter the values"))
     rao.append(f)
print(rao)
a=int(input("enter the searching value"))
k=0
for e in rao:
    if e==a:
        print(k)
        break

    k+=1