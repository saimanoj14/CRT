# 1Q)write a python code to count the no.of digits of number ?
# Ex : 15678 --> 5 

# num = int(input("Enter a number :"))
# 
# count = 0 
# while num > 0 :
# 
    # num = num // 10 
    # count += 1
# print("Number of digits in the number is :" , count)
# 


# 2Q) Sum of the digits of a number ?


# num = int(input("Enter a number :"))
# sum = 0 
# while num > 0 :
    # rem = num % 10
    # num = num // 10 
    # sum += rem 
# 
# print("Sum of the digits in the number is :" ,sum) 
# 

# 3Q) Reverse of the number ?

# num = int(input("Enter a number :"))
# rev = 0
# while num > 0 :
    # rem = num % 10 
    # num = num // 10
    # rev = rev * 10 + rem
# 
# print("Reverse of the number is :" , rev)
# 

# 4Q) count the even and odd digits ?


# num = int(input("Enter a number :"))
# even_count = 0 
# odd_count = 0 
# while num > 0 :
    # rem = num % 10 
    # num = num // 10 
    # if rem % 2 == 0 :
        # even_count += 1 
    # else :
        # odd_count += 1 
# 
# print("Even digits count is :" , even_count)
# print("Odd digits counts is :" , odd_count)

# 5Q) print the largest digit in the number ?

num = int(input("Enter a number :"))

largest = 0 

while num > 0 :
    rem = num % 10 
    num = num // 10 
    if rem > largest :
        largest = rem 

print("Largest digit in the number is :", largest)