class Solution:
    def palindromeCheck(self, s: str) -> bool:
        # If the string is empty, there is no answer.
        if len(s) == 0:
            return False

        left_ptr = 0
        right_ptr = len(s)-1

        while left_ptr < right_ptr:
            if s[left_ptr] != s[right_ptr]:
                return False

            left_ptr += 1
            right_ptr -= 1

        return True

if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    input_str = input().strip()
    output = sol.palindromeCheck(input_str)
    print('Output: ', output)
