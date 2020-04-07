class student:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        # add methods
    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        m3 = self.m3 + other.m3
        s3=student(m1,m2,m3)
        return s3
    # greter method
    def __gt__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m1 + other.m2
        m3 = self.m3 + other.m3
        if m1>m2:
            return  True
        else:
            return False
    def __str__(self):
        return self.m1,self.m2
s1=student(58,69,5)
s2=student(60,65,5)
s3=s1+s2
print(s3.m1,s3.m2)
if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")
print(s1.__str__())

