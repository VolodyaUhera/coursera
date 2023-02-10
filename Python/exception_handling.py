def devide_by(a, b):
    return a / b

try:
    ans = devide_by(40,0)
except ZeroDivisionError as e:
    print("Something went wrong: ", e)
    print(e.__class__)
except Exception as e:
    print(e, "something wrong")
    
