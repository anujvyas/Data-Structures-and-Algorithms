from collections import defaultdict

class Solution:
    def secondMostFrequentElement(self, arr: list) -> None:
        # If the array is empty, there is no answer.
        if len(arr) == 0:
            return -1

        max_frequency = -1
        frequency_hash = defaultdict(int)    # num: freq; default 0

        # Generate frequency_hash + find max_frequency
        for i in arr:
            frequency_hash[i] += 1
            current_freq = frequency_hash[i]

            # Found a num with greater frequency
            if current_freq > max_frequency:
                max_frequency = current_freq
        print(frequency_hash)

        # Find the second highest frequency value
        answer = -1
        second_highest_frequency = -1
        for k in frequency_hash.keys():
            curr_frequency = frequency_hash[k]

            if curr_frequency < max_frequency:
                # Update answer only if small
                if answer == -1 or (k < answer and second_highest_frequency == curr_frequency) or (second_highest_frequency < curr_frequency):
                    answer = k
                    second_highest_frequency = curr_frequency

        return answer

if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    input_arr = [int(x.strip()) for x in input().split(',')]
    output = sol.secondMostFrequentElement(input_arr)
    print('Output: ', output)
