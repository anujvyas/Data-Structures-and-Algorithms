class Solution:
    def countOdd(self, arr):
        count = 0
        for element in arr:
            if element % 2 == 1:
                count += 1

        return count


if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    input = [int(x.strip()) for x in input().split(',')]
    output = sol.countOdd(input)
    print('Output: ', output)
