import math

def find_abundants(num):
	abundants = []
	for test_num in range(1,num+1):
		divisors = []

		for i in range(1,int((math.sqrt(test_num)))+1):
			if test_num%i == 0:
				divisors.append(i)
				if i != 1 and i != test_num//i:
					divisors.append(test_num//i)
		#print divisors, test_num
		if (sum(divisors)> test_num):
			abundants.append(test_num)

	return abundants

def remove_2_abundant_sums_from_list(abundant_list,number_list):
	max_list = max(number_list)
	updated_number_list = number_list
	for abund1 in abundant_list:
		for abund2 in abundant_list:
			if abund1 + abund2 <= max_list:
				updated_number_list[abund1 + abund2] = 0
			else:
				break


	return updated_number_list

if __name__ == "__main__":
	limit = 28000
	abundant_list = find_abundants(limit)
	#print abundant_list
	number_list = range(0,limit+1)
	non_abundant_sum_list = remove_2_abundant_sums_from_list(abundant_list,number_list)
	print sum(non_abundant_sum_list)