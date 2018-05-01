# Program to explore strings and variables in Python

import time
import webbrowser

# Store a string as a variable
message = "Hello, world!"
print (message)

# Update that variable
message = "Hello, Friday evening after work!"
print (message)

count = 1
count_max = 5
print ("\n\t The first number is: " + str(count))

# Explore a while loop
while count < count_max:
	count = count + 1
	print ("\n\t The next number is: " + str(count))
	# Push the limit upwards so the loop continues; alternatively, could have set count_max higher earlier
	count_max = count_max + 0.5
		
print ("\nWe did it.  We counted to " + str(count) + "!")

# Explore test formatting like \n (new line) and \t (new tab)
print ("Now, please enter your name: ")
time.sleep(2)
print ("\n...")
time.sleep(2)
print ("\n...")
time.sleep(2)
print ("\n...")
# Enter a variable because I don't yet know how to request input from the user
name = " harper pack "
print ('\nFine.  I will "guess" what you would have entered.  Your name is...')
print ("\n... *swirling mytstic guessing mist surrounds the screen* ...")
print ("\nYour name is " + name)
time.sleep(1)
print ("\nWait, that's not right...")
# Remove unnecessary spaces around either side of the input
name = name.strip()
print ("\nYour name is " + name.upper())
time.sleep(1)
print ("\n That's not quite it either.  One second...")
time.sleep(1)
print ("\nYour name is " + name.title())
print ("\nNow let us celebrate with music.")
time.sleep(1)
# At the time I was into Porter Robinson and this song in particular
webbrowser.open("https://www.youtube.com/watch?v=HAIDqt2aUek")


