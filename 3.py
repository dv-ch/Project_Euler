# Largest prime factor of 600851475143


def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


n = 15

print(largest_prime_factor(n))
