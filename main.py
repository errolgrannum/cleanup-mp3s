#!/usr/bin/python

from detect import *

from Tkinter import *
import tkMessageBox

from tkFileDialog import askdirectory


source_directory = None
destination_directory = None


def notification():
	tkMessageBox.showinfo("Transfer Complete", "Script is finished! "
		"Directory Mp3s have been transfered to destination directory")
	return

def locate():
	src_contents = retrieve_files(source_directory)
	dest_contents = retrieve_files(destination_directory)

	# print_file_info(src_contents)
	# print_file_info(dest_contents)

	#find and delete duplicate files between the two
	find_duplicates(src_contents, dest_contents)

	#move all the mp3s that are not within the new diretory to the new directory
	move_mp3s(src_contents, dest_contents)

	#notify user
	notification()
	

def set_source():
	global source_directory
	source_directory = askdirectory(parent=app,title="Please select a directory",
										 mustexist=True)
	if source_directory and destination_directory:
		locate()

def set_dest():
	global destination_directory
	destination_directory = askdirectory(parent=app,title="Please select a directory",
										 mustexist=True)
	if source_directory and destination_directory:
		locate()


# main window
app = Tk()
app.title("Cleanup Mp3s")
app.geometry("900x600+200+200")


src_button = Button(app, text="Select Source Directory", width=20, command=set_source)
src_button.pack(side="left", padx=15, pady=15)

dest_button = Button(app, text="Select Destination Directory", width=30, command=set_dest)
dest_button.pack(side="right", padx=15, pady=15)


app.mainloop()

