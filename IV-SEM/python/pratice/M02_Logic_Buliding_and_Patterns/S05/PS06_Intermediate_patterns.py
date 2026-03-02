'''
li = [1,2,3,4,5]
o/p : [1,4,9,16,25]
'''

# a = list(map(int , input().split()))
# l = list()
# for i in a :
#     r = i * i

#     l.append(r)


# print(l)

# ans = [i ** 2 for i in a]
# print(ans)

# even_odd = [i for i in a if i % 2 == 0]
# print(even_odd)




''' li = [a , b , c]

o/p : 'a b c'
'''


# li = ['a' ,'b' , 'c']

# res = ""

# for ch in li :

#     res = res + ch + " "
    
# print(res)

# print(" ".join(li))


''' 1.Pyramid
    n = 4 
    o/p :

    * 
   * * 
  * * *
 * * * * 

'''


# n = int(input())

# for i in range(1 , n + 1) :

#     print(" " * (n - i) + "* " * i)


'''2.Invert pyramid
  o/p  :

  * * * * 
   * * * 
    * * 
     * 

'''

# n = int(input())

# for i in range(1 , n + 1) :

#     print(" *" * (n - i))


'''3.Diamond
n = 4 
o/p : 

   * 
  * * 
 * * * 
* * * * 
 * * * 
  * * 
   * 

'''

# n = int(input())
# for i in range(1 , n + 1) :
#     print(" " * (n - i) + "* " * i)

# for i in range(n - 1 , 0 , -1) :
#     print(" " * (n - i) + "* " * i) 


# n = int(input())

# for i in range(1 , n + 1) :
#     print(" " * (n - i) , end = "" )

#     for j in range(1 , i + 1) : 

#         print(j , end = " ")

#     print()


# for i in range(n - 1 , 0 , -1) :
#     print(" " * (n - i) , end = "")

#     for j in range(1 , i + 1) :
#         print(j , end = " ")

#     print()
 

# n = int(input())
# k = 0
# for i in range(1 , n + 1) :
#     print(" " * (n - i) , end = "" )

#     for j in range(1 , i + 1) : 
#         k = k + 1
#         print(k , end = " ")

#     print()


# for i in range(n - 1 , 0 , -1) :
#     print(" " * (n - i) , end = "")

#     for j in range(1 , i + 1) :
#         k = k + 1
#         print(k , end = " ")

#     print()




# n = int(input())

# for i in range(1 , n + 1) : 

#     print(" " * (n - i) + " ".join([str(k) for k in range(1 , i + 1)]))


# for i in range(n - 1 , 0 , -1) :

#     print(" " * (n - i) + " ".join([str(k) for k in range(1 , i + 1)]))

n = int(input())

for i in range(1 , n + 1) : 

    print(" " * (n - i) + " ".join([str(i) for k in range(1 , i + 1)]))


for i in range(n - 1 , 0 , -1) :

    print(" " * (n - i) + " ".join([str(i) for k in range(1 , i + 1)]))















  