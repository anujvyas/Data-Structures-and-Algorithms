class Solution:
    def reverse(self, arr: list) -> None:
        left_idx = 0
        right_idx = len(arr)-1

        while left_idx < right_idx:
            arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]
            left_idx += 1
            right_idx -= 1


if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    input_arr = [int(x.strip()) for x in input().split(',')]
    sol.reverse(input_arr)
    print('Output: ', input_arr) 
