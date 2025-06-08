def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib = [0, 1]
    while len(fib) < n:
        next_number = fib[-1] + fib[-2]
        fib.append(next_number)
    return fib

print(fibonacci(7))