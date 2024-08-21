# Andrew Wong
# 14/8/24
# version 3.4 (Final)
# The purpose of this program is to record user data for a party hire store

# import tkinter and needed components 
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import ttk
import random

# set up the validate_int_input function
def validate_int_input(char):
    return char.isdigit()

# set up the quit function
def quit():
    main_window.destroy()
    
# set up the print details function
def print_details ():
    # setting up the details window 
    details_window = Tk()
    details_window.geometry('1200x270')
    details_window.title('All details')
    details_window.configure(bg='lightblue')
    # set the name_count variable to 0
    name_count = 0
    # create the column headings
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Row number   ").grid(column=0,row=13)
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Name   ").grid(column=1,row=13)
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Receipt number   ").grid(column=2,row=13)
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Forks   ").grid(column=3,row=13)
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Spoons   ").grid(column=4,row=13)
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Paper plates   ").grid(column=5,row=13)
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Paper cups   ").grid(column=6,row=13)
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Party hats   ").grid(column=7,row=13)
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Balloons   ").grid(column=8,row=13)
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Hired date   ").grid(column=9,row=13)

    # add each item in the list into its own row
    while name_count < counters['total_entries'] :
        Label(details_window, font=("Helvetica", 15), bg='lightblue', text=name_count).grid(column=0,row=name_count+15) 
        Label(details_window, font=("Helvetica", 15), bg='lightblue', text=(all_details[name_count][0])).grid(column=1,row=name_count+15)
        Label(details_window, font=("Helvetica", 15), bg='lightblue', text=(all_details[name_count][1])).grid(column=2,row=name_count+15)
        Label(details_window, font=("Helvetica", 15), bg='lightblue', text=(all_details[name_count][2])).grid(column=3,row=name_count+15)
        Label(details_window, font=("Helvetica", 15), bg='lightblue', text=(all_details[name_count][3])).grid(column=4,row=name_count+15)
        Label(details_window, font=("Helvetica", 15), bg='lightblue', text=(all_details[name_count][4])).grid(column=5,row=name_count+15)
        Label(details_window, font=("Helvetica", 15), bg='lightblue', text=(all_details[name_count][5])).grid(column=6,row=name_count+15)
        Label(details_window, font=("Helvetica", 15), bg='lightblue', text=(all_details[name_count][6])).grid(column=7,row=name_count+15)
        Label(details_window, font=("Helvetica", 15), bg='lightblue', text=(all_details[name_count][7])).grid(column=8,row=name_count+15)
        Label(details_window, font=("Helvetica", 15), bg='lightblue', text=(all_details[name_count][8])).grid(column=9,row=name_count+15)
        # add 1 to the name_count variable, then set the name_count counter to be the same value as the name_count
        name_count +=  1
        counters['name_count'] = name_count

# set up the check_inputs function 
def check_inputs ():
    # set the check variables to 0
    all_check = 0
    input_check = 0

    # check all inputs, if everything is 0 and the name entrybox is empty then send error message 
    if int(item_1_Forks.get()) == 0 and int(item_2_Spoons.get()) == 0 and int(item_3_Paper_plates.get()) == 0 and int(item_4_Paper_cups.get()) == 0 and int(item_5_Party_hats.get()) == 0 and int(item_6_Balloons.get()) == 0 and len(name_entry.get()) == 0 and int(hire_date.get()) == 0:
        messagebox.showerror(' Error', 'Please enter your name, the amount of items you want and how long you want to hire them !')
        all_check = 1

    while True:
        # if everything is 0 and the name entrybox is empty then don't check anything else
        if all_check == 1:
            break
        # check the hire date, if it is empty then send error message
        if len(name_entry.get()) == 0:
            messagebox.showerror('  Error  ', 'Please enter your full name !')
            input_check = 1
            break
        # check the name entry, if it is not only alphabets or empty then send error message
        if (name_entry.get().replace(' ','').isalpha()):
            pass
        else:
            messagebox.showerror('  Error  ', 'Please only enter alphabets for your name !')
            input_check = 1
            break
        # check the item boxes' entry, if all of them is empty send error message
        if int(item_1_Forks.get()) == 0 and int(item_2_Spoons.get()) == 0 and int(item_3_Paper_plates.get()) == 0 and int(item_4_Paper_cups.get()) == 0 and int(item_5_Party_hats.get()) == 0 and int(item_6_Balloons.get()) == 0:
            messagebox.showerror('  Error  ', 'Please pick the amount of items you want !')
            input_check = 1
            break
        # check the hire date, if it is 0 then send error message
        if int(hire_date.get()) == 0:
            messagebox.showerror('  Error  ', 'Please enter how many days you want to hire the items !')
            input_check = 1
            break
        # if there is no errors then input_check will equal to 0 and jump to append_name, otherwise nothing will happen
        if input_check == 0:
            append_name()
            break
        
