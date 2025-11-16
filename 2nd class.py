str1="this is a string.\nwe are creating it it in python."
print(str1)

str1="this is a string.\twe are creating it it in python."
print(str1)

# concatenation

str1="adarsh singh "
str2="i love you"
print(str1+str2)

# length of str

str1="adarsh singh "
str2="i love you"
print(len(str1))
print(len(str2))
print(len(str1+str2))

# indexing

a="Adarsh singh"
b=a[6]
print(b)

#slicing

str="Adarsh singh"
print(str[1:5])
print(str[0:]) # means to the end of string
print(str[:4]) #means that[0:4]
print(str[5:len(str)])
print(str[-5:-1])
print(str[-6:-1])

#String function

str="i am studying python from college"
print(str.endswith("ge")) #print true karega bcoz end of college me ge hai
print(str.endswith("omg")) #print false karega bcoz end of me omg nahi hai
print(str.capitalize()) # 1st letter capital ho jayega
print(str) # simple as it is code print
b= str.capitalize() # benefit of giving a new variable b is that ki anytime we simple print b than 1st letter is capital
print(b)

print(str.replace("o","a")) #replace all o with a
print(str.replace("python","javascript"))
print(str.find("d"))
print(str.find("o")) # first o jaha se start hoga waha ka index de dega
print(str.find("from"))
print(str.find("w")) # no w availabe in str thats why print=-1
print(str.count("from")) # from 1 bar aaya hai to ans 1 aa jayega
print(str.count("o")) # o 3 bar aaya hai to ans 3 aa jayega






















