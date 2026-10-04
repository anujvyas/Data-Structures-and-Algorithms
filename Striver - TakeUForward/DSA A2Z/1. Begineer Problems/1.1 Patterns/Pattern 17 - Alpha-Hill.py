# Take the number of rows as an input
row = int(input())

# Validation
if row <= 0 or row > 10:
    print('Invalid input: Enter a number in between 1 to 10.')

for i in range(0, row):
    CURR_ASCII = 65    # Ascii value for `A` = 65

    # Print spaces
    for j in range(0, row-i-1):
        print(' ', end='')

    # Print pattern
    for k in range(0, i*2+1):
        print(chr(CURR_ASCII), end='')

        # Calculate ascend or descend
        if k >= i:
            CURR_ASCII -= 1
        else:
            CURR_ASCII += 1

    print()
