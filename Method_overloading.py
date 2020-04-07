class student:
    # 1st statement
    def sum (self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else: s=a
        return s
s1=student()
# overloading method we have two value but three parameters so by using overloading methods with 1st statement
# we solve it
print(s1.sum(5,5))
