'''
1Q)
input : 4 

output : 

* * * * 
* * * * 
* * * *
* * * *
'''

# n = int(input())

# for i in range(n) : 
#     for i in range(n) :
#         print("*" , end = " ")

#     print()

'''
2Q) n = 4 

* 
* * 
* * * 
* * * *  

'''

# n = int(input())

# for i in range(n) :

#     for i in range(i + 1) :
#         print("*" , end = " ")

#     print()

''' 
3Q) 

n = 4 

output : 

* * * * 
* * * 
* * 
* 

''' 

# n = int(input())

# for i in range(n) :

#     for j  in range(n - i) :
#         print("*" , end = " ")

#     print()


'''
4Q) 
n = 4 
output : 

1 
2 3 
4 5 6 
7 8 9 10

'''



n = int(input())
k += 1 
for i in range(n) :

    for j in range(i + 1) :

        print(k + 1, end = " ")

        k += 1 

    print()