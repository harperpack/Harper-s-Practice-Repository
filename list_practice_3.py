# Still more practice with lists from Python Crash Course

guests = []
guests.append("josh raab")
guests.append("rosh jaab")
guests.append("david raab")
guests.append("large raab")
guests.append("brian raab")
guests.append("susan raab")
guests.append("baby raab")

print ("We have invited " + str((len(guests))) + " guests to our party.  Let us send them an invitation.")
guests_invited = []

# Send one invitation to each guest
while len(guests) > 0:
	popped_guests = guests.pop().title()
	# Save the items in a new list
	guests_invited.append(popped_guests)
	print ("\nHello, " + popped_guests + "!") 
	print ("\nWe are excited to invite you to our upcoming party. The party will be held at:")
	print ("\n\tRaab Household")
	print ("\t345 Millwood Road")
	print ("\tChappaqua, NY")
	print ("\nWe hope to see you there!  Please bring a gift.")
	print ("\nSincerely,")
	print ("\nTogg Ledley")
	print ("\n\n")
	
print (guests)
print (guests_invited)

too_heavy = guests_invited[-4]

print ("\nWe can't invite " + too_heavy + " because he is too heavy!")
guests_invited.remove(too_heavy)

new_invite = "Thin Raab"
print ("\nWe will invite " + new_invite + " instead.")

guests_invited.append(new_invite)

print ("\nHello, " + new_invite + "!") 
print ("\nWe are excited to invite you to our upcoming party. The party will be held at:")
print ("\n\tRaab Household")
print ("\t345 Millwood Road")
print ("\tChappaqua, NY")
print ("\nWe hope to see you there!  Please bring a gift.")
print ("\nSincerely,")
print ("\nTogg Ledley")
print ("\n\n")

new_invite_2 = "Tub Raab"
new_invite_3 = "Rub Raab"
new_invite_4 = "Slam Raab"
guests_invited.insert(0, new_invite_2)
guests_invited.insert(4, new_invite_3)
guests_invited.append(new_invite_4)

while len(guests_invited) > 0:
	popped_guests = guests_invited.pop()
	guests.append(popped_guests)
	print ("Hi " + popped_guests + "! We discovered we had a big table, so now we're inviting even more people!  \nRemember, the party's at the Raab Household!")
	print ("\n")

while len(guests) > 2:
	popped_guests = guests.pop()
	print ("So sorry, " + popped_guests + "!  Turns out we did not have the table, so you won't be able to come!  Hope you find something else to do.")
	print ("\n")
	
print (guests[0] + ", we had to downsize, but you're still invited to the party!  Looking forward to seeing you at the Raab Household.\n")
print (guests[1] + ", we had to downsize, but you're still invited to the party!  Looking forward to seeing you at the Raab Household.\n")

print (guests)

del guests[1]
del guests[0]

print (guests)
