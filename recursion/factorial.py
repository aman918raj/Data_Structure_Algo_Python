def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def factorial_tail_recursion(n, a=1):
    if n <= 1:
        return a
    return factorial_tail_recursion(n - 1, n * a)

print(factorial(5))
print(factorial_tail_recursion(5))
