from collections import defaultdict

class Solution:
    def sumHighestAndLowestFrequency(self, arr: list[int]) -> int:
        # If the array is empty, there is no answer.
        if len(arr) == 0:
            return -1

        highest_frequency = 0
        lowest_frequency = len(arr) + 1
        frequency_hash = defaultdict(int)    # num: freq; default 0

        for i in arr:
            frequency_hash[i] += 1
            current_freq = frequency_hash[i]

            if current_freq > highest_frequency:
                highest_frequency = current_freq

        for freq in frequency_hash.values():
            if freq < lowest_frequency:
                lowest_frequency = freq

        return highest_frequency + lowest_frequency

if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    input_arr = [int(x.strip()) for x in input().split(',')]
    output = sol.sumHighestAndLowestFrequency(input_arr)
    print('Output: ', output)
