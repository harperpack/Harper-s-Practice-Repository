# More practice with lists

names = ["harry", "chris", "josh raab", "rosh jaab", "adam levine", "ben ferguson"]

print (names[0].title() + " is a friend with whom I lived in New York")
print ("\n" + names[1].title() + " is a friend with whom I lived in Chicago")
print ("\n" + names[2].title() + " and " + names[-3].title() + " are each other's nemesis")

names[-3] = "David Raab"
print ("\n" + names[2].title() + " and " + names[-3].title() + " are each other's nemesis")
