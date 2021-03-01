def is_palindrome(value):
	if value == value[::-1]:
		return True
	else:
		return False

value = input()
print(is_palindrome(value))
