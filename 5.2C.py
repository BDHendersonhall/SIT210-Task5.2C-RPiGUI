import tkinter as tk
import RPi.GPIO as GPIO
import time
    
# set up the board
GPIO.setmode(GPIO.BCM)

# define the colours and their pins
colours = [('red',14),('green',15),('blue',18)]

# set up the pins
for i in range(len(colours)):
    GPIO.setup(colours[i][1], GPIO.OUT)

def LED():
    for i in range(len(colours)):
        if colours[i][1] == v.get():
            GPIO.output(colours[i][1], GPIO.HIGH)
        else:
            GPIO.output(colours[i][1], GPIO.LOW)

def led_exit():
    for i in range(len(colours)):
        GPIO.output(colours[i][1], GPIO.LOW)
    window.destroy()
    
## GUI Definitions ##
window = tk.Tk()
window.title("LED Toggle")

v = tk.IntVar()
    
frame_a = tk.Frame(master=window, height = 10)
frame_a.pack(fill = tk.BOTH, side = tk.TOP, expand = True)

label_a = tk.Label(text = 'select LED to turn on', fg='white', bg='SlateGray3', width=20, height=3)
label_a.pack(fill = tk.X, side = tk.TOP, expand = True, padx = 10, pady = 5)

for i in range(len(colours)):
    tk.Radiobutton(text=colours[i][0], padx = 20, pady = 3, variable = v, value = colours[i][1], command = LED).pack(anchor=tk.W)

exitbutton = tk.Button(text = 'Exit', width = 20, command = led_exit)
exitbutton.pack(fill = tk.X, side = tk.BOTTOM, padx = 10, pady = 5, expand = True)

window.mainloop()

GPIO.cleanup()
