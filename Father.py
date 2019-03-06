class Father:
    name='inty'
    def eat(self):
        print('i can eat')
class Mother:
    def walk(self):
        print('walk like mother')
class Son(Father,Mother):
    pass
    def eat(self):
        print('eat like son')
    def walk(self):
        print('walk like son')
littleInty=Son()
littleInty.eat()
littleInty.walk()