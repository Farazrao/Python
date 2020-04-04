class computer():
    def config(self):
        print("i5,16gb.1TB")
        print("i5,8gb.1TB")
        print("i5,6gb.1TB")
# this is the object related to the class
com1=computer()
com2=computer()
com3=computer()
#  here i call the function config the class computer in object com1
computer.config(com1)
computer.config(com2)
computer.config(com2)
# here is the second method to call the function
com1.config()
com2.config()
com3.config()