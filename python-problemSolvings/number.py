def is_odd(num):
	if num % 2 ==0:
		return False
	else:
		return True


def evenify(num):
	check_odd = is_odd(num)
	if check_odd == True:

		   
		even_num = num*2
	else:
		even_num = num
	return even_num

result = evenify(3)
print(result)