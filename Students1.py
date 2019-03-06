class Students1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def walk(self):
        print(self.name,'can walk')
        print(self.name,'is',self.age)
s1=Students1('china','40')
s1.walk()
s2=Students1('inty','50')
s2.walk()