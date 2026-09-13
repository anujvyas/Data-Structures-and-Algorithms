class Solution:
    """
    Default solution class for codebase.
    """

    def print_recurssive_numbers(self, start, end):
        """
        Method to print the numbers in a recurssive manner.
        Input: start, end
        Output: 1 to n
        """
        # Validation
        if start > end:
            return

        # Logic
        print(start)
        self.print_recurssive_numbers(start+1, end)

if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    sol.print_recurssive_numbers(1, int(input()))
