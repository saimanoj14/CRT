def Student_Grade_System(name:str,n1: int,n2: int,n3: int) -> str:
   


if __name__ == '__main__':
    name = input()
    n1,n2,n3 = list(map(int,input().split()))
    print(Student_Grade_System(name,n1,n2,n3))


Calculate and store student grades for various subjects.

This project stores student grades for various subjects, calculates their average, and determines their final grade. The user can input subject marks, and the system calculates the overall result (pass/fail).

Input: Student name and grades for multiple subjects(3).
Output: Student’s average grade and status (pass/fail).