def get_factorial(n: int) -> int:
    """
    Return n! using a for-range loop.
    Works for n >= 0. (0! == 1)
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def sum_odd_numbers(n: int) -> int:
    """
    Return the sum of all odd numbers from 1..n (inclusive)
    using a while loop. Works for n >= 0.
    Example: n=5 -> 1+3+5 = 9
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    total = 0
    k = 1
    while k <= n:
        if k % 2 == 1:
            total += k
        k += 1
    return total
