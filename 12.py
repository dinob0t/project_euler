                                                                     
                                                                     
                                                                     
                                             
import math

def tri_num_div_over(div):
	cur_tri_num = 1
	tri_count = 1
	last_added = 1
	div_count = 1
	while div_count <= div:
		last_added = last_added + 1
		cur_tri_num = cur_tri_num + last_added
		tri_count = tri_count + 1
		div_count = number_divisors(cur_tri_num)
	return cur_tri_num

def number_divisors(num):
	divisors = 0
	for i in range(2,int(math.ceil(math.sqrt(num)))):
		if num%i==0:
			divisors = divisors + 1
	return divisors*2 + 2

print tri_num_div_over(500)


