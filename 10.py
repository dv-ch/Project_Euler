# Find the sum of all the primes below two million.


def prime_num_sum(n):
    # to speed up checking
    x = 3  # start from odd number
    increment = 2  # loop through odd numbers
    sum = 2  # add first prime number

    if n <= 7:
        return "Use simple maths"

    while True:
        is_prime = True

        # this is faster than adding the primes to a list and checking them
        for i in range(3, int((x**0.5) + 1), increment):
            if x % i == 0:
                is_prime = False
                break

        if (x + increment) >= n:
            return sum

        if is_prime:
            sum += x

        x += increment


print(prime_num_sum(2000000))
