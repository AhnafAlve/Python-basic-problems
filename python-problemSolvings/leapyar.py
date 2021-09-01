
##### Leap Year Detector ######

year = input("please inter a year: ")
year = int(year)

if year % 400 == 0:
	print("It's a leap year")
elif year % 100 == 0:
	print("Its not a leap year")
elif year % 4 == 0:
	print("It's a leap year")
else:
	print("It's not a leap year")