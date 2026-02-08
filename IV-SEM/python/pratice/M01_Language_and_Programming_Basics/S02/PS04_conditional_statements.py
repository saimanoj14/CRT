# read a number from user and check is it is +ve , -ve , zero 

# input : 10 , -20 , 0 
# output : positive , negative , zero 

x  = int(input())

if x > 0: 
    print("positive")

elif x < 0  :
    print("negative")
else :
    print("zero")