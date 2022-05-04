# Fibonacci

# 1
# timp: O(2^n) - pentru ca am calculat de mai multe ori acelasi numar
# spatiu: O(1) - spatiu constant // spatiu O(n) din cauza stivei

def fibonacci(n):
    if n < 0:
        return "Numar invalid!"

    if n == 1 or n == 0:
        return n
    return (fibonacci(n-1) + fibonacci(n-2))

print(fibonacci(2))

# 2
# timp: O(n) -calculeaza o singura data fiecare element
# spatiu: O(n)

def fibonacci_cu_memorare(n, l_fibo):
    if n < 0:
        return "Numar invalid!"

    if n == 1 or n == 0:
        l_fibo.insert(n,n)
        return n

    if len(l_fibo) >= n+1:
        return l_fibo[n]
    else:
        f = fibonacci_cu_memorare(n-1,l_fibo) + fibonacci_cu_memorare(n-2,l_fibo)
        l_fibo.insert(n, f)
        return f

print(fibonacci_cu_memorare(20,[]))


# 3
# timp: O(n)
# spatiu: O(1) - spatiu constant

def fibonacci_iterativ(n):
    if n < 0:
        return "Numar invalid!"
    if n == 1 or n == 0:
        return n

    fibo1 = 1
    fibo2 = 0
    fibo = 0

    while n > 1:
        fibo = fibo1 + fibo2

        #incluim ulimele 2 numere din sir
        fibo2 = fibo1
        fibo1 = fibo
        n -=1
    return fibo

print(fibonacci_iterativ(20))