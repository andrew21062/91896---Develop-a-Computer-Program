# Andrew Wong
#30/7/24
# version 2.31

# import tkinter 
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
import random

def validate_int_input(char):
    return char.isdigit()

# quit function
def quit():
    main_window.destroy()
    
# print details function
def print_details ():
    # details window
    details_window = Tk()
    details_window.geometry('1010x270')
    details_window.resizable(width=False, height=True)
    details_window.title('All details')
    details_window.configure(bg='lightblue')
   
    
    # create the column headings
    name_count = 0
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Recipe number   ").grid(column=0,row=13)
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Name   ").grid(column=1,row=13)
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Hired date   ").grid(column=2,row=13)
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Fork   ").grid(column=3,row=13)
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Spoons   ").grid(column=4,row=13)
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Paper plates   ").grid(column=5,row=13)
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Paper cup   ").grid(column=6,row=13)
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Party hats   ").grid(column=7,row=13)
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Ballons   ").grid(column=8,row=13)
    # add each item in the list into its own row
    while name_count < counters['total_entries'] :
        Label(details_window, font=("Helvetica", 15), bg='lightblue', text=name_count).grid(column=0,row=name_count+15) 
        Label(details_window, font=("Helvetica", 15), bg='lightblue', text=(all_details[name_count][0])).grid(column=1,row=name_count+15)
        Label(details_window, font=("Helvetica", 15), bg='lightblue', text=(all_details[name_count][7])).grid(column=2,row=name_count+15)
        Label(details_window, font=("Helvetica", 15), bg='lightblue', text=(all_details[name_count][2])).grid(column=3,row=name_count+15)
        Label(details_window, font=("Helvetica", 15), bg='lightblue', text=(all_details[name_count][3])).grid(column=4,row=name_count+15)
        Label(details_window, font=("Helvetica", 15), bg='lightblue', text=(all_details[name_count][4])).grid(column=5,row=name_count+15)
        Label(details_window, font=("Helvetica", 15), bg='lightblue', text=(all_details[name_count][5])).grid(column=6,row=name_count+15)
        Label(details_window, font=("Helvetica", 15), bg='lightblue', text=(all_details[name_count][6])).grid(column=7,row=name_count+15)
        Label(details_window, font=("Helvetica", 15), bg='lightblue', text=(all_details[name_count][1])).grid(column=8,row=name_count+15)
        name_count +=  1
        counters['name_count'] = name_count

# check the inputs are all valid
def check_inputs ():
    input_check = 0

    # check the hire date, if it is empity then send erroe message
    if len(name_entry.get()) == 0:
        messagebox.showerror('  Error  ', 'Please entre your full name !')
        input_check = 1
    
    # check the name entry, if it is not only alphabets or empity then send error message
    if (name_entry.get().replace(' ','').isdigit()):  
        messagebox.showerror('  Error  ', 'Please entre your full name !')
        input_check = 1

    # check the item boxes' entry, if it is empity then send erroe message
    if len(item_1_forks.get()) ==0 or len(item_2_spoons.get()) ==0 or len(item_3_Paper_Plates.get()) ==0 or len(item_4_Paprt_Cups.get()) ==0 or len(item_5_Party_hats.get()) ==0 or len(item_6_Paprt_Ballons.get())== 0:
        messagebox.showerror('  Error  ', 'Please entre 0 if you do not need the item.')
        input_check = 1

    # check the item boxes' entry, if they are over 500 then send error message
    if int(item_1_forks.get()) > 500 or int(item_2_spoons.get()) > 500 or int(item_3_Paper_Plates.get()) > 500 or int(item_4_Paprt_Cups.get()) > 500 or int(item_5_Party_hats.get()) > 500 or int(item_6_Paprt_Ballons.get()) > 500:
        messagebox.showerror('  Error  ', 'We do not have over 500 items !')
        input_check = 1
        
    # check the hire date, if it is empity then send erroe message
    if len(hire_date.get()) == 0:
        messagebox.showerror('  Error  ', 'Hire date Must not be 0 !')
        input_check = 1

    # check the hire date, if it is 0 then send erroe message
    if int(hire_date.get()) >= 1:
        pass
    else:
        messagebox.showerror('  Error  ', 'Hire date Must not be 0 !')
        input_check = 1

    # if there is no errors then input_check will equal to 0 and jump to append_name, otherwise nothing will happen
    if input_check == 0: append_name()
        

