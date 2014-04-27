import math

def d(n):
	divisors = []
	divisors.append(1)
	if n ==1:
		return sum(divisors)
	for i in range(2,int(math.ceil(math.sqrt(n)))):
		if n%i == 0:
			divisors.append(i)
			divisors.append(n/i)
	return sum(divisors)

def amicable_dict(num):
	am_dict = {}
	for i in range(1,num):
		am_dict.update({i: d(i)})

	return am_dict

def sum_amicable_pairs(am_dict):
	am_sum = 0
	for i in am_dict.keys():
		if i in am_dict.keys() and am_dict[i] in am_dict.keys():
			if i == am_dict[am_dict[i]] and i != am_dict[i]:
				print i, am_dict[i], am_dict[am_dict[i]]
				am_sum = am_sum + am_dict[i]
	return am_sum

if __name__ == "__main__":
	print sum_amicable_pairs(amicable_dict(10001))
	