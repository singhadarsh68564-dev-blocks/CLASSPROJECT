#type conversion
a=2
b=4.25
print(a+b) # 2.0 + 4.25 => 6.25

# a="2" there will be an error while printing this value 
# b=4.35
# print(a+b)

#type casting
a= int("2")
b=4.25
print(type(a)) #type is integer
print(a+b)

a=3.14
a=str(a)
print(type(a))

#input in python

name = input("enter your name:")
print("welcome:", name)

val= int(input("enter some value;"))
print(type(val), val)

name= input("enter your name:")
Age= input("enter age:")
Marks= input("enter marks:")

print("welcome=", name)
print("age=", Age)
print("marks=", Marks)








