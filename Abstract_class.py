from abc import ABC, abstractmethod
# python does not support abstract class by defual thats why we impor ABC and abstractmethod
class computer(ABC):
    @abstractmethod
    def process(self):
        pass
class laptop(computer):
    def process ():
        print("its running")
class whiteboard(computer):
    def write(self):
        print("its working")
class programming:
    def work(self,com):
        print("solving bugs")
        #com.process()
com1=laptop()
#com2=whiteboard()
#com2.write(com1)
prog1=programming()
prog1.work(com1)