import itertools


def pandigitals(n):
	pan_digit_prods = []
	perms = (itertools.permutations(range(1,n+1),n))
	for perm in perms:
		for n1 in range(n-1):
			for n2 in range(n1+1,n-1):
				perm_list = map(str,list(perm))
				num1 = int(''.join(perm_list[0:n1+1]))
				num2 = int(''.join(perm_list[n1+1:n2+1]))
				eq = int(''.join(perm_list[n2+1:n+1]))
				
				if num1*num2 == eq:
					if eq not in pan_digit_prods:
						pan_digit_prods.append(eq)
					

	return sum(pan_digit_prods)



if __name__ == "__main__":
	print pandigitals(9)