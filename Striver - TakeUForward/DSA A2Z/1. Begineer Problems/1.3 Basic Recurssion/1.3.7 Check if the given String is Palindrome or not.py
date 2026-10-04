class Solution:
    """
    Default solution class for codebase.
    """

    def palindrome(self, string, i, j):
        """
        Method to check if string is palindrome in a recursive manner.
        Input: string, left, right
        Output: true/false
        """
        # Validation
        if j <= i:
            return True
        elif string[i] != string[j]:
            return False
        else:
            i += 1
            j -= 1
            return self.palindrome(string, i, j)

if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    input_str = input()
    output = sol.palindrome(input_str, 0, len(input_str)-1)
    print("Output: ", output)
