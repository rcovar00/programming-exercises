# -*- coding:utf-8 -*-

def fizzbuzz(n):
	"""
	"Write a program that prints the numbers from 1 to n. 
	But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
	For numbers which are multiples of both three and five print “FizzBuzz”."
	>>> fizzbuzz(4)
	1
	2
	Fizz
	4
	>>> fizzbuzz(15)
	1
	2
	Fizz
	4
	Buzz
	Fizz
	7
	8
	Fizz
	Buzz
	11
	Fizz
	13
	14
	FizzBuzz
	"""
	for n in range(1, n+1):

		mod3 = n % 3 == 0
		mod5 = n % 5 == 0

		if mod3 == True and mod5 == True:
			print 'FizzBuzz'
		elif mod3:
			print 'Fizz'
		elif mod5:
			print 'Buzz'
		else:
			print n
