
def find_largest_collatz_chain(num):
	if num == 1:
		return 1
	chains={1:1}
	largest_chain = 1
	largest_chain_start = 1
	for i in range(2,num+1):
		new_chain = []
		cur_num = i
		known_length = 0
		while True:	
			if cur_num not in chains:
				new_chain.insert(0,cur_num)
				chains.update({cur_num:0})
			else:
				known_length = chains[cur_num]
				break
			cur_num = collatz_move(cur_num)
		for j in new_chain:
			known_length = known_length + 1	
			chains.update({j: known_length})


		if known_length > largest_chain:
			largest_chain = known_length
			largest_chain_start = i

	return largest_chain_start


def collatz_move(num):
	if num%2==0:
		return num/2
	else:
		return 3*num+1


if __name__ == "__main__":
	print find_largest_collatz_chain(999999)

