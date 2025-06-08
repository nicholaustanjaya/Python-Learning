def factorial(n):
    if n==0:
        return(1)
    else:
        value=1
        for i in range(1,n+1):
            value *= i
    return(value)

print(factorial(5))
print(factorial(0))
print(factorial(7))
