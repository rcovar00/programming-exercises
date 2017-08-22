def pow(n, exponent):
	"""
	Write a function to calculate the exponentiation of a number without using **
	>>> pow(2,2)
	4
	>>> pow(2,3)
	8
	>>> pow(2,0)
	1
	>>> pow(6,1)
	6
	"""
	result = 0

	if exponent == 0:
		return 1
	elif exponent == 1:
		return n

	while exponent > 1:
		result += n * n
		exponent -= 1

	return result
