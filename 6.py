def sum_sq_diff(num):
	n_sum = 0
	sq_sum = 0
	for i in range(num+1):
		n_sum = n_sum + i
		sq_sum = sq_sum + i**2
	n_sum = n_sum**2
	diff = n_sum - sq_sum
	return diff

print sum_sq_diff(100)