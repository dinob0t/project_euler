import math
def is_prime(num):
	if num <= 1:
		return False
	elif num == 2:
		return True
	elif num%2 == 0:
		return False
	else:
		for i in range(3,int(math.sqrt(num))+1):
			if num%i == 0:
				return False
		return True

def consec_sum_below(n):
	prime_list = []
	for i in range(1,n):
		if is_prime(i):
			prime_list.append(i)
	for i in range(len(prime_list)-1,0,-1):
		start = prime_list[i]
		cur_sum = 0
		cur_index = i
		found = 0
		while cur_sum < start:
			cur_index -+ 1
			cur_sum += prime_list[cur_index]
			if cur_sum == start:
				found = 1
		length = i - cu


		for j in range(i-1,0,-1):
			cur_sum = 0
			for k in range()



			

if __name__ == "__main__":
	consec_sum_below(1000)

