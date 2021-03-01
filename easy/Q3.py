def is_anagram(value, check_value):
	if len(value) != len(check_value):
		return False

	a = [i for i in value.lower()]
	# b = [i for i in check_value.lower()]
	
	for i in check_value.lower():
		try:
			a.remove(i)
		except:
			pass

	if a == []:
		return True
	else:
		return False

value = input()
check_value = input()
print(is_anagram(value, check_value))
