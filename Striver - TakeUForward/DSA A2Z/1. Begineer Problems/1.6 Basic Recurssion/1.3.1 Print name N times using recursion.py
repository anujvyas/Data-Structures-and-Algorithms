class Solution:
    """
    Default solution class for codebase.
    """

    def print_recurssive_name(self, number, name):
        """
        Method to print the name in a recurssive manner.
        Input: number
        Output: name *number of times
        """
        # Validation
        if number <= 0:
            return

        # Logic
        print(name)
        self.print_recurssive_name(number-1, name)

if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    name = 'anuj'
    sol.print_recurssive_name(int(input()), name)
