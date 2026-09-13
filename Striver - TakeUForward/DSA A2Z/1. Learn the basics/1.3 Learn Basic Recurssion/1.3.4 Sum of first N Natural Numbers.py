class Solution:
    """
    Default solution class for codebase.
    """

    def sum_recurssive(self, curr, num):
        """
        Method to sum the numbers in a recurssive manner.
        Input: curr, num
        Output: total
        """
        # Validation
        if curr == num:
            return curr

        return curr + self.sum_recurssive(curr+1, num)

if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    output = sol.sum_recurssive(1, int(input()))
    print("Output: ", output)
