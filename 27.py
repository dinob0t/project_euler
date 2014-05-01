import math

def poly_primes(a,b,n):
	return n*n + a*n + b

def consecutive_primes(a_lim, b_lim):
	best_chain = 0
	best_a = -a_lim
	best_b = -b_lim
	cur_chain = 0
	for a in range(-a_lim, a_lim+1):

		for b in range(-b_lim, b_lim+1):
			cur_chain = 0

			n = 0
			while isprime(poly_primes(a,b,n)):

				cur_chain = cur_chain + 1
				n = n + 1
			if cur_chain > best_chain:
				best_chain = cur_chain
				best_a = a
				best_b = b
				print best_chain, best_a, best_b, 'new best'

	return best_a*best_b

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

if __name__ == "__main__":
	print consecutive_primes(999,999)
