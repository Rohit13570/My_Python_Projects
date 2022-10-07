def discount1(a):
    return a-a*(10/100)
def discount2(b):
    return b-b*(5/100)
result= discount1(discount2(int(input("Enter the value"))))
print (result)