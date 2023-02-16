from mss import mss
from tkinter import *

x = 90
y = 570
x2 = 1170
y2 = 700
root = Tk()
root.geometry(str(x2-x)+'x'+str(y2-y+20))
root.resizable(False, False)
root["bg"]="black"
# Make the root window always on top
root.attributes("-topmost", True)
class Overrideredirect():
	def __init__(self, arg):
		# Make the root window noborder
		root.overrideredirect(arg)
close_button_x_y = [int(0), int(y2-y-10)]
update_button_x_y = [int(x2-x-65), int(y2-y-10)]
label_font=12
label_max_height = 6
sct = mss() #create opencv window
pos = {"x": x, "y": y, "x2": x2-x, "y2": y2-y}
mon = {"top": pos["y"], "left": pos["x"], "width": pos["x2"], "height": pos["y2"]}