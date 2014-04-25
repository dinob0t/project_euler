                                                                     
                                                                     
                                                                                                                 
def find_prime_k(k):
	prime_count = 0
	i = 1

	while prime_count < k:
		i = i + 1
		if isprime(i):
			prime_count = prime_count + 1
	return i 
		
def isprime(n):
	if n ==2:
		return True
	if n%2 == 0:
		return False
	for i in range(2,n):
		if n%i == 0:
			return False
	return True


print find_prime_k(10001)