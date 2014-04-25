

def read_file_return_list(name):
	list = []
	with  open(name,'r') as f:
		for line in f:
			line = line.split('\n')
			list.append(line[0])
			if 'str' in line:
				break
	return list

def str_sum(str1, str2):
	sum_str = []
	max_len = max(len(str1),len(str2))

	str1 = list(str1)
	str2 = list(str2)
	
 	
 	while len(str1)< max_len:
 		str1.insert(0,'0')

 	while len(str2)< max_len:
 		str2.insert(0,'0')
 		

	rem_str = 0
	for i in range(max_len-1,-1,-1):


		total = int(str1[i]) + int(str2[i]) + int(rem_str)
		total_str = str(total)

		if len(total_str) > 1:
			rem_str = total_str[0]
			sum_str.insert(0,total_str[1])
		else:
			rem_str = 0
			sum_str.insert(0,total_str[0])	

	if rem_str >0:
		sum_str.insert(0,rem_str[0])	

	return ''.join(sum_str)
	

if __name__ == "__main__":
	num_list = read_file_return_list('13_input.dat')

	run_sum = num_list[0]
	for i in range(1,len(num_list)):
		run_sum = str_sum(run_sum, num_list[i])

	print run_sum, len(run_sum)
	print run_sum[0:10]