from typing import List

def Collatz_Sequence(n: int) -> List[int]:
    result = [n]               # Start the sequence with n
    while n != 1:
        if n % 2 == 0:
            n = n // 2         # If even, divide by 2
        else:
            n = 3 * n + 1      # If odd, multiply by 3 and add 1
        result.append(n)
    return result

if __name__ == '__main__':
    n = int(input())
    print(Collatz_Sequence(n))
