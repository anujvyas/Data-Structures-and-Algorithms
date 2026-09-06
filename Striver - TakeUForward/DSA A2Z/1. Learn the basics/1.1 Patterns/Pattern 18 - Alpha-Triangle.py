# Take the number of rows as an input
row = int(input())

# Validation
if row <= 0 or row > 10:
    print('Invalid input: Enter a number in between 1 to 10.')

# print the up pattern
for i in range(0, row):
    CURR_ASCII = 65 + row-1 - i    # Ascii value for `A` = 65

    # Print right triangle pattern
    for j in range(0, i+1):
        print(chr(CURR_ASCII), end='')
        CURR_ASCII += 1

    print()
