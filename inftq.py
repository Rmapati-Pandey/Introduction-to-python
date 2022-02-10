class ClassA:
    def __init__(self,val1):
        self.value=val1
    def method_a(self):
        return 20+self.value
class ClassB:
    def __init__(self,val2):
        self.num=val2
    def method_b(self,b):
        super().__init__(100)
        return b.method_a()+self.num

a=ClassA(20)
b=ClassB(10)
print(b.method_b(a))
