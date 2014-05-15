import math
def isprime(n):
	if n<=0:
		return False
	if n==1:
		return False
	if n ==2:
		return True
	if n%2 == 0:
		return False
	for i in range(3,int(math.sqrt(n))+1):
		if n%i == 0:
			return False
	return True

def generate_trun_list(num, direc):
	trunc_list = [2,3,5,7]
	
	for current in trunc_list:
		if max(trunc_list) > num:
			return trunc_list
		for i in range(1,10):
			if direc == 'r':
				join = int(str(current) + str(i))
			else:
				join = int(str(i) + str(current))
			if isprime(join) and join not in trunc_list:
				trunc_list.append(join)


def join_lists(rl, ll):
	both_list = []
	for r in rl:
		if r in ll and len(str(r))>1:
			both_list.append(r)
	return both_list

if __name__ == "__main__":
	right_list =  generate_trun_list(1000000,'r')
	print right_list
	left_list =  generate_trun_list(1000000,'l')
	print left_list
	both = join_lists(right_list, left_list)
	print both
	print sum(both)
	