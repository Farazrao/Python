class A:
    def feature1(self):
        print("hello1")

    def feature2(self):
         print("hello2")

class B():
        def feature3(self):
            print("hello3")

        def feature4(self):
            print("hello4")
# class C inheritance the value of A and B
class C(A,B):
        def feature5(self):
            print("hello5")
        # constructor
a1=A()
a1.feature1()
a1.feature2()
b1=B()
b1.feature3()
b1.feature4()
c1=C()
c1.feature5()
# b1 and c1 show thw parent and child class
#b1.
#c1.
