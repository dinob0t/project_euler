import math
import itertools

def isprime(n):
	if n<=0:
		return False
	if n==1:
		return True
	if n ==2:
		return True
	if n%2 == 0:
		return False
	for i in range(3,int(math.sqrt(n))+1):
		if n%i == 0:
			return False
	return True

def rotate(l,n):
    return l[n:] + l[:n]

if __name__ == "__main__":
	primes = []
	circ_list = []
	total_circ_primes = 0
	for i in range(2,1000001):
		if isprime(i):
			primes.append(i)
	for prime in primes:
		prime_str = str(prime)
		n = len(prime_str)
		prime_str = list(prime_str)
		iscirc = 1
		small_list = []

		if prime not in circ_list:

			for i in range(n):
				perm = rotate(prime_str,i)
				#print int("".join(perm))
				if int("".join(perm)) not in primes:
					iscirc = 0
					break
				if int("".join(perm)) not in small_list:
					small_list.append(int("".join(perm)))
					
			if iscirc == 1:
				circ_list = circ_list + small_list
			
	print len(circ_list), circ_list