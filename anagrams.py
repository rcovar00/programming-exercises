def anagrams():
	"""
	Identify and print anagrams
	>>> anagrams()
	AMOR - ARMO - MARO - MORA - OMAR - RAMO - ROMA
	JAMON - MONJA - MOJAN
	ESPONJA - JAPONES
	"""
	words = "AMOR","ARMO","ESPONJA","JAMON","JAPONES","MARO","MONJA","MOJAN","MORA","OMAR","RAMO","ROMA"

	anagrams = {}
	for word in words:
		chars = list(word)
		chars.sort()
		key = "".join(chars)
		if key in anagrams:
			anagrams[key].append(word)
		else:
			anagrams[key] = [word]

	for key, anagram in anagrams.iteritems():
		print " - ".join(anagram)
