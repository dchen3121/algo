# Write a function fib() that takes an integer n and returns the n-th Fibonacci number.


def fib(n: int) -> int:
    memo = [None for _ in range(n + 1)]
    memo[1], memo[2] = 1, 1

    def fib_help(n: int) -> int:
        if memo[n]:
            return memo[n]
        result = fib_help(n - 1) + fib_help(n - 2)
        memo[n] = result
        return result

    return fib_help(n)