def append_name ():
    # append each item to its own area of the list
    all_details.append([name_entry.get(),item_1_forks.get(),item_2_spoons.get(),item_3_Paper_Plates.get(),item_4_Paprt_Cups.get(),item_5_Party_hats.get(),item_6_Paprt_Ballons.get(),hire_date.get()])
    # clear the boxes
    name_entry.delete(0,'end')
    item_1_forks.delete(0,'end')
    item_2_spoons.delete(0,'end')
    item_3_Paper_Plates.delete(0,'end')
    item_4_Paprt_Cups.delete(0,'end')
    item_5_Party_hats.delete(0,'end')
    item_6_Paprt_Ballons.delete(0,'end')
    hire_date.delete(0,'end')
    counters['total_entries'] += 1
    Label(main_window, font=("Helvetica", 19, "bold"), bg='gray100', text=counters['total_entries'], width=4, borderwidth=2, relief="sunken").grid(column=1,row=1)

# delete a row from the list
def delete_row ():
    # find which row is to be deleted and delete it
    if counters['total_entries'] == 0:
        messagebox.showerror('  Error  ', 'There are not details !')
    else:
        del all_details[int(delete_item.get())]
        counters['total_entries'] -= 1
        name_count = counters['name_count']
        delete_item.delete(0,'end')
        # clear the last item displayed on the GUI
        Label(main_window, font=("Helvetica", 16, "bold"), text="       ").grid(column=0,row=name_count+15) 
        Label(main_window, font=("Helvetica", 16, "bold"), text="       ").grid(column=1,row=name_count+14)
        Label(main_window, font=("Helvetica", 16, "bold"), text="       ").grid(column=2,row=name_count+14)
        Label(main_window, font=("Helvetica", 16, "bold"), text="       ").grid(column=3,row=name_count+14)
        Label(main_window, font=("Helvetica", 16, "bold"), text="       ").grid(column=4,row=name_count+14)
        Label(main_window, font=("Helvetica", 16, "bold"), text="       ").grid(column=5,row=name_count+14)
        Label(main_window, font=("Helvetica", 16, "bold"), text="       ").grid(column=6,row=name_count+14)
        Label(main_window, font=("Helvetica", 16, "bold"), text="       ").grid(column=7,row=name_count+14)
        # print all the items in the list
        print_details()
    
# create the buttons and labels
def setup_buttons():
    # create all the labels, buttons and spinboxes. Put them in the correct grid 
    Button(main_window, font=("Helvetica", 16, "bold"), text="Delete Row", command=delete_row, width=9, bg="red", fg="white").grid(column=4,row=11,sticky=E) 
    Button(main_window, font=("Helvetica", 16, "bold"), text="Quit", command=quit, width=5, fg="white", bg="red").grid(column=7,row=0,pady=5,sticky=E)
    Button(main_window, font=("Helvetica", 16, "bold"), text="Append Details",borderwidth=2, bg="yellow", command=check_inputs).grid(column=1,row=10)
    Button(main_window, font=("Helvetica", 16, "bold"), bg='gray100', text="Print Details", command=print_details, width=10).grid(column=0,row=12,padx=3, pady=3, sticky=W)
    Label(main_window, font=("Helvetica", 16), bg='gray100', text="Full Name", width=9, borderwidth=2, relief="sunken").grid(column=0,row=0,padx=6,sticky=E)
    Label(main_window, font=("Helvetica", 16), bg='gray100', text="Recipe Number", width=13, borderwidth=2, relief="sunken").grid(column=0,row=1,sticky=E)
    Label(main_window, font=("Helvetica", 19, "bold"), bg='gray100', text=counters['total_entries'], width=4, borderwidth=2, relief="sunken").grid(column=1,row=1)
    Label(main_window, font=("Helvetica", 16), bg='gray100', text="Forks", width=7, borderwidth=2, relief="sunken").grid(column=0,row=2,sticky=E)
    Label(main_window, font=("Helvetica", 16), bg='gray100', text="Spoons", width=8, borderwidth=2, relief="sunken").grid(column=3,row=2,sticky=W)
    Label(main_window, font=("Helvetica", 16), bg='gray100', text="Paper Plates", width=11, borderwidth=2, relief="sunken").grid(column=0,row=4,sticky=E)
    Label(main_window, font=("Helvetica", 16), bg='gray100', text="Paper Cups", width=10, borderwidth=2, relief="sunken").grid(column=3,row=4,sticky=W)
    Label(main_window, font=("Helvetica", 16), bg='gray100', text="Party Hats", width=10, borderwidth=2, relief="sunken").grid(column=0,row=6,sticky=E)
    Label(main_window, font=("Helvetica", 16), bg='gray100', text="Ballons", width=7, borderwidth=2, relief="sunken").grid(column=3,row=6,sticky=W)
    Label(main_window, font=("Helvetica", 16), bg='gray100', text="Hired Date", width=10, borderwidth=2, relief="sunken").grid(column=0,row=8,pady=20)          
    Label(main_window, font=("Helvetica", 16), bg='gray100', text="Row number", width=11, borderwidth=2, relief="sunken").grid(column=4,row=9)

