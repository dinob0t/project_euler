
fib1 = 1
fib2 = 2
fib_sum = fib1+fib2
even_sum = fib2
while fib2 < 4000000:
	tmp = fib1 + fib2
	fib1 = fib2
	fib2 = tmp
	if fib2%2 == 0:
		even_sum = even_sum + fib2
print even_sum