class Solution:
    """
    Default solution class for codebase.
    """

    def reverse_array(self, arr, i, j):
        """
        Method to reverse an array in a recurssive manner.
        Input: arr, left, rigth
        Output: reverse
        """
        # Validation
        if j <= i:
            return arr

        # swap
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
        return self.reverse_array(arr, i, j)

if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    input_arr = list(map(int, input().split(',')))
    output_arr = sol.reverse_array(input_arr, 0, len(input_arr)-1)
    print("Output: ", output_arr)
