
def prod_get_digit(num_list):
	digit = 1
	digit_str = str(digit)
	digit_count = 0
	last = num_list[-1]
	cur_digit_index = 0

	
	looking_index = 0
	prod_digits = 1
	while looking_index <= len(num_list)-1:
		digit_count += 1
		looking = num_list[looking_index]
		if cur_digit_index >= len(digit_str):
			digit += 1
			digit_str = str(digit)
			cur_digit_index = 0
		
		cur_char = digit_str[cur_digit_index]
		cur_digit_index +=1
		#print cur_char, cur_digit_index, digit, digit_str, digit_count
		if digit_count == looking:
			print cur_char, looking
			prod_digits = prod_digits* int(cur_char)
			looking_index += 1
			
			
	return prod_digits



if __name__ == "__main__":
	print prod_get_digit([1,10,100,1000,10000, 100000, 1000000])