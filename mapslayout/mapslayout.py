from tkinter import *
import tkintermapview

root = Tk()
root.title('Maps Bali')
root.geometry("600x600")

def tambahMarker(coords):
	print("Tambah Marker: ", coords)
	new_marker = map_widget.set_marker(coords[0],
		coords[1], text="Marker Baru")

#Membuat label map
maps_label = LabelFrame(root)
maps_label.pack()

map_widget = tkintermapview.TkinterMapView(maps_label,
	width=600, height=600, corner_radius=0)

map_widget.set_tile_server(
	"https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",
	max_zoom=22)

#melakukan set kordinat
map_widget.set_position(-8.579025, 115.301351) #Bali
map_widget.set_zoom(10)

map_widget.add_right_click_menu_command(
	label="Tambah Marker",
	command=tambahMarker,
	pass_coords=True)

map_widget.pack(fill="both", expand=True)

root.mainloop()
