class Solution:
    # Method to count number of digits
    def odd_digit_counter(self, number):

        # Validation
        if number < 0:
            return 'Please enter a valid positive number.'

        # Logic
        odd_counter = 0
        while number >= 10:
            digit = number % 10
            number = number // 10

            if digit % 2 == 1:
                odd_counter += 1

        if number % 2 == 1:
            odd_counter += 1

        return odd_counter




if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    output = sol.odd_digit_counter(int(input()))
    print('Output: ', output)