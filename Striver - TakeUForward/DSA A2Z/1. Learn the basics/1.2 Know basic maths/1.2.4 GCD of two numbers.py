class Solution:
    """
    Default solution class for codebase.
    """

    def find_gcd(self, num1, num2):
        """
        Method to find GCD for 2 numbers
        Input: number
        Output: GCD
        """
        if num1 < num2:
            min_num = num1
            max_num = num2
        else:
            min_num = num2
            max_num = num1

        if max_num % min_num == 0:
            return min_num      # Already found the GCD

        # Logic
        for i in range(int(min_num**0.5), 0, -1):
            if min_num % i == 0 and max_num % i == 0:
                return i

        return 1




if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    output = sol.find_gcd(int(input()), int(input()))
    print('Output: ', output)
