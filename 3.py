import math

def find_highest_prime_fac(num):
	for i in range(2,int(math.ceil(math.sqrt(num)))):
		if num%i == 0:		
			if isprime(i):	
				fac = i	
				num = num/i
	return fac


def isprime(num):
	if num%2 == 0:
		return False
	for i in range(2,num):
		if num%i==0:
			return False	
	return True


print find_highest_prime_fac(600851475143)