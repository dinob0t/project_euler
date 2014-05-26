import math
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


def generate_primes(n_max):
	prime_list = []
	cur = 2
	while cur<n_max:
		if isprime(cur):
			prime_list.append(cur)
		cur = cur + 1
	return prime_list

def generate_twice_squares(n_max):
	twice_list = []
	cur = 1
	num = 1
	while cur<n_max:
		twice_list.append(2*cur)
		num +=1
		cur = num**2
	return twice_list

def generate_odd_composite(n_max):
	comp_list = []
	cur = 9
	while cur<n_max:
		if not isprime(cur):
			comp_list.append(cur)
		cur += 2
	return comp_list

def test_goldbach(p_l, t_l, c_l):
	for prime in p_l:
		for twice in t_l:
			cur = prime + twice
			if cur in c_l:
				c_l.remove(cur)
	return c_l




if __name__ =="__main__":
	num = 10000
	prime_list = generate_primes(num)
	twice_list = generate_twice_squares(num)
	comp_list =  generate_odd_composite(num)
	print test_goldbach(prime_list, twice_list, comp_list)
