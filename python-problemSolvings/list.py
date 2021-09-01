year = input("please give an integer: ")
year = int(year)

if year % 4 != 0:
	print("its not a leap year")
else:
	if year % 100 == 0:
		if year % 400 == 0:
			print("its a leap year")
		else:
			("its not a leap year")
	else:
		print("its a leap year")