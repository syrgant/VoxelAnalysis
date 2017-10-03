#ask for file
import re
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
f=open(file_path,'r')
list_of_sentences = f.readlines()


for line in list_of_sentences:
	if (line[0:2] != "//" and line != "\n"):
		#if (line[-3])
		list_coord = line[0:-1].split("\t")
		for one_coord in list_coord:
			#if "-" at [0] then make it negative
			list(map(int, one_coord))

		print (list_coord)