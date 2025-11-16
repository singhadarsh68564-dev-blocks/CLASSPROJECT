# if
age=21
if(age>=18):
    print("can vote & apply for license")
age1=17
if(age1>=18):
    print("can vote & apply for license") # nothing will print
age=21
if(age>=18):
    print("can vote")
    print("can drive")
    print("could murder")
    
# elif

light="green"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go") # go print kar dega 
elif(light=="yellow"):
    print("look")

#  else

light1="pink"
if(light1=="red"):
    print("stop")
elif(light1=="green"):
    print("go")  
elif(light1=="yellow"):
    print("look")
else:
    print("light is broken")

age=24
if(age>=18):
    print("can vote")
else:
    print("cannot vote")

age=16
if(age>=18):
    print("can vote")
else:
    print("cannot vote")

#nesting
 
age=34
if(age>=18):
    if(age>=80): # agar ye sahi hua to ye print karega
        print("cannot drive")
    else:
        print("can drive")

age=97
if(age>=18):
    if(age>=80): 
        print("cannot drive")
    else:
        print("can drive")
















