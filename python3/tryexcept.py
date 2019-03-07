try :
    print(10/8)
    print(10+"0")
except ArithmeticError as e:
    print(e)
# except TypeError as e:
#     print(e)
except Exception:
    print("there is something wrong")

