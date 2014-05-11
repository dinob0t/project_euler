
def factorial(n):
	prod = 1
	if n == 0:
		return 1
	if n == 1:
		return 1
	if n == 2:
		return 2
	for i in range(2,n+1):
		prod = prod*i	
	return prod

def digit_fac_test(num):
	num_str = str(num)
	num_sum = 0
	#print num
	for digit in reversed(num_str):
		num_sum = num_sum + factorial(int(digit))
		if num_sum> num:
			return False
	if num_sum == num:
		print num
		return True
		



if __name__ == "__main__":
	sums = 0
	for i in range(3,999999):
		if digit_fac_test(i):
			sums = sums + i		
	print sums