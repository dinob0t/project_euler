def read_file_return_list(name):
	name_list = []
	with  open(name,'r') as f:
		for line in f:
			name_list = ("".join(line.split('"')).split(','))
			#list.append(line[0])
			if 'str' in line:
				break
	name_list.sort()
	return name_list

def name_to_num(list_in):
	num_list = []
	for name in list_in:
		cur_sum = 0
		for i in range(len(name)):
			cur_char = ord(name[i])
			cur_sum = cur_sum + cur_char - 64
		num_list.append(cur_sum)
	return num_list


def get_total(num_list):
	prod_list = []
	for i in range(len(num_list)):
		prod_list.append(num_list[i]*(i+1))
	return sum(prod_list)


if __name__ == "__main__":
	 name_list = read_file_return_list('22_input.dat')
	 print name_list
	 num_list = name_to_num(name_list)
	 #print num_list

	 print get_total(num_list)
