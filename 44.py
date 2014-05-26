import math

def generate_pent(n):
	p = n*(3*n-1)/2 	
	return p

def is_pent(p):
	sol1 = (0.5 + math.sqrt(0.25 +6*p))/3.0
	sol2 = (0.5 - math.sqrt(0.25 +6*p))/3.0
	
	if sol1%1 == 0:
		
		#print abs(sol1)-1
		if generate_pent(abs(sol1)) == p:
			return True

	if sol2%1 == 0:
		
		#print abs(sol2)-1
		if generate_pent(abs(sol2)) == p:
			return True
	return False
	


def find_pent_pair(max_num):
	best_diff = generate_pent(max_num)
	best_pj = 1
	best_pk = best_diff
	for k in range(1,max_num+1):
		pk = generate_pent(k)
		for j in range(k,0,-1):		
			pj = generate_pent(j)
			curr_diff = abs(pk - pj)
			if curr_diff > best_diff:
				break
			if is_pent(pj + pk) and pk>pj and is_pent(pk-pj):
				if curr_diff < best_diff:
					print pj, pk, curr_diff, j, k
					best_diff = curr_diff	
		
	return best_diff
	
if __name__ == "__main__":

	print find_pent_pair(60000)
