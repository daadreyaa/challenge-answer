def fibonnaci(size):
	a, b, c = -1, 1, 0
	fib = []
	for i in range(size):
		c = a+b
		fib.append(c)
		a = b
		b = c


	return fib

size = int(input())
print(fibonnaci(size))
