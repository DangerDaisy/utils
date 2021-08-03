# Takes all files with user-provided extensions extensions and sorts them alphabetically in a destination folder

from pathlib import *
import os
import shutil
import sys

# Creates a single folder '0-9' instead of giving eacht number its own folder
group_numbers_together = True

folder_to_sort = ""
output_folder = ""
extensions = []

def parse_command_line_arguments():
	global folder_to_sort
	global output_folder
	global extensions

	if len(sys.argv) < 4 or sys.argv[1] == "--help":
		print("Usage: \"file_sorter.py source_folder destination_folder [extensions (without leading '.')]\"")
		return False
	
	folder_to_sort = sys.argv[1]
	output_folder = sys.argv[2]
	
	for index in range(3, len(sys.argv)):
		extensions.append(sys.argv[index])

	return True

def create_folder(folder_to_create):
	try:
		os.makedirs('./' + folder_to_create, 777)
	except FileExistsError:
		print("Folder '" + folder_to_create + " 'already exists")
		return
	print("Folder '" + folder_to_create + "' not found, creating...") 

def get_file_extension(file_to_strip):
	return os.path.splitext(file_to_strip)[1][1:]

def get_files_from_folder(folder):
	items = []
	path = Path(folder)
	for current_item in path.iterdir():
		if os.path.isdir(current_item):
			items += get_files_from_folder(current_item)
			continue;
		if get_file_extension(current_item) in extensions:
			items.append(str(current_item))
	
	return items

def sort_files():
	items_to_sort = get_files_from_folder(folder_to_sort)
	for current_item in items_to_sort:
		destination_folder = output_folder + "/"
		
		current_file_name = os.path.basename(current_item)
		print("Current file: " + str(current_file_name))

		first_character = str(current_file_name)[0]

		if first_character.isnumeric() and group_numbers_together:
			destination_folder += "0-9"
		else:
			destination_folder += first_character.upper()

		create_folder(destination_folder)
		shutil.copyfile(str(current_item), os.path.join(destination_folder, str(current_file_name)))

def main():
	if(parse_command_line_arguments()):
		create_folder(output_folder)
		sort_files()

if __name__ == "__main__":
	main()

# get_files_from_folder
	