# set up the append_name function
def append_name ():
    # Take the entries' value/text and put it into a variable
    receipt_number = random.randint(1000,9999)
    user_name = name_entry.get()
    receipt = str(receipt_number)
    Forks = str(item_1_Forks.get())
    Spoons = str(item_2_Spoons.get())
    Plates = str(item_3_Paper_plates.get())
    Cups = str(item_4_Paper_cups.get())
    Hats = str(item_5_Party_hats.get())
    Balloons = str(item_6_Balloons.get())
    hire_time = str(hire_date.get())
    # Save the user date to a text file
    file = 'user data.txt'
    with open(file, 'a') as f:
        f.write("\n")
        f.write(" - User details")
        f.write("\n")
        f.write("Name: ")
        f.write(user_name)
        f.write("\n")
        f.write("Receipt number: ")
        f.write(receipt)
        f.write("\n")
        f.write("Days of hire: ")
        f.write(hire_time)
        f.write("\n")
        f.write(" - Items amount")
        f.write("\n")
        f.write("Forks: ")
        f.write(Forks)
        f.write("  ")
        f.write("Spoons: ")
        f.write(Spoons)
        f.write("  ")
        f.write("Plates: ")
        f.write(Plates)
        f.write("  ")
        f.write("Cups: ")
        f.write(Cups)
        f.write("  ")
        f.write("Hats: ")
        f.write(Hats)
        f.write("  ")
        f.write("Balloons: ")
        f.write(Balloons)
        f.write("  ")
        f.write("\n")
        f.close()
    messagebox.showinfo("Showinfo", "Data Saved")
    # append each item to its own area of the list
    all_details.append([user_name, receipt_number, Forks, Spoons, Plates, Cups, Hats, Balloons,hire_time])
    # clear all entries
    name_entry.delete(0,'end')
    item_1_Forks.set(' 0 ')
    item_2_Spoons.set(' 0 ')
    item_3_Paper_plates.set(' 0 ')
    item_4_Paper_cups.set(' 0 ')
    item_5_Party_hats.set(' 0 ')
    item_6_Balloons.set(' 0 ')
    hire_date.set(' 0 ')
    delete_item.delete(0,'end')
    # row number goes up by 1 and show it on the main window
    counters['total_entries'] += 1
    Label(main_window, font=("Helvetica", 19, "bold"), bg='gray100', text=counters['total_entries'], width=4, borderwidth=2, relief="sunken").grid(column=1,row=1)

# set up delete_row function 
def delete_row ():
    try:
        # put the delete box's number into a variable 
        row_to_delete = int(delete_item.get())
        # if there are no stored data, then sent a error message
        if counters['total_entries'] == 0:
            raise ValueError('There are no details!')
        # if the input is not a no row number, then sent a error message
        if row_to_delete >= counters['total_entries'] or row_to_delete < 0:
            raise ValueError('Invalid row number!')
        # delete the row related to the row number
        del all_details[row_to_delete]
        counters['total_entries'] -= 1
        print_details()
        # reprint the row number, because one row was deleted
        Label(main_window, font=("Helvetica", 19, "bold"), bg='gray100', text=counters['total_entries'], width=4, borderwidth=2, relief="sunken").grid(column=1, row=1)
        # clear the entry box
        delete_item.delete(0,'end') 
    # the delete box error message
    except ValueError as e:
        messagebox.showerror('Error', ' That is not a row number ! ')
    
# set up the setup_buttons function
def setup_buttons():
    # set up all buttons and labels on the main window
    Button(main_window, font=("Helvetica", 16, "bold"), image=delete_icon, command=delete_row, width=100, bg="brown1").grid(column=4,row=11) 
    Button(main_window, font=("Helvetica", 16, "bold"), text="Quit", command=quit, width=5, fg="white", bg="red").grid(column=7,row=0,pady=5,sticky=E)
    Button(main_window, font=("Helvetica", 16, "bold"), text="Submit Details",borderwidth=2, bg="yellow", command=check_inputs).grid(column=1,row=10)
    Button(main_window, font=("Helvetica", 16, "bold"), bg='gray100', text="Print Details", command=print_details, width=10).grid(column=0,row=12,padx=3, pady=3, sticky=W)
    Label(main_window, font=("Helvetica", 16), bg='gray100', text="Full Name", width=9, borderwidth=2, relief="sunken").grid(column=0,row=0,padx=6,sticky=E)
    Label(main_window, font=("Helvetica", 16), bg='gray100', text="Row Number", width=13, borderwidth=2, relief="sunken").grid(column=0,row=1,sticky=E)
    Label(main_window, font=("Helvetica", 19, "bold"), bg='gray100', text=counters['total_entries'], width=4, borderwidth=2, relief="sunken").grid(column=1,row=1)
    Label(main_window, font=("Helvetica", 16), bg='gray100', text="Forks", width=7, borderwidth=2, relief="sunken").grid(column=0,row=2,sticky=E)
    Label(main_window, font=("Helvetica", 16), bg='gray100', text="Spoons", width=8, borderwidth=2, relief="sunken").grid(column=3,row=2,sticky=W)
    Label(main_window, font=("Helvetica", 16), bg='gray100', text="Paper Plates", width=11, borderwidth=2, relief="sunken").grid(column=0,row=4,sticky=E)
    Label(main_window, font=("Helvetica", 16), bg='gray100', text="Paper Cups", width=10, borderwidth=2, relief="sunken").grid(column=3,row=4,sticky=W)
    Label(main_window, font=("Helvetica", 16), bg='gray100', text="Party Hats", width=10, borderwidth=2, relief="sunken").grid(column=0,row=6,sticky=E)
    Label(main_window, font=("Helvetica", 16), bg='gray100', text="Balloons", width=7, borderwidth=2, relief="sunken").grid(column=3,row=6,sticky=W)
    Label(main_window, font=("Helvetica", 16), bg='gray100', text="Hired Date", width=10, borderwidth=2, relief="sunken").grid(column=0,row=8,pady=20)          
    Label(main_window, font=("Helvetica", 16), bg='gray100', text="Row number", width=11, borderwidth=2, relief="sunken").grid(column=4,row=9)


