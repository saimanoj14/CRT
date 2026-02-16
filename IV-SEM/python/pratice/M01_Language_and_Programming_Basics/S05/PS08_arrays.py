import numpy as np
arr = np.array([10,20,30])
print(arr)
print(np.max(arr))
print(np.min(arr))
print(np.sum(arr))
print(np.mean(arr))
print("Even numbers list :" , np.arange(2 , 10 , 2))
print("Odd numbers List :" , np.arange(1 , 10 , 3))



n = int(input("Enter the size of the array :"))
elements = list(map(int ,input("enter elements of the array :").split()))
print("Array elements are :" , np.array(elements))
print("Sum of the user array input elements is :" , np.sum(elements))






# Q)Third maximum number ?

l = list(map(int , input("enter the elements of the array :").split()))
if len(l) < 3 :
    print(max(l))
else :
    print("Third maximum number is :" , np.sort(l)[-3])




# Q) Monotonic array : elements are in increasing or decreasing order ?

def is_monotonic(array) :
    return (all(array[i] <= array[i + 1] for i in range(len(array) - 1)) or all(array[i] >= array[i + 1] for i in range(len(array) - 1)))

array = list(map(int , input("enter the elements of the array :").split()))
print("Is the array monotonic ? :" , is_monotonic(array))

