class Solution:
    """
    Default solution class for codebase.
    """

    def factorial(self, num):
        """
        Method to calculate factorial of the numbers in a recurssive manner.
        Input: num
        Output: factorial
        """
        # Validation
        if num == 1:
            return 1

        return num * self.factorial(num-1)

if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    output = sol.factorial(int(input()))
    print("Output: ", output)
