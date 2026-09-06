class Solution:
    """
    Default solution class for codebase.
    """

    def check_prime(self, number):
        """
        Method to check if number is prime or not
        Input: number
        Output: True/False
        """
        # Validation
        if number < 0:
            return 'Please enter a valid positive number.'

        # Logic
        divisors = []
        for i in range(1, int(number**0.5) + 1):

            if number % i == 0:
                divisors.append(i)

                if number/i != i:
                    divisors.append(number//i)

            if len(divisors) > 2:
                return False

        return True

if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    output = sol.check_prime(int(input()))
    print('Output: ', output)
