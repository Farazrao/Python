class student:
    uversity='lahore leads university'
    def __init__(self,m1,m2,m3):
        self.m1= m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    # this is a class method
    @classmethod
    def info(cls):
        return cls.uversity
    # this is a static method
    @staticmethod
    def info1():
        print("this is studnet class")
s1=student(34,67,32)
s2=student(89,32,12)
# print he avg
print(s1.avg())
# print class method
print(student.info())
# print static method
student.info1()
