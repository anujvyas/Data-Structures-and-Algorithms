class Solution:
    def isPrime(self, n: int) -> bool:
        divisors = []
        for i in range(1, int(n**0.5) + 1):

            if n % i == 0:
                divisors.append(i)

                if n/i != i:
                    divisors.append(n//i)

            if len(divisors) > 2:
                return False

        return True

    def sieve(self, n: int, arr: list):
        for idx in range(n*2, len(arr), n):
            arr[idx] = False

    def primeUptoN(self, n: int) -> int:
        if n < 2:
            return 0
        elif n == 2:
            return 1

        # Initialize array of boolean
        prime_arr = [2]
        sieve_arr = [True]*(n+1)
        sieve_arr[0] = sieve_arr[1] = False

        for i in range(3, n+1, 2):
            if sieve_arr[i] == True and self.isPrime(i):
                # Set all multiples of i to false
                prime_arr.append(i)
                self.sieve(i, sieve_arr)

        return len(prime_arr)

if __name__ == '__main__':
    # Create solution object
    sol = Solution()
    output = sol.primeUptoN(int(input()))
    print('Output: ', output)
