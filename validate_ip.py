def validate_ip(ip):
	"""
	Validate ip address v4 and v6
	>>> validate_ip('192.156.78.290')
	False
	>>> validate_ip('192.156.78.20')
	True
	>>> validate_ip('192.156.78.20.34.39')
	True
	>>> validate_ip('192.156.34')
	False
	>>> validate_ip('....')
	False
	"""
	valid = True
	try:
		address = ip.split('.')
		address = map(int, address)
	except ValueError as e:
		valid = False
	else:
		if len(address) not in [4, 6]:
			valid = False

		if valid:
			for num in address:
				if num < 0 or num > 255:
					valid = False
					break

	return valid