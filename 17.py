
def letter_count(num_str):
	return len("".join(num_str))


def num_2_words(num):
	
	numbers={00: "and", 1: "one", 2: "two", 3: "three", \
	4: "four", 5: "five", 6: "six", 7: "seven", \
	8: "eight", 9: "nine", 10:"ten", 11: "eleven",\
	12: "twelve", 13: "thirteen", 14: "fourteen",\
	15: "fifteen", 16: "sixteen", 17: "seventeen", \
	18: "eighteen", 19: "nineteen", 20: "twenty", \
	30: "thirty", 40: "forty", 50: "fifty", \
	60: "sixty", 70: "seventy", 80: "eighty", \
	90: "ninety", 100: "hundred", 1000: "thousand"}

	num_word = []
	num_str = str(num)

	if num==1000:
		num_word.append(numbers[1])
		num_word.append(numbers[num])
		return num_word
	if len(num_str)==3:
		num_word.append(numbers[int(num_str[0])])
		num_word.append(numbers[100])
		if num%100 > 0:
			num_word.append(numbers[00])
			#if second position is not a 'teen' number
			if int(num_str[1]) != 1 and int(num_str[1]) != 0:	
				num_word.append(numbers[int(num_str[1] + '0')])
				if int(num_str[2]) != 0:
					num_word.append(numbers[int(num_str[2])])
			else:
				num_word.append(numbers[int(num_str[1] + num_str[2])])

	elif len(num_str)==2:
		if int(num_str[0]) != 1:
			num_word.append(numbers[int(num_str[0] + '0')])
			if int(num_str[1]) != 0:
				num_word.append(numbers[int(num_str[1])])	
		else:
			num_word.append(numbers[int(num_str[0] + num_str[1])])

	else:
		num_word.append(numbers[int(num_str[0])])



	return num_word







if __name__ == "__main__":
	letter_sum = 0
	for i in range(1,1001):
		#print num_2_words(i)
		letter_sum = letter_sum + letter_count(num_2_words(i))
	print letter_sum