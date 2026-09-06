class Solution:
    # Method to reverse digits of a number
    def reverse_digit(self, number):

        # Validation
        if number < 0:
            return 'Please enter a valid positive number.'

        # Logic
        reverse_num = 0

        while number > 0:
            digit = number % 10
            reverse_num = reverse_num*10 + digit

            number = number // 10

        return reverse_num




if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    output = sol.reverse_digit(int(input()))
    print('Output: ', output)