import itertools

def pandigitals_sum():
	total = 0
	perms = (itertools.permutations(range(0,9+1),10))
	for perm in perms:
		perm_list = list(perm)
		int_890 = int("".join(map(str,perm_list[7:10])))
		if int_890%17==0:
			int_789 = int("".join(map(str,perm_list[6:9])))
			if int_789%13==0:
				int_678 = int("".join(map(str,perm_list[5:8])))
				if int_678%11==0:
					int_567 = int("".join(map(str,perm_list[4:7])))	
					if int_567%7==0:
						int_456 = int("".join(map(str,perm_list[3:6])))	
						if int_456%5==0:
							int_345 = int("".join(map(str,perm_list[2:5])))	
							if int_345%3==0:
								int_234 = int("".join(map(str,perm_list[1:4])))	
								if int_234%2==0:
									
									total += int("".join(map(str,perm_list)))	
	return total

if __name__ == "__main__":
	print pandigitals_sum()
