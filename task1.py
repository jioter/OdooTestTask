def even_or_odd(x):
	if x == 0:
		return Error
	if x % 2 != 0:
		return 'Odd'
	else:
		return 'Even'

assert even_or_odd(22) == 'Even'
