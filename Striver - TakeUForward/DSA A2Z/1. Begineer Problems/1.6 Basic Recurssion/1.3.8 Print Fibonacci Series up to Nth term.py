class Solution:
    """
    Default solution class for codebase.
    """

    def fibonacci(self, max_idx, fibo_arr, curr_idx):

        # Validation
        if curr_idx > max_idx:
            return fibo_arr

        fibo_arr.append(fibo_arr[curr_idx-1] + fibo_arr[curr_idx-2])
        curr_idx += 1
        return self.fibonacci(max_idx, fibo_arr, curr_idx)

if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    fibo = [0, 1]
    output = sol.fibonacci(int(input()), fibo, 2)
    print("Output: ", output)
