def is_isogram(value):
	value = value.lower()
	isogram = [i for i in value]
	if len(isogram) == len(set(isogram)):
		print(True)
	else:
		print(False)

value = input()
is_isogram(value)