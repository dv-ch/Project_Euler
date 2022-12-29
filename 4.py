# Find the largest palindrome made from the product of two 3-digit numbers.


def largest_palindrome_product(upper_n, lower_n, palindromes=[]):
    for x in range(upper_n, lower_n, -1):
        for y in range(upper_n, lower_n, -1):
            if str(x * y) == str(x * y)[::-1]:
                palindromes.append(x * y)
    return palindromes


upper_n = 999
lower_n = 99

palindromes = largest_palindrome_product(upper_n, lower_n)

print(f"{max(palindromes)}")
