# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(4)

# def show(n):
#     if(n==-7):
#         return
#     print(n)
#     show(n-2)
# show(5)

def fact(n):
    if(n==1 or n==0):
        return  1
    return fact(n-1)*n
print(fact(4))
print(fact(5))

#  Write a recursive function to calculate the sum of first n natural numbers.

def calcsum(n):
    if(n==0):
        return 0
    return calcsum(n-1)+n
print(calcsum(5))

# write a recursive function to print all element in a list.hint=use list & index as parameters.

def list_(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    list_(list,idx+1)
fruits=["apple","mango","litchi","guava"]
list_(fruits)
