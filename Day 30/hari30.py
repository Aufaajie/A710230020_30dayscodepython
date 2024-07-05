def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

def reverse_string(string):
    return string[::-1]

if __name__ == "__main__":
    num = 5
    print(f"Factorial of {num} is {factorial(num)}")

    num = 17
    if is_prime(num):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

    text = "Hello, World!"
    print(f"Number of vowels in '{text}' is {count_vowels(text)}")

    text = "Python is awesome"
    print(f"Reversed string of '{text}' is '{reverse_string(text)}'")
