"""Calculate (1 / n!) * (1! + 2! + 3! + ... + n!) for a given n, where n is an integer greater or equal to 1."""
import math as m

def zero_or_infinity (n):
	latter = [m.factorial(i) for i in range(1, n + 1)]
	ans = (1 / m.factorial(n)) * (sum(latter))
	return round(ans,6)
