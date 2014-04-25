def find_pal_prod(low,high):
	best = 0
	for i in range(high,low,-1):
		if i < best/999:
			break
		for j in range(high,low,-1):
			prod = i*j
			if prod < best:
				break
			prod_str = str(prod)
			pal = True
			for k in range(len(prod_str)//2):
				if prod_str[k] != prod_str[len(prod_str)-1-k]:
					pal = False
					break
			if pal == True and prod > best:
				best = prod
	return best

print find_pal_prod(99, 999)