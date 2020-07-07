"""
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
"""

# best practice
def increment_string_best (strng):
	head = strng.rstrip('0123456789')
	tail = strng[len(head):]
	if tail == "": return strng + "1"
	return head + str(int(tail) + 1).zfill(len(tail))

# personal solution
def increment_string (s):
	if not (s[-1] in '0123456789'):
		s += '1'
		return s
	digit = int(s[-1])
	if digit != 9:
		s = s[:-1]
		s += str(digit + 1)
	else:
		count = 0
		while s[-1] == '9':
			s = s[:-1]
			count += 1
		if not (s[-1] in '0123456789'):
			s += str(digit + 1)
			s += count * '0'
		else:
			digit = int(s[-1])
			s = s[:-1]
			s += str(digit + 1)
			s += count * '0'
	return s

# extra stuff
def digit_length (s):
	global start
	for i, c in enumerate(s):
		if c.isdigit():
			start = i
			break
	length = len(s[start:])
	return length
