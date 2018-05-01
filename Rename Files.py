# Explore os module during Udacity tutorial

import os
def rename():
    # obtain file names
    files = os.listdir(r"C:\Users\exchv\Pictures\prank")
    saved_path = os.getcwd()
    print("Current working directory is "+saved_path)
    os.chdir(r"C:\Users\exchv\Pictures\prank")
    # rename files
    for name in files:
        print("The old name was: "+name)
        os.rename(name,name.translate(None, "0123456789"))
        print("The new name is: "+name)
    os.chdir(saved_path)
      
rename()
