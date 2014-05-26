import math
import time
def is_pent(p):
	sol1 = (0.5 + math.sqrt(0.25 +6*p))/3.0
	#sol2 = (0.5 - math.sqrt(0.25 +6*p))/3.0
	if sol1%1 == 0:
		if generate_pent(abs(sol1)) == p:
			return True
	#if sol2%1 == 0:
		#if generate_pent(abs(sol2)) == p:
			#return True
	return False

def generate_pent(n):
	p = n*(3*n-1)/2 	
	return p

def generate_tri(n):
	p = n*(n+1)/2 	
	return p

def generate_hex(n):
	p = n*(2*n-1) 	
	return p

def is_tri(p):
	sol1 = (-0.5 + math.sqrt(0.25 +2*p))
	#sol2 = (-0.5 - math.sqrt(0.25 +2*p))
	if sol1%1 == 0:
		if generate_tri(abs(sol1)) == p:
			return True
	#if sol2%1 == 0:
		#if generate_tri(abs(sol2)) == p:
			#return True
	return False

def is_hex(p):
	sol1 = (1.0 + math.sqrt(1.0 +8*p))/4.0
	#sol2 = (1.0 - math.sqrt(1.0 +8*p))/4.0
	if sol1%1 == 0:
		if generate_hex(abs(sol1)) == p:
			return True
	#if sol2%1 == 0:
		#if generate_hex(abs(sol2)) == p:
			#return True
	return False

def run():
	for i in range(144, 100000):
		pent = generate_hex(i)
		if is_pent(pent):

			print i, pent
			break


if __name__ == "__main__":
	t0 = time.time()
	run()
	t1 = time.time()
	print t1-t0


