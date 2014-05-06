import math

def pandigitals(n):
	pan_dict = {}
	digit_list = range(1,n+1)
	n_str = str(n)
	max_n = int('9'*len(n_str))
	max_half = len(n_str)//2

	for i in range(1,max_n+1):
		for j in range(1,max_n+1):
			#go backwards from number and find divisors


if __name__ == "__main__":
	print pandigitals(2)