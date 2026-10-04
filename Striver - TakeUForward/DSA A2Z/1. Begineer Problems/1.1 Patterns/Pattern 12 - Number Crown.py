# Take the number of rows as an input
row = int(input())

# Validation
if row <= 0 or row > 10:
    print('Invalid input: Enter a number in between 1 to 10.')


for i in range(0, row):

    # Print right triangle pattern
    for j in range(0, i+1):
        print(j+1, end='')

    # Print space
    for k in range(0, (row - (i+1))*2):
        print(' ', end='')

    # Print reverse triangle
    for l in range(i+1, 0, -1):
        print(l, end='')

    print()
