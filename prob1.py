def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return [str(i) for i in range(limit + 1) if primes[i]]

def solution(i):
    primes = sieve_of_eratosthenes(100000)  
    prime_string = ''.join(primes) 
    return prime_string[i:i+5]

