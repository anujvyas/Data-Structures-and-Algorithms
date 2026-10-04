# Take the number of rows as an input
row = int(input())

# Validation
if row <= 0 or row > 10:
    print('Invalid input: Enter a number in between 1 to 10.')

for i in range(0, row*2-1):

    STAR_CNT = i+1 if i < row else 2*row - i - 1

    # print the left pattern
    for j in range(0, STAR_CNT):
        print('*', end='')

    # print space
    SPACE_CNT = row-i-1 if i < row else i-row+1
    for j in range(0, SPACE_CNT*2):
        print(' ', end='')

    # print the right pattern
    for j in range(0, STAR_CNT):
        print('*', end='')

    print()         # default adds as new line
