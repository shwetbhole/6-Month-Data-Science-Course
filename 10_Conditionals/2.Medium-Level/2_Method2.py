def is_prime(n):
    """
    Optimized prime checker.
    we only need to check divisors up to square root of n
    """

    if n<=1:
        return False
    if n==2:    # 2 is the only even prime
        return True
    if n%2==0:  # Even  numbers > 2 are not prime
        return False

    # check odd divisors only, upto sqrt(n)
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0:
            return False

    return True

# test the optimized version
for num in range(1, 100):
    print(f"{num}: {'Prime' if is_prime(num) else 'Not prime'}")