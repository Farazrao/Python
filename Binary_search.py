# global variable using for finding the position of the number
POS=-1
def search (list,n):
   l=0
   u=len(list)-1
   while l<=u:
       mid=(l+u)//2
       if list[mid]==n:
           globals()['pos']=mid
           return True
       else:
           if list[mid] < n:
               l = mid;
           else:
               u = mid;
list = [10,52,85,96,7,45,99668,877885,955882,2548]
n=877885
if search(list,n):
    print("found at",pos)
else:
    print("not found")