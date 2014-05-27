
def power(n,p,trim):
	total = n
	for i in range(1,p):
		total *=n
		total_str = list(str(total))
		if len(total_str) > trim:
			total = int("".join(total_str[len(total_str)-trim:len(total_str)]))

	return total


if __name__ == "__main__":
	total = 0
	for i in range(1,1001):
		total = total + power(i,i,10)
	print total

