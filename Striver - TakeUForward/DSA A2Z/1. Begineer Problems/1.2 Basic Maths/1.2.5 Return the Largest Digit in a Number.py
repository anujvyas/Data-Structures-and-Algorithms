class Solution:
    # Method to count number of digits
    def largestDigit(self, n):

        # Logic
        largest_digit = 0
        while n >= 10:
            digit = n % 10
            n //= 10

            if digit > largest_digit:
                largest_digit = digit

        if n > largest_digit:
            return n

        return largest_digit


if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    output = sol.largestDigit(int(input()))
    print('Output:', output)