
def sum_diagonal_sprial(num):

	if num==1:
		return 1
	if num ==2:
		return 4
	last_num = 1
	sum_num = 1
	for i in range(3,num+1,2):
		for j in range(4):
			last_num = last_num + i - 1
			
			sum_num = sum_num + last_num

	
	return sum_num



if __name__ == "__main__":
	print sum_diagonal_sprial(1001)
