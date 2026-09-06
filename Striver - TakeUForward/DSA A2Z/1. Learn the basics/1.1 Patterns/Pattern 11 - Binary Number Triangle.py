# Take the number of rows as an input
row = int(input())

# Validation
if row <= 0 or row > 10:
    print('Invalid input: Enter a number in between 1 to 10.')


for i in range(0, row):

    # Decide the starting binary value for the current row
    PRINT_NUM = 1 if i % 2 == 0 else 0

    # Print pattern
    for j in range(0, i+1):
        print(PRINT_NUM, end='')
        PRINT_NUM = 1 if PRINT_NUM == 0 else 0

    print()
