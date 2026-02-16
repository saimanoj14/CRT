# 1Q)  Read a and d from user and dispaly upto 10  ( Arithmetic series ) ? 

a , d = map(int , input().split())
for i in range(10) :
    print(a + i * d , end = " ")



# 2Q) Fibonacci series ==> 0 , 1 ((Recursive , List , Memorization ) techniquest used)

# n values 
# n = 5 
# 0 1 1 2 3 
n = int(input())
a = 0 
b = 1 
for i in range(n) :
    print(a , end = " ")
    a , b = b , a + b 

                                  #    (OR)  



n = int(input())
li = [0 , 1] 

for i in range(2 , n) :

    li.append(li[i-2] + li[i-1])

print(li)



# 3Q) Power of a number till (10) numbers ?

#  n = 2 
#  o/p : 2 , 4 , 8 , 16 , ..


n = int(input())
for i in range(11) :
    print(n ** i , end = " ")