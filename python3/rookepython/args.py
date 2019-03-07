"""what is *args"""
# def add(num1,num2,num3):
#     print (num2+num2+num3)
# # add( 1,1,2)
# def add(*args):
#     print (type(args))
# add(23,23,56)
def add(*args):
    for name in args:
        print ("i love "+name)
add('xiaowang','xiaoming','wangwang')