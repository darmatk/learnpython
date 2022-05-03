from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frame Layout")
root.iconbitmap('images/icon2.ico')

frame = LabelFrame(root, text="Radio Button", padx=50, pady=180)
frame.grid(row=0, column=0, padx=10, pady=10, rowspan=2)

frame2 = LabelFrame(root, text="Button", padx=130, pady=50)
frame2.grid(row=1, column=1, padx=10, pady=10)

frame3 = LabelFrame(root, text="Image", padx=10, pady=10)
frame3.grid(row=0, column=1, padx=10, pady=10)

TOPPINGS = [
	("Pepperoni", "Pepperoni"),
	("Cheese", "Cheese"),
	("Mushroom", "Mushroom"),
	("Onion", "Onion"),
	("Chili", "Chili")
]

my_img = ImageTk.PhotoImage(
		Image.open('images/husky2-355x282.jpg'))
my_label = Label(frame3, image=my_img)
my_label.pack()

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
	Radiobutton(frame, text=text, variable=pizza, value=topping).pack(anchor=W, padx=10)

button1 = Button(frame, text="Submit")
button1.pack()

button2 = Button(frame2, text="click me please")
button2.pack()

root.mainloop()
