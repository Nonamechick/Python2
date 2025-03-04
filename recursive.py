def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n - 1)

def Fib(n):
    if n == 0 or n == 1:
        return n
    return Fib(n - 1) + Fib(n - 2)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:-1])

def is_prime(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)
    
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


def find_max(lst, n):
    if n == 1:
        return lst[0]
    return max(lst[n - 1], find_max(lst, n - 1))



if __name__ == '__main__':
    print(find_sum(6))  
    print(Fib(6)) 
    num = 5
    print(f"Factorial of {num}:", factorial(num))

    string = "Abdurahmon"
    print(f"Reversed '{string}':", reverse_string(string))  

    prime_check = 29
    print(f"Is {prime_check} prime?", is_prime(prime_check))    

    nums = 12345
    print(f"Sum of digits of {nums}: {sum_of_digits(nums)}")  

    a, b = 48, 18
    print(f"GCD of {a} and {b}: {gcd(a, b)}")  

    word = "racecar"
    print(f"Is '{word}' a palindrome? {is_palindrome(word)}")  

    lst = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Maximum element in list: {find_max(lst, len(lst))}")  
