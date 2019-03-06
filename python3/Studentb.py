class Studentb:
#     def eat(self,name,age):
#         print(name+"can eat"+"and he is"+age)
# Studentb().eat("JAMES",'21')
    name='包崇应'
    age=18
    def eat(self):
        print(self.name,'can eat','he is ',self.age)
    def walk(self):
        print(self.name,'跑的很快','他的年龄是',self.age)
Studentb().eat()
Studentb().walk()
student1=Studentb()
student1.eat()
student1.walk()
student2=Studentb()
student2.eat()
student2.walk()