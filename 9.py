# Pythagorean triplet


def pythagorean_triplet():
    a = 1
    while True:
        b = a + 1

        while True:
            c = b + 1

            if a + b + c > 1000:
                break

            while True:
                if a + b + c < 1000:
                    c += 1
                    continue
                elif (a * a) + (b * b) != (c * c):
                    break

                return a * b * c

            b += 1

        a += 1


print(pythagorean_triplet())
