import math
def isprime(n):
	if n<=0:
		return False
	if n==1:
		return True
	if n ==2:
		return True
	if n%2 == 0:
		return False
	for i in range(3,int(math.sqrt(n))+1):
		if n%i == 0:
			return False
	return True

def find_truncable_primes():
	starting_primes = [2,3,5,7]
	for start in starting_primes:
		expand_prime(start)

def expand_prime(start):
	print start
	for right in range(1,10):
		join = int(str(start) + str(right))
		if check_left_right(join):
			print 'passed check, expanding'
			expand_prime(join)	
		else:
			if start not in trun_list and len(str(start)) > 1:
				print 'adding', start
				trl = len(trun_list)
				if trl == 0:
					trun_list.append(start)
				elif start in trun_list:
					pass
				else:
					trun_str = list(str(trun_list[trl-1]))

					if trl> 

					print trun_str, trun_list, start
				 	if trl > len(str(start)) and int("".join(trun_str[:len(trun_str)-2])) == start:
			 			pass
		 			else:
						trun_list.append(start)



def check_left_right(num):
	if len(str(num))==1:
		return True
	if isprime(num):
		num_str = list(str(num))
		print 'made it right'
		if isprime(int("".join(num_str[1:]))):
			print 'made it left'	
			return True	
	return False
			



if __name__ == "__main__":
	trun_list = []
	find_truncable_primes()
	print trun_list
	