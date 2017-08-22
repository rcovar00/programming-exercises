def greatest_difference(a):
	"""
	Write a function that takes an array of numbers and returns the 
	greatest difference you can get by subtracting any two of those numbers.
	>>> greatest_difference([5,8,6,1])
	7
	>>> greatest_difference([4,3])
	1
	>>> greatest_difference([234,24,98,0,-23,234])
	257
	"""
	a.sort()
	return a[-1] - a[0]