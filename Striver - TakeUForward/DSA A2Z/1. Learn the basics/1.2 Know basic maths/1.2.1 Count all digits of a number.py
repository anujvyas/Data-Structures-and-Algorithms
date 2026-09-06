class Solution:
    # Method to count number of digits
    def digit_counter(self, number):

        # Validation
        if number < 0:
            return 'Please enter a valid positive number.'

        # Logic
        counter = 0
        while number > 10:
            number = number / 10
            counter += 1

        return counter+1




if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    output = sol.digit_counter(int(input()))
    print('Output: ', output)