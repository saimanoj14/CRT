def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    # Calculate average
    average = (n1 + n2 + n3) / 3
    
    # Truncate to 2 decimal places
    average_truncated = int(average * 100) / 100

    # Determine pass/fail
    status = "Pass" if average_truncated >= 40 else "fail"

    # Dynamic formatting: 1 decimal if whole number, else 2 decimals
    if average_truncated == int(average_truncated):
        avg_str = f"{average_truncated:.1f}"
    else:
        avg_str = f"{average_truncated:.2f}"

    return f"Average grade: {avg_str}, Status: {status}"

if __name__ == '__main__':
    name = input()
    n1, n2, n3 = list(map(int, input().split()))
    print(Student_Grade_System(name, n1, n2, n3))
