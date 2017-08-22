def find_sum(array1, array2, sum):
	"""
	Write a function that returns true if two numbers from two sorted arrays add up to a given sum.
	>>> find_sum([34,45,23],[43,2,7,8],34)
	False
	>>> find_sum([2],[43,2,7,8],10)
	True
	"""
	for a1 in array1:
		for a2 in array2:
			if a1 + a2 == sum:
				return True

	return False