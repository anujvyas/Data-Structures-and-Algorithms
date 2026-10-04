class Solution:
    """
    Default solution class for codebase.
    """

    def print_divisors(self, number):
        """
        Method to print all divisors of a number
        Input: number
        Output: List of divisors
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

        divisors.sort()
        return divisors

if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    output = sol.print_divisors(int(input()))
    print('Output: ', output)
