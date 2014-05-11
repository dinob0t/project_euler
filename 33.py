import string
import fractions

def digit_cancelling(num_den_digits):
	num_prod = 1
	den_prod = 1
	max_num = int('9'*num_den_digits)
	for den in range(1,max_num+1):
		den_str = str(den)
		for num in range(1, den+1):
			num_str = str(num)
			for digit in num_str:
				#print num, den
				if den_str.find(digit) != -1:
					ns = list(num_str)
					ds = list(den_str)
					
					ns.pop(num_str.find(digit))
					ds.pop(den_str.find(digit))

					
					ns = "".join(ns)
					ds = "".join(ds)

					if ns and ds and int(ds) !=0 and num%10!=0 and ns !=ds:
						if abs(float(ns)/float(ds) - 1.0*num/den) < 0.0000001:
							print ns, ds, num, den
							num_prod = int(ns)*num_prod
							den_prod = den_prod*int(ds)
	return num_prod, den_prod



if __name__ == "__main__":
	print digit_cancelling(2)
