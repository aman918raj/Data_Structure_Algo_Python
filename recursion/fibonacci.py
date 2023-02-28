def fibonacci_tail_recursion(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return fibonacci_tail_recursion(n - 1, b, a + b)


print(fibonacci_tail_recursion(1))
