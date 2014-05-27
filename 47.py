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

def find_prime_fac(num, prime_list):
	for i in range(1,int(math.ceil(math.sqrt(num)))):
		if num%i == 0:		
			if isprime(i):
				if i not in prime_list:	
					prime_list.append(i)
				num = num/i
				if isprime(num):
					if num not in prime_list:
						prime_list.append(num)
				else:
					find_prime_fac(num, prime_list)
				return prime_list
	

def find_consec_distinct(n_max, chain):
	found = 0
	for i in range(4,n_max):
		tmp = find_prime_fac(i,[])
		if tmp and len(tmp) == chain:
			found = 1
			for j in range(1,chain):
				tmp = find_prime_fac(i+j,[])
				if not tmp or not len(tmp) == chain:
					found = 0
					break
		if found == 1:
			return i

		
	return 0




if __name__ == "__main__":
	print find_consec_distinct(1000000,4)

