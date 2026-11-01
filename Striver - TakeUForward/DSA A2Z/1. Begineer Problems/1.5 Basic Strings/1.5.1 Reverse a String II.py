class Solution:
    def reverseString(self, arr: list[str]) -> str:
        # If the array is empty, there is no answer.
        if len(arr) == 0:
            return ''

        left_ptr = 0
        right_ptr = len(arr)-1

        while left_ptr < right_ptr:
            arr[left_ptr], arr[right_ptr] = arr[right_ptr], arr[left_ptr]
            left_ptr += 1
            right_ptr -= 1

        return ''.join(arr)

if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    input_arr = [x for x in input().strip()]
    output = sol.reverseString(input_arr)
    print('Output: ', output)
