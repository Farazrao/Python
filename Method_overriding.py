class A:
    def show(self):
        print(" A is show")
class B(A):
    def show(self):
        print("B is show")
# here this is overiding
a1=B()
a1.show()