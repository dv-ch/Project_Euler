# Find the difference between the sum of the
# squares of the first one hundred natural numbers
# and the square of the sum.


def sum_square_difference():
    x, y = 0, 0

    for i in range(1, 101):
        x += i * i
        y += i

    y *= y

    return y - x


print(sum_square_difference())
