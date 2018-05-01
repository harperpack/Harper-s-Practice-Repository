# Still practicing with lists, from Python Crash Course

locations = ["japan", "korea", "vietnam", "cambodia", "new zealand"]

print (locations)
print ("\n")

# Adjust each item in the list to be capitalized
for location in locations:
	locations.remove(location)
	location = location.title()
	locations.insert(0, location)
	
print ("Here is a list of places I would like to go:")
print (locations)

print("\nHere is a list of places I would like to go, sorted alphabetically:")
print (sorted(locations))

print ("\nThe order of the original list has not changed:")
print (locations)

print ("\nHere is a list of places I would like to go, sorted in reverse alphabetical order:")
print (sorted(locations, reverse=True))

print ("\nThe order of the original list still has not changed:")
print (locations)

print ("\nAnd now we have reversed the order of the list:")
locations.reverse()
print (locations)

print ("\nLo! the list has been returned to its original order:")
locations.reverse()
print (locations)

print ("\nLet's sort the list alphabetically - for real this time:")
locations.sort()
print (locations)

print ("\nAnd now we will print the list in reverse alphabetical order:")
locations.sort(reverse=True)
print (locations)
