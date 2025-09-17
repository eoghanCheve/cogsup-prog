"""
Write a script that lists all the prime numbers between 1 and 10000.
(A prime number is an integer greater or equal to 2 which has no divisors except 1 and itself). 
Hint: Write an is_factor helper function.
"""

list_of_primes = []

def is_factor(d, n):
    """True iff (if and only if) d is a divisor of n."""
    return(n % d == 0)

def is_prime(n):
    prime = True
    for a in list_of_primes: #optimizable if we take the primes lower than sqrt(n)
        prime = prime and not(is_factor(a,n))
    return prime

for i in range(2,10000):
    if is_prime(i):
        list_of_primes.append(i)

print(list_of_primes)