from tkinter import *
from tkinter import filedialog
from tkinter import font
root = Tk()
root.title('Redwan Islam -- Notepad-TextEditor')
root.geometry("1200x600")

#Create a new file function 
def new_file():
    my_text.delete("1.0",END)
    root.title('NewFile - TEditor')

#Create open file function
def open_file():
    my_text.delete("1.0", END)
    text_file = filedialog.askopenfilename(title="Open", filetypes=(("Text Files", "*.txt"),("All Files", "*.*"),("HTML Files", "*.html")))
    name = text_file
    name = name.replace("C:/Users/Redwan Islam/Downloads/","")
    root.title(f'{name} - TEditor')
    text_file=open(text_file,'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

#Save as file
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*",title="Save File", filetypes=(("Text Files", "*.txt"),("All Files", "*.*"),("HTML Files", "*.html")))
    if text_file:
        name = text_file
        name = name.replace("C:/Users/Redwan Islam/Downloads/","")
        root.title(f'{name} - TEditor')
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0,END))
        text_file.close()


# Create a mainFrame
my_frame = Frame(root)
my_frame.pack(pady=5)

#Create a Scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side = RIGHT, fill = Y)

#Create a Text box
my_text = Text(my_frame, width=97, height=25, font=("Helvetica",16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

#Configure our Scrollbar
text_scroll.config(command = my_text.yview)

#Create menu 
my_menu = Menu(root)
root.config(menu = my_menu)

#Add File menu
file_menu = Menu(my_menu,tearoff = False)
my_menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", command = new_file)
file_menu.add_separator()
file_menu.add_command(label = "Open", command = open_file)
file_menu.add_separator()
file_menu.add_command(label = "Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = root.quit)

#Add Edit menu
edit_menu = Menu(my_menu,tearoff = False)
my_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Cut")
edit_menu.add_separator()
edit_menu.add_command(label = "Copy")
edit_menu.add_separator()
edit_menu.add_command(label = "Undo")
edit_menu.add_separator()
edit_menu.add_command(label = "Redo")

root.mainloop()