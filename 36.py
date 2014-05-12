def generate_palindrome_binary(num):
	pal_sum = 0
	for i in range(num):
		if ispal(str(i)): 
			if ispal(trim_bin(i)):
				pal_sum = pal_sum + i
				print i
	return pal_sum

def ispal(num_str):
	mid = len(num_str)//2 -1
	count = 1 + len(num_str)%2
	#print count, mid, num_str, len(num_str)
	for i in range(mid,-1,-1):
		#print i, count
		if num_str[i] != num_str[mid+count]:
			return False
		count += 1
	return True

def trim_bin(num):
	bl = bitLen(num)
	num = bin(num)
	return num[len(num)-bl:]


def bitLen(int_type):
	length = 0
	while (int_type):
		int_type >>= 1
		length += 1
 	return(length)

if __name__ == "__main__":
	print generate_palindrome_binary(1000000)


	