from pathlib import Path
#import os
import platform
import codecs
import tkinter as tk
from tkinter import filedialog
#from collections import Counter
#print(os.name)
print(platform.system())
#if platform.system()=='Windows':

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

def file_read(fname):
    with open(fname, 'r') as txt:
        #root = tk.Tk()
        #root.withdraw()
        #file_path = filedialog.askopenfilename()

    #txt = open(fname,encoding="UTF-8")
        file=txt.read()
    count = file.count('ý')
    #with open(fname, 'a') as txt:

        #txt.write("This is a test")
    print(file)
    print(count)
    #file=txt.read()
    #print(file.find('w'))



if file_path != "":
    file_read(file_path)
#elif file_path == "":
#    root = tk.Tk()
#    root.withdraw()
#    file_path = filedialog.askopenfilename()