def search (list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            return True
        i+=1
    else:
           return False
list = [5,8,6,9,7]
n=9
if search(list,n):
    print("found")
else:
    print("not found")