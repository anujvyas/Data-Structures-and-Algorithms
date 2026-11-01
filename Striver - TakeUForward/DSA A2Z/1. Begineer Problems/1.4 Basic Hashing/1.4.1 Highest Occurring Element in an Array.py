from collections import defaultdict

class Solution:
    def mostFrequentElement(self, arr: list) -> None:
        # If the array is empty, there is no answer.
        if len(arr) == 0:
            return -1

        max_frequency = -1
        frequent_value = -1
        frequency_hash = defaultdict(int)    # num: freq; default 0

        for i in arr:
            frequency_hash[i] += 1
            current_freq = frequency_hash[i]

            # Found a num with greater frequency or equal freq but smaller
            if (current_freq > max_frequency) or (current_freq == max_frequency and i < frequent_value):
                frequent_value = i
                max_frequency = current_freq

        return frequent_value

if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    input_arr = [int(x.strip()) for x in input().split(',')]
    output = sol.mostFrequentElement(input_arr)
    print('Output: ', output)
