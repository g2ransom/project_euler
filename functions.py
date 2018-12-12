
import math
import numpy as np
import itertools
from functools import reduce
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


def gcd(a, b):
	'''Finds the greatest common denominator using the Euclidean Algorithm'''
	if b == 0:
		return a;
	elif a >= b:
		return gcd(b, a % b)
	else:
		return gcd(b, a)


def primes(m, n):
	'''Sieve of Eratosthenes - Takes Too Much Memory'''
	nums = {x: True for x in range(m, n+1)}
	for i in range(m, int(round(math.sqrt(n)))):
		if nums[i] == True:
			for j in range(i**2 + i, n+1, i):
				nums[j] = False
	return [key for key,val in nums.iteritems() if val == True]


def largest_prime_sieve(n):
	'''Largest prime using Sieve of Eratosthenes'''
	prime_list = primes(n)
	return max(prime_list)


def smallest_prime(n):
	assert n >= 2
	for i in range(2, int(round((math.sqrt(n))))+1):
		if n % i == 0:
			return i
	return n


def largest_prime(n):
	'''What is the largest prime factor of the number 600851475143?

	Generalized the solution for any number'''
	while True:
		p = smallest_prime(n)
		if p < n:
			n //= p
		else:
			return n



def p003(n): return largest_prime(n)


def check_palindrome(n):
	if str(n) == str(n)[::-1]:
		return True
	else:
		return False


def p004(max_val):
	'''Find the largest palindrome made from the product of two 3-digit numbers.'''
	largest_pal = 0
	for i in range(1, max_val):
		for j in range(1, max_val):
			product = i * j
			if (check_palindrome(product) == True) and (product > largest_pal):
				largest_pal = product
	return largest_pal 


# def p005(B):
	'''Error when i = 1 and log 1 = 0'''
	# primes_list = primes(B)
	# print list(enumerate(primes_list,1))
	# return np.prod([prime ** int(round(math.log(B, i))) for i, prime in enumerate(primes_list, 1)])


def p005(B):
	'''What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''
	ans = 1
	for i in range(1, B+1):
		ans *= i // gcd(i, ans)
	return ans


def sum_of_squares(n):
	return (n*(n+1) * (2*n + 1)) / 6

def square_of_sums(n):
	sum_n = (n*(n+1)) / 2
	return sum_n ** 2

def p006(n):
	'''Find the difference between the sum of the squares of the first one hundred natural numbers 

	and the square of the sum.'''
	return square_of_sums(n) - sum_of_squares(n)


def is_prime(x):
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, int(round(math.sqrt(x)) + 1), 2):
			if x % i == 0:
				return False
		return True


def prime_range(n):
	low = int(round(n * math.log(n) + n * (math.log(math.log(n)) - 1)))
	high = int(round(n * math.log(n) + n * (math.log(math.log(n)))))
	prime_range = [x for x in range(low, high+1)]
	return list(filter(lambda x: is_prime(x) == True, prime_range))


def prime_count(n):
	count = 0
	for i in range(2, n+1):
		if is_prime(i) == True:
			count += 1
	return count


def p007(n):
	'''What is the 10 001st prime number?'''
	if n > 6:
		primes_list = prime_range(n)
		previous_primes = prime_count(primes_list[0])
		return primes_list[n - previous_primes]
	else:
		first_six = {1: 2, 2: 3, 3: 5, 4: 7, 5: 11, 6: 13}
		return first_six[n]


def string_product(s): 
	'''Takes a string of digits s and computes the product of each digit
	
	ex: string_product('1234') = 24'''
	return reduce(lambda x, y: int(x) * int(y), s)


def p008(n):
	'''Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.'''
	NUMBER = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
	return max(string_product(NUMBER[i: i+n]) for i in range(len(NUMBER) - n + 1))


def p009(target_number):
	'''There exists exactly one Pythagorean triplet for which a + b + c = 1000.

	Find the product abc.'''
	for a in range(1, 1000):
		for b in range(1, 1000):
			c = math.sqrt(a**2 + b**2)
			if (a+b+c == target_number) & (a < b) & (b < c):
				return int(a*b*c), (a,b,c)



def p010(max_val):
	'''Find the sum of all the primes below two million.'''
	return sum([i for i in range(2, max_val) if is_prime(i) == True])




