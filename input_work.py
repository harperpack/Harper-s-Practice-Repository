# practice using input

phrase = input("What would you like to say? ")
print("Here's what you said: \n" + phrase)

# practice using str.format method

for day_num, day in enumerate(['Wed', 'Thurs', 'Fri'], 4):
    print('{} is the {} day of the week!'.format(day, day_num))
