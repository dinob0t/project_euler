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


if __name__ =="__main__":
	print generate_primes(100)
	print generate_twice_squares(100)
