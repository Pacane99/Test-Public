#Simple GUI test
# import all tkinter in the program's global scope
from tkinter import *
# import requests for the http fetch
import requests
# create a root window
root = Tk()
#modify the window
root.title("Simple GUI")
root.geometry("200x100")
#create frame in the window to hold other widgets
app = Frame(root)
#invoque grid() method
app.grid()
#Window anf fram are now in place
##
#create a label in the frame
lbl = Label(app,text = "this is a label")
# invoke the lbl object's grid method
lbl.grid()
##
#create a button in the frame
button1 = Button(app,text = "Button1")
button1.grid()
button2 = Button(app)
button2.grid()
button3 = Button(app)
button3.grid()
#alternative 1 to label property
button2.configure(text = "Button2")
#alternative 2 to label property
button3["text"] = "button 3"
#test - modify label with currency valur
r = requests.get("http://www.apilayer.net/api/live?access_key=7a0b7a73ad149f3f992ffe00606675e6&format=1")
data = r.json()
a=data['quotes']['USDCAD']
#display new label for button 3
button3["text"] = str(a)


#kick off the window's event loop
root.mainloop()