# set up the main window 
main_window = Tk()
main_window.geometry('690x420')
main_window.resizable(width=False, height=False)
main_window.title('The Party Shop')

# import all images that program will use and set up the main window's background
main_icon = PhotoImage(file='main icon.png')
main_bg = PhotoImage(file="main background.png")
delete_icon = PhotoImage(file="delete icon.png")
main_window.iconphoto(False, main_icon)
Label(main_window, image=main_bg).place(relheight=1, relwidth=1)

# setup variables
amount = list(range(0, 501))
validate_name_cmd = main_window.register(validate_int_input)
a = StringVar()
b = StringVar()
c = StringVar()
d = StringVar()
e = StringVar()
f = StringVar()
n = StringVar()

# create counters and a empty list to store details 
counters = {'total_entries':0,'name_count':0}
all_details = []  
item_ammount = amount

# set up entry boxes and a combobox
name_entry = Entry(main_window, font=("Helvetica", 14), width=15, borderwidth=1, relief="solid")
name_entry.grid(column=1,row=0)
item_1_Forks = ttk.Combobox(main_window, font=("Helvetica", 16, "bold"), width=3, textvariable = a, state = "readonly")
item_1_Forks['values'] = item_ammount
item_1_Forks.grid(column=1,row=2)
item_1_Forks.current(0)
item_2_Spoons = ttk.Combobox(main_window, font=("Helvetica", 16, "bold"), width=3, textvariable = b, state = "readonly")
item_2_Spoons['values'] = item_ammount
item_2_Spoons.grid(column=4,row=2)
item_2_Spoons.current(0)
item_3_Paper_plates = ttk.Combobox(main_window, font=("Helvetica", 16, "bold"), width=3, textvariable = c, state = "readonly")
item_3_Paper_plates['values'] = item_ammount
item_3_Paper_plates.grid(column=1,row=4)
item_3_Paper_plates.current(0)
item_4_Paper_cups = ttk.Combobox(main_window, font=("Helvetica", 16, "bold"), width=3, textvariable = d, state = "readonly")
item_4_Paper_cups['values'] = item_ammount
item_4_Paper_cups.grid(column=4,row=4)
item_4_Paper_cups.current(0)
item_5_Party_hats = ttk.Combobox(main_window, font=("Helvetica", 16, "bold"), width=3, textvariable = e, state = "readonly")
item_5_Party_hats['values'] = item_ammount
item_5_Party_hats.grid(column=1,row=6)
item_5_Party_hats.current(0)
item_6_Balloons = ttk.Combobox(main_window, font=("Helvetica", 16, "bold"), width=3, textvariable = f, state = "readonly")
item_6_Balloons['values'] = item_ammount
item_6_Balloons.grid(column=4,row=6)
item_6_Balloons.current(0)
hire_date = ttk.Combobox(main_window, font=("Helvetica", 18, "bold"), width=3, textvariable = n, state = "readonly")
hire_date['values'] = (' 0 ', ' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ', ' 10 ', ' 11 ', ' 12 ', ' 13 ', ' 14 ')
hire_date.grid(column=1,row=8) 
hire_date.current(0)
delete_item = Entry(main_window, font=("Helvetica", 16, "bold"), width=5, borderwidth=1, relief="solid", validate="key", validatecommand=(validate_name_cmd, "%S"))
delete_item .grid(column=4,row=10)  
# jump to the setup_buttons function
setup_buttons()
# loop the whole program 
main_window.mainloop()
