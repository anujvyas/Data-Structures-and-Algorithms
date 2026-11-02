class Solution:
    def longestCommonPrefix(self, arr: list[str]) -> str:
        # If the array is empty, there is no answer.
        if len(arr) == 0:
            return ''

        # Initialize variables
        longest_common_prefix = arr[0]

        # Iterate through each element
        for item in arr[1:]:
            max_length = min(len(item), len(longest_common_prefix))
            curr_idx = 0

            # Find the breakpoint
            while curr_idx < max_length:
                if longest_common_prefix[curr_idx] != item[curr_idx]:
                    break

                curr_idx += 1

            # If no prefix match
            if curr_idx == 0:
                return ''

            # Trim the longest_common_prefix
            longest_common_prefix = longest_common_prefix[0:curr_idx]

        return longest_common_prefix

if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    arr = [x.strip() for x in input().split(',')]
    output = sol.longestCommonPrefix(arr)
    print('Output: ', output)
