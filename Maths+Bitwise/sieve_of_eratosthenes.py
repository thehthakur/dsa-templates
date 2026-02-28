import math
from array import array
from typing import Sequence


def sieve_of_eratosthenes(n: int) -> Sequence[int]:
    is_prime: Sequence[int] = array("i", (1 for _ in range(n + 1)))

    # Optimization - 1:
    # If n is at all composite, it will have at least one factor in [2, isqrt(n)]
    for p in range(2, math.isqrt(n) + 1):
        if is_prime[p]:
            # Optimization - 2:
            # Any composite number < p * p, would have already had a
            # prime factor in [2, isqrt(that composite number)]
            # and therefore would have been checked already
            # Take e.g., 45 vs p * p = 49
            for i in range(p * p, n + 1, p):
                is_prime[i] = 0

    primes: Sequence[int] = array("i")
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)

    return primes


if __name__ == "__main__":
    n: int = 1000
    print(sieve_of_eratosthenes(n))
