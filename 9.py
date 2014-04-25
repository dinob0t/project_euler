                                                                     
                                                                     
                                                                     
                                             

import math
def find_pyth_triplet_sum(num):
	for a in range(1,num):
		for b in range(1,num):
			c_sq = a**2 + b**2
			c = math.sqrt(c_sq)
			if c.is_integer():
				if a+b+int(c) == num:
					return a*b*int(c)
	return 0

print find_pyth_triplet_sum(1000)


