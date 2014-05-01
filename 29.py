

def distinct_powers(a_lim,b_lim):
	distinct_dict = {}
	count = 0
	for a in range(2,a_lim+1):
		for b in range(2,b_lim+1):
			current = a**b
			if current not in distinct_dict.keys():
				count = count + 1
				distinct_dict.update({current:count})

	return count
if __name__ == "__main__":
	print distinct_powers(100,100)