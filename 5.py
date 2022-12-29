# What is the smallest positive number that is evenly
# divisible by all of the numbers from 1 to 20?


def smallest_multiple(arr, x):
    while True:
        for i in arr:
            if x % i != 0:
                break
            elif i == 20:
                return x
        x += 20


arr = list(range(11, 21))
x = 20

print(smallest_multiple(arr, x))
