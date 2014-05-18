import math

def return_triangle_solutions(num):
	solns = 0
	for a in range(1,num):
		for b in range(a,num):
			c = math.sqrt(a**2 + b**2)
			if is_whole(num) and a + b + c == num:
				solns += 1
	return solns



def is_whole(x):
	if x%1==0:
		return True
	return False

def find_most_solns(max_num):
	current_max = 0
	current_biggest = 0
	for i in range(1,max_num):
		cur_solns = return_triangle_solutions(i)
		if cur_solns > current_biggest:
			current_biggest = cur_solns
			current_max = i
	return current_max

if __name__ == "__main__":
	print find_most_solns(1000)
