"""this is **args"""
def m1(*args,**kwargs):
   print "the type of",type(args)
   print ("the type of ",type(kwargs))
#m1()
#dic_inty={'name':'inty','age':'18 years old','height':'190cm','weght':'195lb'}

#def someone(dic_someone):
 #   for k,v in dic_someone.items():
#for k,v in dic_inty.items():
def someone(**kwargs):
    for  k ,v in kwargs.items():
        print (k, ':', v)
someone(name='xiaohong',age='65',herght="65")