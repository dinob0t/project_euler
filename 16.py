import math

def x_n_squaring(x,n):
	if n<0:
		return x_n_squaring(1.0/x, -n)
	elif n==0:
		return 1
	elif n==1:
		return x
	elif n%2==0:
		return x_n_squaring(x*x,n/2)
	elif n%2==1:
		return x*x_n_squaring(x*x,(n-1)/2)


def add_digits(num):
	num_str = str(num)
	run_sum = 0
	for i in range(len(num_str)):
		run_sum = run_sum + int(num_str[i])
	return run_sum


if __name__ == "__main__":
	num = x_n_squaring(2,1000)
	print add_digits(num)
