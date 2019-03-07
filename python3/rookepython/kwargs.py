"""kwargs"""
def m1(*args,**kwargs):
    print "the type of",type(args)
    print ("the type of ",type(kwargs))
#m1()
dic_inty={'name':'inty','age':'18 years old','height':'190cm'}
for k,v in dic_inty.items():
    print (k,':',v)