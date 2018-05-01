# practice with tuples from Python Crash Course

menu = ("fish", "chicken", "steak", "ox")
print ("Our restaurant has a set menu.  We only have the following items:\n")
for item in menu:
	print (item.title())

print ("\nWe cannot accept any subtitutions.")

print ("\nIt turns out the Queen of England is coming, and is allergic to our menu.  Our menu must change.")
print ("\nWe have developed a new menu for the Queen:")
menu = ("broccoli", "spinach", "pancakes", "rhubarb", "beans")
for item in menu:
	print (item.title())
	
print ("\nThe Queen is welcome to whichever item she pleases.")
print ("\nWe expect that " + menu[2] + " would only be eaten for breakfast.")
