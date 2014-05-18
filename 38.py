

def return_largest_pandigital_multiple(n1,n2):
	current_largest = 0
	for i in range(n1,n2+1):
		#print i

		for p in range(2,50):
			pan = 1
			prod_list = []
			for j in range(1,p):
				prod = i*j
				prod_str = list(str(prod))
				cont = 1
				#print prod_str, i, j
				for digit in prod_str:
				 	#print digit
					if digit in prod_list or int(digit)==0:
						#print digit
						cont = 0
				 		break
				 	else:
				 		prod_list.append(digit)
				if cont !=1:
					#print prod_list
					pan = 0
				 	break
			if len(prod_list) == 9 and pan ==1:
				print i, prod_list, j
				current_largest = prod_list
	return current_largest


if __name__ == "__main__":
	print "".join(return_largest_pandigital_multiple(1,10001))