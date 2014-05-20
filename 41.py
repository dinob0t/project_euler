import itertools
import math

def pandigitals(n):
	pans = []
	perms = (itertools.permutations(range(1,n+1),n))
	for perm in perms:
		current = int("".join(map(str,list(perm))))
		
		if isprime(current):
			pans.append(current)

	return pans

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

if __name__ == "__main__":
	print pandigitals(7)