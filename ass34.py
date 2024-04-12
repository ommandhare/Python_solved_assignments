"""
Get a number from user and check if number is twin prime number

"""

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_twin_prime(num):
    if is_prime(num):
        return (is_prime(num - 2) or is_prime(num + 2))
    return False

user_input = int(input("Enter a number: "))

if is_twin_prime(user_input):
    print(f"{user_input} is a twin prime number.")
else:
    print(f"{user_input} is not a twin prime number.")
