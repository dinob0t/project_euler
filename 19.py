
def factorial_sum_digits(n):
	prod = 1
	for i in range(1,n+1):
		prod = prod * i
		prod_str = str(prod)
		if int(prod_str[len(prod_str)-1]) == 0:

			prod_str = prod_str[:-1]
		prod = int(prod_str)

	prod_sum = 0
	for i in range(len(prod_str)):
		prod_sum = prod_sum + int(prod_str[i])

	return prod_sum


if __name__ == "__main__":
	print factorial_sum_digits(100)

