a=10
def update():
    a=9
    globals()['a']
    print("inside fun",a)
    globals()['a']=15
update()
print("outside fun",a)