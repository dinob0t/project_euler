
def get_first_fib_number_length_n(n):

	F_n2 = 1
	if n==1:
		return F_n2
	F_n1 = 1
	F_n = F_n1+F_n2
	count = 3

	while len(str(F_n))<n:
		F_n2 = F_n1
		F_n1 = F_n
		F_n = F_n1+F_n2	
		count = count + 1
		#print F_n, count
		

	return count





if __name__ == "__main__":
	print get_first_fib_number_length_n(1000)
