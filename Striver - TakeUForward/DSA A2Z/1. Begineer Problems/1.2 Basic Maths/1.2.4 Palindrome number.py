class Solution:
    """
    Default solution class for codebase.
    """

    def check_palindrome(self, number):
        """
        Method to check if a number is palindrome or not
        Input: number
        Output: Palindrome or Not
        """
        # Validation
        if number < 0:
            return 'Please enter a valid positive number.'

        # Logic
        reverse_num = 0
        original_num = number

        while number > 0:
            digit = number % 10
            reverse_num = reverse_num*10 + digit

            number = number // 10

        return 'Palindrome' if reverse_num == original_num else 'Not Palindrome'




if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    output = sol.check_palindrome(int(input()))
    print('Output: ', output)
