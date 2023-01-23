from tkinter import *


main_window =Tk() #Creating an instance of tkinter class

#Labels
'''to add this label to the main window we can use .grid method
or .pack method, .grid method converts the labels into rows and columns
There can be n number of rows and index starts from 0. Another is the pack
method, this is used to relocate the defualt widget to the borders '''


Label(main_window, text="Hello world") 
main_window.mainloop()