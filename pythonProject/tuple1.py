tuple1=("apple","cherry","pineapple","guava")
print(tuple1)
list1=list(tuple1)
list1.insert(3,"banana")
list1.append("mango")
tuple1=tuple(list1)
print(tuple1)
print(type(tuple1))