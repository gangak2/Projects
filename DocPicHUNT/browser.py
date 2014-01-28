#$Id: entryfield.py,v 1.2 2004/03/17 04:29:31 mandava Exp $
#this is a program depicting the use of entry field widget.
#entry widgets are basic widgets used to collect input from the user.
#entry widgets are limited to a single line of text which can be in only
#one font. 
#the root is also packed with 4 buttons along with the entry widget..


import Tkinter 
from Tkinter import *
import docpic
suggest = 3


root =Tk()
root.title('DocPic HUNT')
Label (text='enter the file name').pack(side=TOP,padx=10,pady=10)


e=Entry(root, width=20)
e.pack()
e.focus_set()
print e.get()
def foo(a):
	temp = e.get()
	print temp
	if a == 0:
		docpic.image2text(temp,suggest)
	elif a == 1:
		docpic.image2image(temp,suggest)
	elif a == 2:
		docpic.text2image(temp,suggest)
	elif a == 3:
		docpic.text2text(temp,suggest)




Button(root, bg='grey',text='Image2Text', width=20,command= lambda :foo(0)).pack(side= LEFT)
Button(root, bg='grey',text='Image2Image', width=20,command= lambda : foo(1)).pack(side= LEFT)
Button(root, bg='grey',text='Text2Image', width=20,command=lambda : foo(2)).pack(side= RIGHT)
Button(root, bg='grey',text='Text2Text', width=20,command=lambda : foo(3)).pack(side= RIGHT)

root.mainloop()

