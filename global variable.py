a=10
def update():
    global a
    a=15
    print("inside fun",a)
update()
print("out side fun",a)