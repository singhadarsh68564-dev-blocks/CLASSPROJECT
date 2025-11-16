# a=input("what is your name:")
# print("length of name:",len(a))

# a="iam AAAA$$$$$$$$$$"
# print(a.count("$"))

marks=74

if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="c"
else:
    grade="D"

print("grade of the student ->", grade)

marks=int(input("enter student marks:"))

if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="c"
else:
    grade="D"

print("grade of the student ->", grade) 

# ques1

num=int(input("enter number:"))

rem=num%2

if(rem==0):
    print("EVEN")
else:
    print("ODD")

# ques2

a=int(input("1st number:"))
b=int(input("1st number:"))
c=int(input("1st number:"))

if(a>=b and a>=c):
    print("largest1:", a)
elif(b>c):
    print("largest2:", b)
else:
    print("largest3:", c)

# ques3

x=int(input("enter number:"))

if(x%7==0):
    print("multiple of 7")
else:
    print("not multiple of 7")











