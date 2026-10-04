# Take the number of rows as an input
row = int(input())

# Validation
if row <= 0 or row > 10:
    print('Invalid input: Enter a number in between 1 to 10.')


PRINT_NUM = 1
for i in range(0, row):

    # Print right triangle pattern
    for j in range(0, i+1):
        print(PRINT_NUM, end='')
        PRINT_NUM += 1

    print()
