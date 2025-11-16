# ques1 = store following word meaning in a python dictionary:
# table: "a piece of furniture","list of facts & figure"
# cat: "a small animal" 

a={"cat":"a small animal",
  "table": ["a piece of furniture","list of fact & figure"]}
print(a)

# ques = 2 you are given a list of subjects for students. assume one classroom is required for 1 subjects. how many classroom are needed by all students
# "python","java","c++","python","javascript","java","python","java","c++","c"
sets={"python","java","c++","python","javascript","java","python","java","c++","c"}
print(len(sets)) # 5 classroom required

# ques=3 WAP to enter marks of 3 subjects from the user and store them in a dictionary. start with
# an empty dictionary & add one by one. use subject name as key & marks as a value.

# marks={}
# a=int(input("enter phy marks:"))
# marks.update({"phy":a})
# b=int(input("enter math marks:"))
# marks.update({"math":b})
# c=int(input("enter che marks:"))
# marks.update({"che":c})
# print(marks)

# ques=4 figure out a way to store 9 & 9.0 as seprate values in the set
# (take help of built in data type)

b={9,9.0}
print(b) # yaha python dono value ko same le rha hai
b={9,"9.0"}
print(b)
c={("float",9.0),("int",9)}
print(c)

