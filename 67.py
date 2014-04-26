def read_file_return_list(name):
	list = []
	with  open(name,'r') as f:
		for line in f:
			line = line.split('\n')
			list.append(line[0])
			if 'str' in line:
				break
	return list

def triangle_to_dict(triangle):
	tri_dict = {}
	row_count = 0
	for i in triangle:
		tri_dict.update({row_count: i.split(' ')})
		row_count = row_count + 1
	return tri_dict

def find_max_path_sum(tri_dict):
	end = max(tri_dict.keys()) + 1
		
	for row in range(end-2, -1, -1):
		for index in range(len(tri_dict[row])):
			(tri_dict[row])[index] = int((tri_dict[row])[index]) + max(int((tri_dict[row+1])[index+1]),int((tri_dict[row+1])[index]))
	return tri_dict[0]


if __name__ == "__main__":
	triangle =  read_file_return_list('67_input.dat')
	tri_dict = triangle_to_dict(triangle)
	print find_max_path_sum(tri_dict)
