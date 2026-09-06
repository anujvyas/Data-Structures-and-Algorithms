# Take the number of rows as an input
row = int(input())

# Validation
if row <= 0 or row > 10:
    print('Invalid input: Enter a number in between 1 to 10.')

for i in range(0, 2*row-1):

    # print the pattern
    for j in range(0, 2*row-1):

        # Calculate distance from all four borders
        top = i
        left = j
        right = 2*row-2-j
        bottom = 2*row-2-i

        print(row - min(top, left, right, bottom), end='')

    print()