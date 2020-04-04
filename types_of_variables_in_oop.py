class car:
    # here wheel is he class variable
    wheel=4
    def __init__(self):
        # here mill and company is the unstance variables
        self.mill=10
        self.company="BMW"

c1=car()
c2=car()
# here i can update the c1.mill value (10 to 8)
c1.mill=8
# here i can update the class variable value (4 to 5)
car.wheel=5
print(c1.company,c1.mill,c1.wheel)
print(c2.company,c2.mill,c1.wheel)