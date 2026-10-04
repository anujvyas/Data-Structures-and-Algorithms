class Solution:
    def arraySortedOrNot(self, arr):
        prev = arr[0]
        for idx in range(1, len(arr)):
            if arr[idx] < prev:
                return False

            prev = arr[idx]
        return True


if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    input_arr = [int(x.strip()) for x in input().split(',')]
    output = sol.arraySortedOrNot(input_arr)
    print('Output: ', output)
