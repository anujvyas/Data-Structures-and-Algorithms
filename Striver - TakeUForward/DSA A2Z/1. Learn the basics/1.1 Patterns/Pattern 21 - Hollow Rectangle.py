# Take the number of rows as an input
row = int(input())

# Validation
if row <= 0 or row > 10:
    print('Invalid input: Enter a number in between 1 to 10.')

for i in range(0, row):

    # print the pattern
    for j in range(0, row):
        if i%(row-1) == 0 or j%(row-1) == 0:
            print('*', end='')
        else:
            print(' ', end='')

    print()         # default adds as new line
