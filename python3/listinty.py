# newList=[]
# for i in range(11):
#     newList.append(i*2)
# print(newList)
# print([i*2 for i in range(11)])
list=["小明","王二","王八","李四"]
#emptylist=[]
#for name in list:
#    if name.startswith("王"):
#       emptylist.append(name)
#      print(name)
#print(emptylist)
print([name for name in list if name.startswith("王")])