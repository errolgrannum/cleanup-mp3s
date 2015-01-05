#!/usr/bin/python

import shutil
import os


"""store the filename,make sure the file is an mp3, store the size of the file. 
compare if the original file exists within the new directory if it does The file 
should be deleted"""


#store the names and stats of files within a directory into a dictionary
def retrieve_files(directory):
	for root, dirs, files in os.walk(directory):
			dir_contents = {}
			dir_contents[directory] = root # save the directory name
			for name in files:
				if not name.startswith('.'):
					file_stats = os.stat(os.path.join(root,name))
					dir_contents[name] = file_stats
			return dir_contents


# get the folder names from given directory dictionary
def retrieve_directory_name(directory):
	for key, val in directory.items():
		if not hasattr(val, 'st_size'):
			return val


# print the contents of a directory
def print_file_info(file_dict):
	for key, val in file_dict.items():
		if hasattr(val, 'st_size'):
			print key, "=>", val.st_size



# remove the copied items from the original directory (dir2)
def delete_duplicates(file_name, original_directory):
	for key, val in original_directory.items():
		if not hasattr(val, 'st_size'):
			directory_name = val # the value that doesnt contain os stats is the directory name
	os.remove(os.path.abspath(os.path.join(directory_name,file_name)))


# pre : 2 parmeters takes two dictionaries, which represent their contents within
# post : duplicates will be detected
def find_duplicates(src_dir, dest_dir):
	key1 = dest_dir.keys()
	key2 = src_dir.keys()
	match = [items for items in key1 if items in key2]
	"""if the os stats are similar, theres a good indicator we have detected 
	duplicates"""
	for files in match:
		if dest_dir[files].st_size == src_dir[files].st_size:
			delete_duplicates(files,src_dir)
	
# if mp3 items are not in the new directory, move them from the original
def move_mp3s(src_dir, dest_dir):	
	original_dir = retrieve_directory_name(src_dir)	
	new_dir = retrieve_directory_name(dest_dir)
	for files in os.listdir(os.path.abspath(original_dir)):
		if files.endswith(".mp3"):
			shutil.move(os.path.abspath(os.path.join(original_dir,files)),new_dir)
			

