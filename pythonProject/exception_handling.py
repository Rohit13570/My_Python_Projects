def division(a,b):
    try:
        return a/b
    except:
            print("This operation cannot be done")
    finally:
        print("Operations complete")
x = float(input("Enter your dividend"))
y = float(input("Enter your divisor"))
print(division(x,y))



