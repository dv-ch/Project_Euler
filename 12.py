# What is the value of the first triangle number
# to have over five hundred divisors?


def triangle_number(n):
    count = 1
    div = 0
    t_num = 0

    if n == 0:
        return 1

    while True:
        t_num += count

        upper_divisor = t_num

        for i in range(1, t_num):
            if i >= upper_divisor:
                break
            if t_num % i == 0:
                div += 2
                upper_divisor = t_num / i

        if div > n:
            return t_num
        else:
            div = 0

        count += 1


print(triangle_number(500))
