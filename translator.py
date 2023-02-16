import time
from mss import mss
import cv2
import numpy
from config import *
import pytesseract
from googletrans import Translator
from tkinter import *
from config import Overrideredirect

class Translator_novels():
	@classmethod
	def update_text(self):
		rgb = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
		psm = pytesseract.image_to_string(rgb, lang='eng', config='--psm 1') #1-7 від чітко до розмито
		result = Translator().translate(psm, scr="en", dest='uk')
		return result.text

	@classmethod
	def change_mode(self):
		if self.mode == False:
			Overrideredirect(True)
			self.mode = True
		else:
			Overrideredirect(False)
			self.mode = False

	@classmethod
	def parse(self):
		# Make the root window alpha color
		root.attributes('-alpha',0)
		#generate pictures
		self.img = numpy.asarray(sct.grab(mon))
		# Make the root window alpha color
		root.attributes('-alpha',1)
		#Translate the text
		self.text_label['text'] = self.update_text()
		#press "q" to exit
		#if cv2.waitKey(25) & 0xFF == ord("q"):
		#cv2.destroyAllWindows()
	
	@classmethod
	def add_interface(self):
		self.mode = False
		self.text_label = Label(text="", height=label_max_height, justify=LEFT, font=label_font, bg="black", fg="white")
		self.text_label.place(x=0, y=0)
		Button(root, text="Update", font=6, command=self.parse, bg="black", fg="white").place(y=update_button_x_y[1], x=update_button_x_y[0])
		Button(root, text="Close", font=6, command=root.destroy, bg="black", fg="white").place(y=close_button_x_y[1], x=close_button_x_y[0])
		Button(root, text="Change mode", font=6, command=self.change_mode, bg="black", fg="white").place(y=close_button_x_y[1], x=close_button_x_y[0]+100)

if __name__ == '__main__':
	Translator_novels.add_interface()
	root.mainloop()