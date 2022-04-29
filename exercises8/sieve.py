def primes(limit):
    nums = set(range(2, limit+1))
    notprime = {i for i in range(2, limit+1) for i in range(i*i, limit+1, i)}
    return sorted(nums-notprime)