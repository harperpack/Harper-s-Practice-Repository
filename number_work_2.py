# more practice with numbers from Python Crash Course

import time

print ("Let's try counting to one million.")
time.sleep(2)  
print("Just kidding!  That would take a long time.")
one_million = (list(range(1,1000001)))

print ("\nThe smallest number in the list of the first million numbers is:")
print (min(one_million))

print ("\nThe largest number in the list of the first million numbers is:")
print (max(one_million))

print ("\nThe sum of the first million numbers is:")
print (sum(one_million))

