class Solution:
    def sum(self, arr):
        total = 0
        for element in arr:
            total += element

        return total


if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    arr = [int(x.strip()) for x in input().split(',')]
    output = sol.sum(arr)
    print('Output: ', output)
