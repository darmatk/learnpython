from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title("Menampilkan Pilihan")
root.iconbitmap('images/icon2.ico')
root.geometry("515x200")
root.resizable(width=False, height=False)

def openfile():
	filetext.delete(0, END)
	root.filename = filedialog.askopenfilename(
		initialdir="/tkinter/images",
		title="Pilih Gambar",
		filetypes=(("JPG Files", "*.jpg"),
			("Semua File", "*.*")))
	filetext.insert(0, root.filename)

def tampilkanGambar():
	global my_img
	top = Toplevel()
	top.title('Tampilkan Gambar')
	top.iconbitmap('images/icon2.ico')

	my_img = ImageTk.PhotoImage(
		Image.open(filetext.get()))
	lbl = Label(top, image=my_img).pack()
	Button(top, text="Keluar", command=top.destroy).pack()

def pilihslider():
	messagebox.showinfo("Tampilkan slide value",
		"Value Slide : " + str(horizontal.get()))

def tampilkanCheckbx():
	messagebox.showinfo("Tampilkan checkbox value", "Value Checkbox : " + varJenisKelamin.get())

def tampilkanDropdown():
	messagebox.showinfo("Tampilkan dropdown value", "Value Dropdown : " + varDropdown.get())

# frame layout untuk membuat frame
frame_img = LabelFrame(root, text="Open File")
frame_img.grid(row=0, column=0, columnspan=4, padx=5)

filetext = Entry(frame_img, width=70)
filetext.grid(row=0, column=0, pady=10, padx=5)

# button untuk mengambil gambar
button_file = Button(frame_img, text="Buka File", command=openfile)
button_file.grid(row=0, column=1, padx=5)

button_submit_file = Button(frame_img, text="Tampilkan", width=20, command=tampilkanGambar)
button_submit_file.grid(row=1, column=0, columnspan=2)

# membuat frame slider
frame_slider = LabelFrame(root, text="Slider")
frame_slider.grid(row=1, column=0, padx=5, sticky=W+E)

# menampilkan slider
horizontal = Scale(frame_slider, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack(anchor=W)

#menampilkan button slider
button_submit_slider = Button(frame_slider, text="OK", command=pilihslider)
button_submit_slider.pack(pady=5)

#frame untuk menampilkan checkbox
frame_checkbox = LabelFrame(root, text="Checkbox")
frame_checkbox.grid(row=1, column=1, padx=5, sticky=W+E)

varJenisKelamin = StringVar()

checkbxpria = Checkbutton(frame_checkbox, text="Pria", variable=varJenisKelamin, onvalue="Pria")
checkbxwanita = Checkbutton(frame_checkbox, text="Wanita", variable=varJenisKelamin, onvalue="Wanita")

checkbxpria.deselect()
checkbxwanita.deselect()
checkbxpria.pack(anchor=W)
checkbxwanita.pack(anchor=W)

button_submit_checkbox = Button(frame_checkbox, text="OK", command=tampilkanCheckbx)
button_submit_checkbox.pack()

#frame untuk menampilkan dropdown menu
frame_dropdown = LabelFrame(root, text="Dropdown Menu")
frame_dropdown.grid(row=1, column=2, padx=5, sticky=W+E)

pilihan_dropdown = [
	"Senin",
	"Selasa",
	"Rabu",
	"Kamis",
	"Jumat",
	"Sabtu",
	"Minggu"
]

varDropdown = StringVar()
varDropdown.set(pilihan_dropdown[0])

dropdownMenu = OptionMenu(frame_dropdown, varDropdown, *pilihan_dropdown)
dropdownMenu.pack()

btn_dropdown = Button(frame_dropdown, text="OK", command=tampilkanDropdown)
btn_dropdown.pack()

root.mainloop()
