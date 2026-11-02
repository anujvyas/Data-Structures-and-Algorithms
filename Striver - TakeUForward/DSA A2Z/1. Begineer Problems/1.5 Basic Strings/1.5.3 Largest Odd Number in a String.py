class Solution:
    def largeOddNum(self, s: str) -> str:
        # If the string is empty, there is no answer.
        if len(s) == 0:
            return ''

        # Initialize pointers
        left_ptr = 0
        right_ptr = len(s)-1

        # Find the rightmost odd digit
        while right_ptr > -1:
            if int(s[right_ptr]) % 2 == 1:
                break
            right_ptr -= 1

        # Check if the right pointer has valid index
        if right_ptr != -1:
            # Skip all the left zeros
            while left_ptr <= right_ptr:
                if int(s[left_ptr]) != 0:
                    break
                left_ptr += 1

            return s[left_ptr:right_ptr+1]

        return ''

if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    input_str = input().strip()
    output = sol.largeOddNum(input_str)
    print('Output: ', output)
