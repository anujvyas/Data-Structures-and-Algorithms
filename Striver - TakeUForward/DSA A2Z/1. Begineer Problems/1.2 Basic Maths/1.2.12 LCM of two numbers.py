class Solution:
    """
    Default solution class for codebase.
    """

    def find_lcm(self, num1, num2):
        """
        Method to find GCD for 2 numbers
        Input: number
        Output: LCM
        """
        if num1 < num2:
            min_num = num1
            max_num = num2
        else:
            min_num = num2
            max_num = num1

        if max_num % min_num == 0:
            return max_num      # Already found the GCD

        # Logic
        for i in range(max_num+1, max_num * min_num):
            if i % min_num == 0 and i % max_num == 0:
                return i

        return max_num * min_num


if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    output = sol.find_lcm(int(input()), int(input()))
    print('Output: ', output)
