"""Given a positive number n > 1 find the prime factor decomposition of n.
The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
"""

from collections import Counter

def prime_factors (n):
	i = 2
	factors = []
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			factors.append(i)
	if n > 1:
		factors.append(n)
	p = Counter(factors)
	string = ''
	for key, val in p.items():
		if val != 1:
			string += f'({key}**{val})'
		else:
			string += f'({key})'
	return string

prime_factors(86240)
