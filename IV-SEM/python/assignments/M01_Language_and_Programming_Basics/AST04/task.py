def Reverse_String(s: str) -> str:
    reversed_s = ""           # Start with empty string
    for char in s:
        reversed_s = char + reversed_s  # Prepend each character
    return reversed_s

if __name__ == '__main__':
    s = input()
    print(Reverse_String(s))
