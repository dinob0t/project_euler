def find_smallest_num_for_div(max_div):	
	for i in range (max_div, 1000000000,max_div):
		num = i
		found = 1
		for j in range(max_div,1,-1):	
			if num%j != 0:		
				found = 0
				break
		if found == 1:
			return i

print find_smallest_num_for_div(20)