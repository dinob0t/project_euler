import math
import itertools
def isprime(n):
	if n<=0:
		return False
	if n==1:
		return False
	if n ==2:
		return True
	if n%2 == 0:
		return False
	for i in range(3,int(math.sqrt(n))+1):
		if n%i == 0:
			return False
	return True

# def pandigitals(n):
# 	pans = []
# 	perms = (itertools.permutations(range(1,n+1),n))
# 	for perm in perms:
# 		current = int("".join(map(str,list(perm))))
		
# 		if isprime(current):
# 			pans.append(current)

# 	return pans

def four_digit_primes():
	prime_list = []
	for i in range(1000,10000):
		if isprime(i):
			prime_list.append(i)
	return prime_list

def eliminate_non_perms(prime_list):
	new_list = []
	for prime in prime_list:
		perms = (itertools.permutations(list(str(prime)),4))
		perm_list = []
		for perm in perms:
			p = int("".join(perm))
			if p in prime_list:
				perm_list.append(p)
				prime_list.remove(p)
		if len(perm_list)>3:
			new_list.append(perm_list)
	return new_list

def check_arithmetic(pp_list):
	for p_list in pp_list:
		p_list = sorted(p_list)
		for i in range(1,4500):
			count = 1
			for j in range(0,len(p_list)-1):
				if p_list[j] + i in p_list and p_list[j] + 2*i in p_list:
					print p_list[j], p_list[j] + i, p_list[j] + 2*i

			









if __name__ == "__main__":
	prime_list =  four_digit_primes()
	perm_prime_list = eliminate_non_perms(prime_list)
	check_arithmetic(perm_prime_list)




