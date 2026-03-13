'''
Python collection 
list :

leet code problems : (169 , 88 , 217)


tuples : 
.Immutable 
.Accessing 
.Concatenation
.Nesting of tuples 
.Repetition of tuples 
.Slicing of tuples 
.Deleting a tuple 

leetcode problems : (349 , 657)

'''


a = [1 , 23 , 45 , 68]
print(a)
b = list((1 , 23 , 45, 7 , 98))
print(b)

# 2)Accessing of list : Index 0 , -1 

a = [1,23,45,68]

print(a[1])
print(a[2])


# creating list with Repated elements 

a = [1 , 2, 3]

print(a * 2)


# adding elements to a list 

a = [1,2,3]
a.append(50)
a.insert(1 , 20)
print(a)

# Remove elements from list 

b = list((1 , 23 , 4 , 5 , 7 , 98))
print(b)
b.remove(7)
print(b)
b.pop()
print(b)
b.clear()
print(b)



