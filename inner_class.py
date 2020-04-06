class student:
    # simple function
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()
        # show all the values
    def show(self):
        print(self.name,self.rollno)
        # show the value of laptop also
        self.lap.show()
        # inner class
    class laptop:
        # simple function
        def __init__(self):
            self.brand='HP'
            self.CPU='i5'
            self.ram=8
            # show all the values
        def show(self):
            print(self.brand,self.CPU,self.ram)
s1=student('Rao',2)
s2=student('Faraz',3)
# only show all the values of s1
s1.show()