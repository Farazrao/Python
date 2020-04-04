import sys
sys.setrecursionlimit(2000)
# here we set the recursion limit
print (sys.getrecursionlimit())
# here we get the recursion
i=0
def greet ():
    global i
    i+=1
    print("hello",i)
    greet()
greet()