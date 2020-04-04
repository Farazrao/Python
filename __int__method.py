class computer():
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("config is",self.cpu,self.ram)
# here i mentioned the values of cpu and ram ,com1 is object of class compuer and define two
# parameter values
com1=computer('i5',12)
com2=computer('i6',16)
# this is call method
com1.config()
com2.config()

