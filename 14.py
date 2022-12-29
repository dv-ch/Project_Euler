# Which starting number, under one million,
# produces the longest chain of the Collatz sequence?


def longest_collatz_sequence(n):

    chains = {1: 1}

    for i in range(1, n):
        num = i
        arr = []

        while True:
            if num in chains:
                for x in arr:
                    chains[x] = len(arr) - arr.index(x) + chains[num]
                break
            elif num % 2 == 0:
                arr.append(num)
                num /= 2
                continue
            elif num != 1:
                arr.append(num)
                num = (num * 3) + 1
                arr.append(num)
                num /= 2
                continue

            break

    longest_chain = max(chains.values())
    highest_num = [k for k, v in chains.items() if v == longest_chain]
    return highest_num


print(longest_collatz_sequence(1000000))
