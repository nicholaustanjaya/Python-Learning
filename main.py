def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def print_prime(is_prime_flag,number):
    if is_prime_flag:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

# number = int(input("Put some number = "))
for i in range(2,51):
    result = is_prime(i)
    print_prime(result,i)

