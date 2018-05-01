# Explore webbrowser module during Udacity tutorial

import webbrowser
import time

variable = 1
variable_max = 4

while (variable < variable_max):
    time.sleep(30)
    webbrowser.open("https://www.youtube.com/watch?v=HAIDqt2aUek")
    variable = variable + 1
