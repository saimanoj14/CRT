a = list(map(int , input().split()))
a.sort()
target = int(input())
for i in a : 

    left = 0 
    right = len(a) - 1 

    while left <= right : 

        mid = (left + right ) // 2

        if a[mid] > target  : 

            right -= -1
            
        elif a[mid] < target : 

            left += 1 
        elif a[mid] == target : 
            print("found" , a[mid]) 

            break ; 


        
        