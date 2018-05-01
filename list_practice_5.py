# Continued practice with lists, from Python Crash Course

pizzas = ["plain", "pepperoni", "olive", "anchovy", "artichoke"]
print ("I have create a list of my favorite types of pizza.")

# print a statement about each pizza
for pizza in pizzas:
	print ("\nOne of my favorite pizzas is " + pizza + " pizza.")
	
print ("\nAs you can see, I'm a big fan of pizza!")
print ("\nOne of my favorite things about pizza is the warm crust.")
print ("\nI think the only thing I like more than the crust is the cheese and the sauce!")
print ("\nAs you can tell, I think pizza is great!")

print ("\nSome of my favorite pizzas are those with toppings, like the following:")

pizza_toppings = []

for pizza in pizzas[1:]:
	print (pizza.title() + " pizza has a topping, which I think is super great!")
	print ("\n")
	
print ("\nI will now list my favorite pizza toppings, because I am practicing using lists:")
pizza_toppings = pizzas[1:]
for topping in pizza_toppings:
	print ("\nI like " + topping + " as a topping.")
	
print ("\n I would be remiss not to mention spinach and mushrooms!  And last, but not least, broccoli!")
pizza_toppings.append("spinach")
pizza_toppings.append("mushroom")
pizza_toppings.append("broccoli")

print ("\nHere are the first three items in my topping list:")
print (pizza_toppings[0:3])

print ("\nHere are three items from the middle of my topping list:")
print (pizza_toppings[2:5])

print ("\nHere are three items from the end of my topping list:")
print (pizza_toppings[-3:])

print ("\nLet us appreciate that the lists 'pizzas' and 'pizza_toppings' are distinct lists.")
print ("\nFirst, I will print the 'pizzas' list:")
count = 1
for pizza in pizzas:
	print ("Item # " + str(count) + " in my 'pizzas' list is " + pizza + ".")
	count = count + 1
	
print ("\nNow I will print the list of pizza toppings:")
count = 1
for topping in pizza_toppings:
	print ("Item # " + str(count) + " in my 'pizza_toppings' list is " + topping + ".")
	count = count + 1
	
print ("\nAre the two lists different?  Subarashi.")
