import customtkinter as custom
import tkinter as tk
from PIL import Image, ImageTk
import datetime

# creating an empty list
list_of_tasks = []

# FUNCTIONS TO PERFORM OPERATIONS
# functions to perform operations
def open_file():
    try:
        with open(file='./to_do_list.txt', mode='r') as file:
            data = file.readlines()
            for task in data:
                if task != '\n':
                    list_of_tasks.append(task)
                    box.insert(tk.END, task)
    except:
        file = open(file='to_do_list', mode='w')
        file.close()


# function to add a task to the list
def add_task():
    task = task_entry.get()
    task_entry.delete(0, tk.END)
    if task:
        if task in list_of_tasks:
            pass
        else:
            list_of_tasks.append(task)
            with open(file='./to_do_list.txt', mode='a') as file:
                file.write(f"\n{task}")
            list_of_tasks.append(task)
            box.insert(tk.END, task)


# function to delete a task from the list
def delete_task():
    t = str(box.get(tk.ANCHOR))
    if t in list_of_tasks:
        list_of_tasks.remove(t)
        with open(file='./to_do_list.txt', mode='w') as file:
            for i in list_of_tasks:
                file.write(f"{i}\n")
        box.delete(tk.ANCHOR)


# function for dark mode
def dark_mode():
    window.config(bg='#242424')
    add_button.configure(bg_color='#3572EF', fg_color='#3572EF')
    delete_button.configure(bg_color="#242424", fg_color='#242424', text_color='white', hover_color='black')
    date_label.configure(bg_color='white', text_color='#242424', fg_color='white')


# function for light mode
def light_mode():
    window.config(bg='white')
    add_button.configure(bg_color='black', fg_color='black', text_color='white', hover_color='#242424')
    delete_button.configure(bg_color='whitesmoke', fg_color='whitesmoke', hover_color='yellowgreen', text_color='black')
    date_label.configure(bg_color='#242424', fg_color='#242424', text_color='white')


# setting up the window
window = custom.CTk()
window.geometry("500x500")
window.config(bg='white')
window.title('THE TO DO LIST')

# setting up the header
header_path = Image.open('./resources/header.png')
header = ImageTk.PhotoImage(header_path)
label_header = custom.CTkLabel(master=window, image=header, text="")
label_header.pack()

# setting up the designed logo
logo_path = Image.open('./resources/LOGO.png')
logo = ImageTk.PhotoImage(logo_path)
label_logo = custom.CTkLabel(master=window, image=logo, text="")
label_logo.place(x=10, y=10)

# creating the frame
frame = custom.CTkFrame(window, width=300, height=257)
frame.place(x=100, y=190)

# creating the entry box
task_entry = custom.CTkEntry(frame, width=275, font=('Times New Roman', 20, 'normal'))
task_entry.place(x=10, y=8)
task_entry.focus()

# creating the add button
add_button = custom.CTkButton(window, text="ADD", font=('Times New Roman', 24, 'normal'), bg_color='black',
                              fg_color='black', text_color='white', hover_color='#242424', width=300, height=25,
                              command=add_task)
add_button.place(x=100, y=150)

# creating the list frame
frame_1 = custom.CTkFrame(window, border_width=3, width=300, height=230, fg_color='#A7E6FF')
frame_1.pack(pady=(135, 0))

# creating the list box
box = tk.Listbox(frame_1, bg='#A7E6FF', fg='black', bd=0, font=('Times New Roman', 20, 'normal'), cursor='hand2',
                 selectbackground='black', selectforeground='white', height=1, width=30)
box.pack(side=tk.LEFT, fill=tk.BOTH, padx=1)

# creating the scrollbar
scroll_bar = custom.CTkScrollbar(frame_1, bg_color='#050C9C', button_color='#A7E6FF')
scroll_bar.pack(side=tk.RIGHT, fill=tk.BOTH)
box.config(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=box.yview)

# creating the delete button
delete = Image.open('./resources/delete.png')
delete_img = custom.CTkImage(delete)
delete_button = custom.CTkButton(window, image=delete_img, bg_color='white', text="DELETE", fg_color='whitesmoke',
                                 text_color="black", command=delete_task, hover_color='yellowgreen')
delete_button.pack(pady=8)

# creating the dark mode button
dark = Image.open('./resources/moon.png')
dark_img = custom.CTkImage(dark)
dark_button = custom.CTkButton(window, image=dark_img, width=10, height=10, text="", bg_color='#050C9C',
                               fg_color='#050C9C', command=dark_mode)
dark_button.place(x=450, y=10)

# creating the light mode button
light = Image.open('./resources/sun.png')
light_img = custom.CTkImage(light)
light_button = custom.CTkButton(window, image=light_img, width=10, height=10, bg_color='#050C9C', fg_color='#050C9C',
                                text="", command=light_mode)
light_button.place(x=400, y=10)

# creating the today's date label
date_label = custom.CTkLabel(master=window, text=f"TODAY'S DATE: {datetime.date.today()}",
                             font=('Times New Roman', 20, 'bold'), text_color='white', fg_color='#242424', height=20,
                             width=60)
date_label.place(x=125, y=118)

open_file()

window.mainloop()
