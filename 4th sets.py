a={1,2,3,"hello",78.6,True,False,(3,"hello")}
print(a)
print(type(a))
b={1,2,2,2,2,"hello","hello","hello","good","good",(4,"hello","hello"),(4,"hello","hello")}
print(b) # set me jo bhi repated hota hai wo ek bar hi output me aata hai
print(len(b)) # repeated or duplicated value can't calculated in length
c={} # this is empty dict not set
print(type(c))
d=set() # this is how we create an empty set
print(type(d))
print(d)

# sets method

sets=set()
sets.add(1) # ek bar me ek hi element add kar sakte hai
print(sets)
print(sets.add(3)) # aise karne par set me element add nahi hoga NONE return hoga as a output
print(sets)  # ab sets me 3 add ho gya print karne par it means pehle add karo phir print karo
sets.add((3,4,5.3,"hello","hello"))
sets.add(67)
sets.add("adarsh")
sets.add((3,4,5.3,"hello","hello")) # duplicate item do bar add nahi hota 
#  ye list hai add nahi ho sakta = sets.add([5,"good"])
print(sets)

sets.remove(67)
print(sets)
#sets.remove(5) # yaha key error aayega bcoz ye element set me nahi hai
print(len(sets))
sets.clear()
print(sets)
print(len(sets))

aa={1,2,3,5,6,"hello","bye","coding",(2,"python","morning")}
# print(aa.pop()) # kisi random value ko print kra raha hai
aa.pop() # koi random value remove kar rha hai
aa.pop() # do bar pop likhne se do koi value hta diya
print(aa)

set1={3,4,5,"hello","love",(5,"kite","pyar"),"shampoo","soap"}
set2={4,5,"soap","love",(5,3.6),58.36,"adarsh","dhoka"}
set1.discard(4) # remove specified element
print(set1)
print(set1.union(set2)) # ye ek naya set return karega jo union hoga set1 and set2 ka
print(set1|set2) # ye ek naya set return karega jo union hoga set1 and set2 ka
print(set1) # union karne ke bad set1 print karenge to set1 as it is return karega 
print(set1.intersection(set2))
print(set1&set2)
print(set1.difference(set2))
print(set1-set2)
print(set1.symmetric_difference(set2))
print(set1^set2)













