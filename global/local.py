a=10
print(id(a))
def update():
    a=9
    x=globals()['a']
    print(id(a))
    print("inside fun",a)
    globals()['a']=15
update()
print("outside fun",a)