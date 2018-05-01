# working with numbers from Python Crash Course

print ("I can print each of the integers from 1 to 20. Look and see!")
numbers = list(range(1,21))
print (numbers)

print ("\nI can also print them vertically, like a pro:")
for number in numbers:
	print (number)

# explore using the third argument of the range function
print ("\nI can now show you all of the odd numbers from 1 to 20. Just take another look:")
odd_numbers = list(range(1,21,2))
for number in odd_numbers:
	print (number)

print ("\nI can go beyond and print the multiples of 3 between 3 and 30.  Almost like I'm a wizard!")
multiples = list(range(3,31,3))
for multiple in multiples:
	print (multiple)

# list comprehension - create a list in one line
print ("\nNow, let us practice list comprehension...")
cubes = [cube**3 for cube in range(1,11)]
for cube in cubes:
	print (cube)
