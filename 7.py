# What is the 10,001st prime number?


def prime_num_generator(n):
    x = 3  # start from odd numbers only
    count = 1  # includes the first prime number (2)

    if count == n:
        return 2

    while True:
        is_prime = True

        for i in range(3, int((x**0.5) + 1), 2):
            if x % i == 0:
                is_prime = False
                break

        if is_prime:
            count += 1

        if count == n:
            return x

        x += 2  # loop through odd numbers only


print(prime_num_generator(10000))
