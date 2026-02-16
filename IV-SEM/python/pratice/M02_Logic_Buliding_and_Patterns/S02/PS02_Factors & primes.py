# # 1Q)find factors of the number given by user ?

n = int(input("Enter a number : "))
count = 0 
for i in range(1 , n + 1) :
    if (n % i == 0) :
        count += 1 
        print(i)
print(count)


# 2Q) REVERSE INTEGER from  LEET CODE 

n = int(input("Enter a number : "))
if n >= 0 : 
    print(int(str(n)[::-1]))
else :
    n = -1 * n 
    print(-1*(int(str(n)[::-1])))

# 3Q) Given nuber is a prime or not ? 

n = int(input("Enter a number :"))
count = 0 
for i in range(1 , n + 1) :
    if (n % i ==  0) :
        count += 1    
if count == 2 :
    print("Given number is a prime number.")
else :
    print("Given number is not a prime number.")