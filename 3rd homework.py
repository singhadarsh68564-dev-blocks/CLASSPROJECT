# ques1 = wap to ask the user to enter names of their 3 favorite movies & store them in a list

# movies=[]
# a=input("1st movie:")
# b=input("2nd movie:")
# c=input("3rd movie:")

# movies.append(a)
# movies.append(b)
# movies.append(c)
# print(movies)
# # another way 
movies1=[]
movies1.append(input("1st movie:"))
movies1.append(input("2nd movie:"))
movies1.append(input("3rd movie:"))
print(movies1)

# ques =2 wap to check if a list contains a palindrome of elements
# palindrome= aage se and back se padhne par same ho

list1=[1,2,1]
list2=[1,2,3]

a=list1.copy()
a.reverse()
if(a==list1):
    print("palindrome")
else:
    print("not palindrome")

b=list2.copy()
b.reverse()
if(b==list2):
    print("palindrome")
else:
    print("not palindrome")

list3=["m","a","a","m"]
c=list3.copy()
c.reverse()
if(c==list3):
    print("palindrome")
else:
    print("not palindrome")

# ques = 3 wap to count the number of students with the "A" grade in the following tuple.
# ["C","D","A","A","B","B","A"]

grade=("C","D","A","A","B","B","A")
print(grade.count("A"))

# ques = 3 store the values in a list & sort them from a to d

list=["C","D","A","A","B","B","A"]
list.sort()
print(list)



















