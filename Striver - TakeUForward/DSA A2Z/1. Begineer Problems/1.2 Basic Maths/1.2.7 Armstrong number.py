class Solution:
    """
    Default solution class for codebase.
    """

    def check_armstrong(self, number):
        """
        Method to check if a number is Armstrong number or not
        Input: number
        Output: True or False
        """
        # Validation
        if number < 0:
            return 'Please enter a valid positive number.'

        # Logic
        original_num = number
        new_num = 0

        while number > 0:
            digit = number % 10
            new_num += digit ** 3

            number = number // 10

        return new_num == original_num



if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    output = sol.check_armstrong(int(input()))
    print('Output: ', output)
