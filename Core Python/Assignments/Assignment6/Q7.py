n = 5
for i in range(n):
    # Print leading spaces for pyramid alignment
    print("  " * (n - i - 1), end="")
    # Print odd number of alphabets per row
    for j in range(2 * i + 1):
        print(chr(65 + j), end=" ")
    print()