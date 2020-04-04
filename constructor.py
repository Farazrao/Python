class computer:
    def __init__(self):
        self.name='faraz'
        self.age=24
        # i create new function here because i can update the value pf age
    def update(self):
        self.age=23
        # here i can compare he age of rao and faraz
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
c1=computer()
c2=computer()
c3=computer()
c4=computer()
# here i compare and simple print
if c1.compare(c2):
    print("the ages are same")
# aslo i changed thevalue by using another method
c1.name="rao"
# here i update the vlue of c2 .age
c2.age=23
c1.update()

print(c1.name)
print(c2.age)
print(c3.name)
print(c4.age)