# create empty list for camp details and empty variable for entries in the list
counters = {'total_entries':0,'name_count':0}
all_details = []  

# the main window settings
main_window = Tk()
main_window.geometry('690x420')
main_window.resizable(width=False, height=False)
main_window.title('v2.41')

# main background settings 
main_bg = PhotoImage(file="main background.png")
Label(main_window, image=main_bg).place(relheight=1, relwidth=1)

# entry box and spinboxes
validate_name_cmd = main_window.register(validate_int_input)
name_entry = Entry(main_window, font=("Helvetica", 14), width=15, borderwidth=1, relief="solid")
name_entry.grid(column=1,row=0)
item_1_forks = Entry(main_window, font=("Helvetica", 16, "bold"), width=5, borderwidth=1, relief="solid", validate="key", validatecommand=(validate_name_cmd, "%S"))
item_1_forks.grid(column=1,row=2)
item_2_spoons = Entry(main_window, font=("Helvetica", 16, "bold"), width=5, borderwidth=1, relief="solid", validate="key", validatecommand=(validate_name_cmd, "%S"))
item_2_spoons.grid(column=4,row=2)
item_3_Paper_Plates = Entry(main_window, font=("Helvetica", 16, "bold"), width=5, borderwidth=1, relief="solid", validate="key", validatecommand=(validate_name_cmd, "%S"))
item_3_Paper_Plates.grid(column=1,row=4)
item_4_Paprt_Cups = Entry(main_window, font=("Helvetica", 16, "bold"), width=5, borderwidth=1, relief="solid", validate="key", validatecommand=(validate_name_cmd, "%S"))
item_4_Paprt_Cups.grid(column=4,row=4)
item_5_Party_hats = Entry(main_window, font=("Helvetica", 16, "bold"), width=5, borderwidth=1, relief="solid", validate="key", validatecommand=(validate_name_cmd, "%S"))
item_5_Party_hats.grid(column=1,row=6)
item_6_Paprt_Ballons = Entry(main_window, font=("Helvetica", 16, "bold"), width=5, borderwidth=1, relief="solid", validate="key", validatecommand=(validate_name_cmd, "%S"))
item_6_Paprt_Ballons.grid(column=4,row=6)
hire_date = Entry(main_window, font=("Helvetica", 16, "bold"), width=5, borderwidth=1, relief="solid", validate="key", validatecommand=(validate_name_cmd, "%S"))
hire_date.grid(column=1,row=8)
delete_item = Entry(main_window, font=("Helvetica", 16, "bold"), width=5, borderwidth=1, relief="solid", validate="key", validatecommand=(validate_name_cmd, "%S"))
delete_item .grid(column=4,row=10)  
#Start the GUI it up
setup_buttons()
main_window.mainloop()
