
def sum_power_digits(num,power):
	num_str = str(num)
	num_sum = 0

	for i in range(len(num_str)):
		num_sum = num_sum + int(num_str[i])**power 

	return num_sum


def find_max(power):
	nine_list = []
	nine_list.append('9')
	nines = int("".join(nine_list))
	
	while nines < sum_power_digits(nines,power):
		nine_list.append('9')
		nines = int("".join(nine_list))
	return nines

def find_numbers(power):

	max_test = find_max(power)
	
	success_sum = 0
	
	for i in range(2,max_test):
		spd = sum_power_digits(i, power)
		if spd == i:
			success_sum = success_sum + i
		
	return success_sum



if __name__ == "__main__":
	#print sum_power_digits(99999,4)
	print find_numbers(5)
