# Take the number of rows as an input
row = int(input())

# Validation
if row <= 0 or row > 10:
    print('Invalid input: Enter a number in between 1 to 10.')

# print the up pattern
stars = 0
for i in range(0, 2*row-1):
    # calculate stars
    if i < row:
        stars += 1
    else:
        stars -= 1

    # Print *
    for j in range(0, stars):
        print('*', end='')

    print()
