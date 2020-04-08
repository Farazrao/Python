class topten:
    def __init__(self):
        self.num=1
        # funtion of iteration 1st
    def __iter__(self):
        return self
    # function of iteration second
    def __next__(self):
        if self.num<=10:
            a=self.num
            self.num+=1
            return a
        else:
            raise stopIteration
val=topten()
for i in val:
    print(i)