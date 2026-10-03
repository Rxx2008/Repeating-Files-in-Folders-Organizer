import os
import shutil
from tkinter import *
from tkinter import filedialog

filepath = ''
dirA = 'empty'
dirB = ''
dirDir = ''


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


tk = Tk()
tk.geometry("400x200")
center_window(tk)


def opendir(bttype):
    global dirA
    global dirB
    global dirDir
    if bttype == 'a':
        dirA = filedialog.askdirectory()
        t_dirA = Label(tk, text=dirA, anchor='center', justify='center')
        t_dirA.place(relx=0.16, rely=0.15)
    if bttype == 'b':
        dirB = filedialog.askdirectory()
        t_dirB = Label(tk, text=dirB, anchor='center', justify='center')
        t_dirB.place(relx=0.16, rely=0.42)
    if bttype == 'dir':
        print('a')
        dirDir = filedialog.askdirectory()
        t_dirDir = Label(tk, text=dirDir, anchor='center', justify='center')
        t_dirDir.place(relx=0.16, rely=0.69)


def start():
    tk.quit()

def split_file(lao_file, xin_file):
    city, typ = os.path.splitext(lao_file)
    if typ == '':
        shutil.copytree(lao_file, xin_file)
    else:
        shutil.copyfile(lao_file, xin_file)



tk.focus_force()

buttonA = Button(tk, text='Open File A', command=lambda: opendir('a'))
buttonA.place(relx=0.16, rely=0.0, relwidth=0.7)
#buttonA.pack()

buttonB = Button(tk, text='Open File B', command=lambda: opendir('b'))
buttonB.place(relx=0.16, rely=0.27, relwidth=0.7)
#buttonB.pack()

buttonDir = Button(tk, text='Choose directory for processed files', command=lambda: opendir('dir'))
buttonDir.place(relx=0.16, rely=0.54, relwidth=0.7)
#buttonDir.pack()

buttonPro = Button(tk, text='Continue', command=start)
buttonPro.place(relx=0.77, rely=0.85)
#buttonPro.pack()

tk.mainloop()

file_rep = os.listdir(dirDir)

fileA = os.listdir(dirA)
fileB = os.listdir(dirB)

#fix bug for mac
if ".DS_Store" in fileA:
    fileA.remove(".DS_Store")

if ".DS_Store" in fileB:
    fileB.remove(".DS_Store")

new_dir_name_beta = 'precessed files'
new_dir_name = new_dir_name_beta
rep = 1
while True:
    if new_dir_name in file_rep:
        rep += 1
        new_dir_name = new_dir_name_beta + str(rep)
    else:
        break

new_dir = dirDir + '/' + new_dir_name
os.mkdir(new_dir)

sameA = new_dir + '/same in A'
sameB = new_dir + '/same in B'
difAB = new_dir + '/different in A and B'
difA = new_dir + '/different in A'
difB = new_dir + '/different in B'

sameA.replace('\\', '/')
sameB.replace('\\', '/')
difAB.replace('\\', '/')
difA.replace('\\', '/')
difB.replace('\\', '/')
os.mkdir(sameA)
os.mkdir(sameB)
os.mkdir(difAB)
os.mkdir(difA)
os.mkdir(difB)

for i in fileA:
    old_file = dirA + '/' + i
    if i in fileB:
        new_file = sameA + '/' + i
        split_file(old_file, new_file)
    else:
        new_file = difA + '/' + i
        split_file(old_file, new_file)

for i in fileB:
    old_file = dirB + '/' + i
    if i in fileA:
        new_file = sameB + '/' + i
        split_file(old_file, new_file)
    else:
        new_file = difB + '/' + i
        split_file(old_file, new_file)
