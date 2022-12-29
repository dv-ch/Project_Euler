# Find the sum of the even-valued terms in the Fibonacci sequence below 4000000.

x, y, z = 1, 1, 0

while x < 4000000:
    x, y = y, x + y
    if x % 2 == 0:
        z += x

print(z)
