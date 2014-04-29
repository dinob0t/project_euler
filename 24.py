

def lexicographic_order_to_num(digits, count_num):
	current = range(0,digits+1)
	print current
	count = 1
	if count_num == 1:
		return current
	while count <count_num:

		for i in range(0,digits):
			if current[i] < current[i+1]:
				k = i
		for i in range(0,digits+1):
			if current[k]< current[i]:
				l = i		
		tmp = current[l]
		current[l] = current[k]
		current[k] = tmp
		#print current, 'before', k+1, digits

		for i in range(k+1, digits):
			new_end = current.pop(k+1)
			#print new_end, digits-1-(i-k-1)
			current.insert(digits - (i-k-1) ,new_end)




		#print current
		count = count + 1
	return current
 


if __name__ == "__main__":
	print lexicographic_order_to_num(9,1000000)