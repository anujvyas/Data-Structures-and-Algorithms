# Take the number of rows as an input
row = int(input())

# Validation
if row <= 0 or row > 10:
    print('Invalid input: Enter a number in between 1 to 10.')

# print the pattern
for i in range(0, row):
    for j in range(0, i+1):
        print('*', end='')
    print()         # default adds as new line
