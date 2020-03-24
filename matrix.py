def update (lst):
    print(id(lst))
    lst[1]=25
    lst[2]=26
    print(id(lst))
    print("x",lst)
lst=[10,20,30]
print(id(lst))
update(lst)
print("lst",lst)