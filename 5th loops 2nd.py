# list=[1,2,3,4,5,6]
# for element in list:
#     print("list",element)

# items=[1,2,89.5,True,"potato","hello"]
# for element in items :
#     print("items",element)

# tup=(1,2,3,5,6)
# for num in tup:
#     print("tup",num)

# str="adarsh singh son of ashok singh"
# for alphabet in str:
#     print(alphabet)
# else:
#     print("END")


str="adarsh singh son of ashok singh"
for alphabet in str:
    print(alphabet)
    if(alphabet=="s"):
        print("found")
        break
else: # yaha end print nahi hoga kyuki kyuki break wala use kiya hai yahi direct print kiya hota end to print ho jata.
    print("END")


# ques 1
# print the elements of the following list using a loop:[1,4,9,16,25,36,49,64,81,100]
# list=[1,4,9,16,25,36,49,64,81,100]
# for value in list:
#     print(value)

# ques 2
# search for a number X in this tuple using loop:[1,4,9,16,25,36,49,64,81,100]
# tup=(1,4,9,16,25,36,49,64,81,100)
# X=49
# idx=0
# for num in tup:
#     if(num==X):
#         print("found",idx)
#     idx+=1    

# RANGE

'''range function return a sequence of numbers, staarting from 0 by
by default, and increments by 1(by default),and stop before a specified number.'''

#print(range(5))
# seq=range(5)
# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])
# print(seq[4])
# ye print nahi hoga kyuki ek kam hota hai range function me jitna ham range ke andar number dalte hai print(seq[5])
# seq=range(5) # range me last wala number include nahi hota
# for num in seq:
#     print(num)

# for num in range(10): # yaha hamne stop diya hai 10 by default start 0 hai
#     print(num)

# for num in range(2,10): # yaha start and stop dono hamne diya hai start include hota hai, stop include nahi hota
#     print(num)

# for num in range(2,10,2): # yaha start and stop and step teeno hamne diya hai, step ka matlab kitne se increase hoga
#     print(num)

# for i in range(1,101):
#      print(i)

# for i in range(100,0,-1):
#     print(i)

# ques: print the multiplication table of a number n.
# a=int(input("enter a number:"))
# for i in range(1,11):
#     print(a*i) # yaha a=12 liya and output me 12 ka table print ho gya

# PASS STATEMENT:
''' pass is a null statement that does nothing. it is used as a placeholder for future code.'''

# for i in range(5):
#     pass

# print("hello")


# ques=WAP to find the sum of first n natural numbers.(using while)

# n=5
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print("total sum :",sum)

# n=7
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)

# ques = WAP to find the factorial of first n natural numbers.(using for)

# n=5
# facto=1
# i=1
# while i<=n:
#     facto*=i
#     i+=1
# print(facto)

# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)










