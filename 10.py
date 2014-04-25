                                                                     
                                                                     
                                                                     
                                             
import math


def sum_primes_below_n(n):
	run_sum = 0
	for i in range(2,n):
		if isprime(i):
			run_sum = run_sum + i
	return run_sum

def isprime(n):
	if n ==2:
		return True
	if n%2 == 0:
		return False
	for i in range(3,int(math.ceil(math.sqrt(n)))+1):
		if n%i == 0:
			return False
	return True

print sum_primes_below_n(2000000)