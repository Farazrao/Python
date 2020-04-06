class A:
    def feature1(self):
        print("hello1")

    def feature2(self):
         print("hello2")
class B():
    def __init__(self):
        print("in B in init")

    def feature3(self):
        print("hello3")

    def feature4(self):
        print("hello4")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C in init")
a1=C()