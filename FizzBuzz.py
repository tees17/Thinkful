#committing a change for the sake of committing a change
for i in range (1,100):
	if i % 3 == 0 and i % 5 == 0:
		i=str(i)
		print(i+"FizzBuzz")
	elif i % 3 == 0:
		i=str(i)
		print(i+"Fizzy")
	elif i % 5 == 0:
		i=str(i)
		print(i+"Buzzy")
	else:
		print(i)
