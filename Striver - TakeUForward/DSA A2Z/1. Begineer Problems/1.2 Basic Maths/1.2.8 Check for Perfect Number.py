class Solution:
    """
    Default solution class for codebase.
    """

    def isPerfect(self, n: int) -> bool:
        divisors = []

        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)

                if n/i != i and n/i != n:
                    divisors.append(n//i)

        # sum of all perfect divisors
        total = 0
        for div in divisors:
            total += div

        return True if n == total else False

if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    output = sol.isPerfect(int(input()))
    print('Output:', output)
