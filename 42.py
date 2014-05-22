def read_file_return_list(name):
	
	with  open(name,'r') as f:
		for line in f:

			line = line.split(',')
			if 'str' in line:
				break
		word_list = []
		for word in line:
			word_list.append(word.replace('"', ''))

	return word_list

def generate_triangles(limit):
	triangle_list = []
	n = 1
	cur_tri = 1
	triangle_list.append(cur_tri)
	while cur_tri< limit:
		n = n + 1
		cur_tri = int(0.5*n*(n+1))
		triangle_list.append(cur_tri)
	return triangle_list

def find_triangle_words(words, triangles):
	num = 0
	for word in words:
		cur_word_sum = sum([x -64 for x in map(ord,word.upper())])
		if cur_word_sum in triangles:
			num = num + 1
	return num


if __name__ == "__main__":
	words = read_file_return_list('42_input.dat')
	max_word_length = max([len(x) for x in words])
	triangles = generate_triangles(max_word_length*26)
	print find_triangle_words(words, triangles)
	