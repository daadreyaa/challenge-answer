def ascii_conversion(value, check_value):
	if check_value == None:	
		for i in value:
			print(chr(i), end=" ")

	if value == None:
		for i in check_value:
			print(ord(i), end=" ")

	# # print()
	
	# L = []
	# for i in check_value:
	# 	L.append(ord(i))

	# if value == L:
	# 	print(True)
	# else:
	# 	print(False)


get_input = input()
try:
	value = [int(i) for i in get_input.split()]
	check_value = None 
except:
	check_value = get_input
	value = None
# try:
# 	print(value)
# except:
# 	pass
# try:
# 	print(check_value)
# except:
# 	pass

ascii_conversion(value, check_value)
