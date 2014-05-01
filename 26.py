

def get_length_recur_frac(denom):

	if denom==1:
		return 0
	trial_dict = {}
	trial = 10
	whole = trial//denom
	remain = trial - whole*denom
	trial_dict.update({trial:1})
	end_trial = 0

	while remain !=0 and end_trial ==0:
		trial = remain*10

		if trial in trial_dict.keys():
			return len(trial_dict) - trial_dict[trial] + 1
		else:
			trial_dict.update({trial:len(trial_dict)+1})

		whole = trial//denom
		remain = trial - whole*denom

	if remain ==0:
		return 0

def find_max_cycle_to(d):
	best_len = 0
	best_num = 0
	for i in range(1,d+1):
		current_len = get_length_recur_frac(i)
		if current_len > best_len:
			best_len = current_len
			best_num = i		

	return best_num


if __name__ == "__main__":
	print find_max_cycle_to(1000)
