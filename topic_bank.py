import tkinter as tk
from tkinter import *
import random

topic_bank_directory = 'C:/'
topic_bank_filename = topic_bank_directory + "topic_bank.txt"


def topic_bank_from_file(filename):
    topic_bank_file_openage = open(topic_bank_filename, 'r')
    topic_bank = topic_bank_file_openage.read().splitlines()
    print(topic_bank)
    topic_bank_file_openage.close()

    return topic_bank

topic_list = topic_bank_from_file(topic_bank_filename)
global randoms_list
randoms_list = topic_list.copy()

def write_topic_to_file(event=None):
    topic_string = str(topic_entry_var.get())
    topic_bank_file_openage = open(topic_bank_filename, 'a')

    topic_bank_file_openage.write(topic_string)
    topic_bank_file_openage.write('\n')

    topic_bank_file_openage.close()
    topic_entry_var.set("")
    root.update()


def reset():
    global randoms_list
    randoms_list = topic_list.copy()
    print(randoms_list)
    random_topic_str.set("")
    root.update()


def choose_random_topic():
    print(len(randoms_list))
    topic_index = random.randint(0, len(randoms_list)-1)
    print(topic_index)
    print(randoms_list[topic_index])
    random_topic_str.set(randoms_list[topic_index])
    root.update()
    randoms_list.remove(randoms_list[topic_index])
    if len(randoms_list) == 0:
        random_topic_str.set("Out of topics! Press the reset button to start again")


root = tk.Tk()
root.title('Topic Bank')
root.iconbitmap("PL_icon.ico")
choice_colour = '#cfb7e5'
root['background']=choice_colour


# Label 1
topic_entry_label = tk.Label(root, text="Enter new topic", width=60, height=1)
topic_entry_label.grid(row=0, column=0, columnspan=2)
topic_entry_label['background'] = choice_colour

# Entry 1
topic_entry_var = tk.StringVar()
topic_entry_var.set("")
topic_entry = tk.Entry(root, textvariable = topic_entry_var, width=60)
topic_entry.grid(row=1, column=0, columnspan=2)
# topic_entry.delete(0, "end")  # Clear the entry box

# Button 1
enter_topic_button = tk.Button(root, text='Enter topic', command=write_topic_to_file, width=30, height=1)
enter_topic_button.grid(row=3, column=0, columnspan=3)
# plus allow pressing enter key to to the same as the above button:
root.bind('<Return>', write_topic_to_file)

# Label 2
topic_entry_label = tk.Label(root, text="", width=60, height=1)
topic_entry_label.grid(row=4, column=0, columnspan=2)
topic_entry_label['background'] = choice_colour

# Label 3
topic_entry_label = tk.Label(root, text="View random topic", width=60, height=1, anchor='center')
topic_entry_label.grid(row=5, column=0, columnspan=2)
topic_entry_label['background'] = choice_colour

# Button 2
random_topic_button = tk.Button(root, text='Pick random topic', command=choose_random_topic, width=30, height=1)
random_topic_button.grid(row=6, column=0, columnspan=1)

# Button 3
random_topic_reset_button = tk.Button(root, text='Reset random topics', command=reset, width=30, height=1)
random_topic_reset_button.grid(row=6, column=1, columnspan=1)

# Label 4
random_topic_str = tk.StringVar()
random_topic_str.set("")
random_topic_label = tk.Label(root, textvariable=random_topic_str, relief=SUNKEN, width=60, height=1, anchor='center')
random_topic_label.config(bg="white")
random_topic_label.grid(row=7, column=0, columnspan=2)

# Label 5
topic_entry_label = tk.Label(root, text="", width=60, height=1)
topic_entry_label.grid(row=8, column=0, columnspan=2)
topic_entry_label['background'] = choice_colour

root.mainloop()
