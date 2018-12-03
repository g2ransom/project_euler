'''
Solutions to Project Euler problems. You can call each function via command line by using

'python -c 'import functions; print functions.function_name(3, 5, 1000)'' 
'''

def p001(x1, x2, max_val):
	'''
	Original Problem: find the sum of all the multiples of 3 or 5 below 1000.

	Enhanced solution: take any two numbers and find the sum of all multiples

	of those two numbers below a maximum value.

	(To Do) - Create loops that do not waste iterations'''

	total = 0
	larger_number = x1 if x1 > x2 else x2
	smaller_number = x1 if x1 < x2 else x2

	max_iter1 = (max_val / larger_number) if (max_val % larger_number) == 0 else (max_val / larger_number) + 1
	max_iter2 = (max_val / smaller_number) if (max_val % smaller_number) == 0 else (max_val / smaller_number) + 1
	
	for n in range(1, max_iter1):
		mult1 = larger_number * n
		total = total + mult1

	for m in range(1, max_iter2):
		if m % larger_number != 0:
			mult2 = smaller_number * m
		else:
			mult2 = 0
		total = total + mult2
	return total


def fibonacci(max_val):
	fibs = [1, 2]
	while fibs[-1] < max_val:
		x = fibs[-1] + fibs[-2]
		if x < max_val:
			fibs.append(x)
		else:
			return fibs


def p002(max_val):
	'''
	By considering the terms in the Fibonacci sequence whose values do not exceed four million, 

	find the sum of the even-valued terms.'''
	fibs = fibonacci(max_val)
	even_sum = sum(list(filter(lambda x: x % 2 == 0, fibs)))
	return even_sum


