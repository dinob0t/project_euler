

def lexicographic_order_to_num(digits, count_num):
	current = range(0,digits+1)
	count = 1
	if count_num == 1:
		return current
	while count <=count_num:

		for i in range(0,digits):
			if current[i] < current[i+1]:
				k = i
		for i in range(0,digits+1):
			if current[k]< current[i]:
				l = i		
		tmp = current[l]
		current[l] = current[k]
		current[k] = tmp

		current[k+1:digits] in reversed(current[k+1:digits+1])



		print current
		count = count + 1
	return current
 


if __name__ == "__main__":
	lexicographic_order_to_num(2, 3)