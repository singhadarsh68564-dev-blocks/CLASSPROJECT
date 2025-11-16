# key jo hai list and dict ke alawa kuch bhi ho sakta hai like string, int,float,tuple
# value me ham kuch bhi le sakte hai str,int,float,list,tup

a={"key":"value",
"name":"adarsh",
"learning":"self",
"age":35,
"marks":67.6,
"adult":True,
"subjects":["python","java","ruby","c++"],
"topics":("dict","set")
}
print(a)
print(type(a))
print(a["subjects"])
print(a["topics"])
print(a["name"])
print(a["adult"])
print(a["marks"])
a["name"] ="krish"# yaha name key ka jo value hai wo change hoke krish ho 
print(a)
a["surname"]="singh" # yaha naya key add ho jayega kyuki surname ek naya key hai
print(a)
null_dict={} #print an empty dict
print(null_dict)
null_dict["a"]="ram"
print(null_dict)

# Nested dictionaries

a={"name":"adarsh",
"subjects":{"phy":89,
    "che":97,
    "math":98,}}

print(a)
print(a["name"])
print(a["subjects"]) #yaha subject bhi ek dict hai
print(a["subjects"]["che"]) 

# dictionary method

b={"name":"aniket","village":"kalyanpur","age":20,"height":5.8,"weight":56.93,"goodperson":True,}
print(b.keys())
print(len(b))
print(list(b.keys())) # yaha jo key hai wo list ke form me print hoga 
print(b.values())
print(list(b.values())) # yaha jo values hai wo list ke form me print hoga
print(b.items())
print(list(b.items())) # yaha jo key value pair hai wo list ke form me print hoga list hoga and list ke andar tuple hoga 
pairs=(list(b.items())) # 1 indexing wala key: value pair return karega 
print(pairs[1])
print(b["name"]) 
print(b.get("name"))
# print(b["name2"]) # yaha error aayega
print(b.get("name2")) # yaha None value return hoga # yaha error nahi aayega
print(b["village"])
b.update({"city":"gopalganj"})
print(b)
c={"ps":"baikunthpur","po":"rajapatti"}
b.update(c)
print(b)













