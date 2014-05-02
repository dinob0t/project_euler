
def ways_to_split_amount(in_list):
	#pounds amount in cents

	combinations =1
	split_list = in_list[:]

	while True:
		next_term = 0
		for i in range(len(split_list)-1, -1, -1):
			if split_list[i] != 1:
				next_term = i
				break
		if split_list[i] == 1:
			break

		if split_list[next_term] == 200:
			split_list.pop(next_term)
			split_list.append(100)
			split_list.append(100)
		elif split_list[next_term] == 100:
			split_list.pop(next_term)
			split_list.append(50)
			split_list.append(50)
		elif split_list[next_term] == 50:
			split_list.pop(next_term)
			split_list.append(20)
			split_list.append(10)
			split_list.append(10)
			split_list.append(10)
			combinations = combinations + ways_to_split_amount(split_list)
			split_list.pop(len(split_list)-1)
			split_list.pop(len(split_list)-1)
			split_list.pop(len(split_list)-1)
			split_list.append(20)
			split_list.append(10)
		elif split_list[next_term] == 20:
			split_list.pop(next_term)
			split_list.append(10)
			split_list.append(10)
		elif split_list[next_term] == 10:
			split_list.pop(next_term)
			split_list.append(5)
			split_list.append(5)
		elif split_list[next_term] == 5:
			split_list.pop(next_term)
			split_list.append(2)
			split_list.append(1)
			split_list.append(1)
			split_list.append(1)
			combinations = combinations + ways_to_split_amount(split_list)
			split_list.pop(len(split_list)-1)
			split_list.pop(len(split_list)-1)
			split_list.pop(len(split_list)-1)
			split_list.append(2)
			split_list.append(1)

		elif split_list[next_term] == 2:
			split_list.pop(next_term)
			split_list.append(1)
			split_list.append(1)
			
		combinations = combinations +1
		# if sum(split_list) != 200:
		# 	print split_list, combinations, sum(split_list)
		#print split_list, combinations, next_term, len(split_list), split_list[next_term]



	return combinations

if __name__ == "__main__":
	start = []
	start.append(10)
	print ways_to_split_amount(start)