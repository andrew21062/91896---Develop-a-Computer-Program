# Andrew Wong
#08/8/24
# version 3.2

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
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Recipe number   ").grid(column=2,row=13)
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Forks   ").grid(column=3,row=13)
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Spoons   ").grid(column=4,row=13)
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Paper plates   ").grid(column=5,row=13)
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Paper cups   ").grid(column=6,row=13)
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Party hats   ").grid(column=7,row=13)
    Label(details_window, font=("Helvetica", 15, "bold"), bg='lightblue', text="Ballons   ").grid(column=8,row=13)
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
    # set the input_check variable to 0
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
    if len(item_1_Forks.get()) ==0 or len(item_2_Spoons.get()) ==0 or len(item_3_Paper_plates.get()) ==0 or len(item_4_Paper_cups.get()) ==0 or len(item_5_Party_hats.get()) ==0 or len(item_6_Ballons.get())== 0:
        messagebox.showerror('  Error  ', 'Please entre 0 if you do not need the item.')
        input_check = 1

    # check the item boxes' entry, if they are over 500 then send error message
    if int(item_1_Forks.get()) > 500 or int(item_2_Spoons.get()) > 500 or int(item_3_Paper_plates.get()) > 500 or int(item_4_Paper_cups.get()) > 500 or int(item_5_Party_hats.get()) > 500 or int(item_6_Ballons.get()) > 500:
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
        
# set up the append_name function
def append_name ():
    # Take the entries' value/text and put it into a variable
    recipe_number = random.randint(1000,9999)
    user_name = name_entry.get()
    recipe = str(recipe_number)
    Forks = str(item_1_Forks.get())
    Spoons = str(item_2_Spoons.get())
    Plates = str(item_3_Paper_plates.get())
    Cups = str(item_4_Paper_cups.get())
    Hats = str(item_5_Party_hats.get())
    Ballons = str(item_6_Ballons.get())
    hire_time = str(hire_date.get())
    # Save the user date to a text file
    file = 'user data.txt'
    with open(file, 'a') as f:
        f.write("\n")
        f.write("Name: ")
        f.write(user_name)
        f.write("\n")
        f.write("Recipe number: ")
        f.write(recipe)
        f.write("\n")
        f.write("Items amount: ")
        f.write(Forks)
        f.write("  ")
        f.write(Spoons)
        f.write("  ")
        f.write(Plates)
        f.write("  ")
        f.write(Cups)
        f.write("  ")
        f.write(Hats)
        f.write("  ")
        f.write(Ballons)
        f.write("  ")
        f.write("\n")
        f.write("Days of hire: ")
        f.write(hire_time)
        f.write("\n")
        f.close()
    messagebox.showinfo("Showinfo", "Data Saved")
    # append each item to its own area of the list
    all_details.append([user_name, recipe_number, Forks, Spoons, Plates, Cups, Hats, Ballons,hire_time])
    # clear the boxes
    name_entry.delete(0,'end')
    item_1_Forks.delete(0,'end')
    item_2_Spoons.delete(0,'end')
    item_3_Paper_plates.delete(0,'end')
    item_4_Paper_cups.delete(0,'end')
    item_5_Party_hats.delete(0,'end')
    item_6_Ballons.delete(0,'end')
    hire_date.delete(0,'end')
    # row number goes up by 1 and show it on the main window
    counters['total_entries'] += 1
    Label(main_window, font=("Helvetica", 19, "bold"), bg='gray100', text=counters['total_entries'], width=4, borderwidth=2, relief="sunken").grid(column=1,row=1)

# set up delete_row function
def delete_row ():
    # check if there are any entries, if no then sent a error message
    if counters['total_entries'] == 0:
        messagebox.showerror('  Error  ', 'There are not details !')
    else:
        # find which row is to be deleted and delete it
        del all_details[int(delete_item.get())]
        counters['total_entries'] -= 1
        name_count = counters['name_count']
        delete_item.delete(0,'end')
        # clear the row by covering it with space
        Label(main_window, font=("Helvetica", 16, "bold"), text="       ").grid(column=0,row=name_count+15) 
        Label(main_window, font=("Helvetica", 16, "bold"), text="       ").grid(column=1,row=name_count+14)
        Label(main_window, font=("Helvetica", 16, "bold"), text="       ").grid(column=2,row=name_count+14)
        Label(main_window, font=("Helvetica", 16, "bold"), text="       ").grid(column=3,row=name_count+14)
        Label(main_window, font=("Helvetica", 16, "bold"), text="       ").grid(column=4,row=name_count+14)
        Label(main_window, font=("Helvetica", 16, "bold"), text="       ").grid(column=5,row=name_count+14)
        Label(main_window, font=("Helvetica", 16, "bold"), text="       ").grid(column=6,row=name_count+14)
        Label(main_window, font=("Helvetica", 16, "bold"), text="       ").grid(column=7,row=name_count+14)
        # jump to the print_details function
        print_details()
    
# set up the setup_buttons function
def setup_buttons():
    # set up all buttons and labels on the main window
    Button(main_window, font=("Helvetica", 16, "bold"), image=delete_icon, command=delete_row, width=100, bg="brown1").grid(column=4,row=11) 
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

# create counters and a empty list to store details 
counters = {'total_entries':0,'name_count':0}
all_details = []  

# set up the main window 
main_window = Tk()
main_window.geometry('690x420')
main_window.resizable(width=False, height=False)
main_window.title('v3.2')

# import all images that programm will use and set up the main window's background
main_icon = PhotoImage(file='main icon.png')
main_bg = PhotoImage(file="main background.png")
delete_icon = PhotoImage(file="delete icon.png")
main_window.iconphoto(False, main_icon)
Label(main_window, image=main_bg).place(relheight=1, relwidth=1)

# setup other variables
validate_name_cmd = main_window.register(validate_int_input)
n = StringVar()

# set up entry boxes and a combobox
name_entry = Entry(main_window, font=("Helvetica", 14), width=15, borderwidth=1, relief="solid")
name_entry.grid(column=1,row=0)
item_1_Forks = Entry(main_window, font=("Helvetica", 16, "bold"), width=5, borderwidth=1, relief="solid", validate="key", validatecommand=(validate_name_cmd, "%S"))
item_1_Forks.grid(column=1,row=2)
item_2_Spoons = Entry(main_window, font=("Helvetica", 16, "bold"), width=5, borderwidth=1, relief="solid", validate="key", validatecommand=(validate_name_cmd, "%S"))
item_2_Spoons.grid(column=4,row=2)
item_3_Paper_plates = Entry(main_window, font=("Helvetica", 16, "bold"), width=5, borderwidth=1, relief="solid", validate="key", validatecommand=(validate_name_cmd, "%S"))
item_3_Paper_plates.grid(column=1,row=4)
item_4_Paper_cups = Entry(main_window, font=("Helvetica", 16, "bold"), width=5, borderwidth=1, relief="solid", validate="key", validatecommand=(validate_name_cmd, "%S"))
item_4_Paper_cups.grid(column=4,row=4)
item_5_Party_hats = Entry(main_window, font=("Helvetica", 16, "bold"), width=5, borderwidth=1, relief="solid", validate="key", validatecommand=(validate_name_cmd, "%S"))
item_5_Party_hats.grid(column=1,row=6)
item_6_Ballons = Entry(main_window, font=("Helvetica", 16, "bold"), width=5, borderwidth=1, relief="solid", validate="key", validatecommand=(validate_name_cmd, "%S"))
item_6_Ballons.grid(column=4,row=6)
hire_date = ttk.Combobox(main_window, font=("Helvetica", 18, "bold"), width=3, textvariable = n, state = "readonly")
hire_date['values'] = (' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ', ' 10 ', ' 11 ', ' 12 ', '13 ', ' 14 ')
hire_date.grid(column=1,row=8)
hire_date.current(0) 
delete_item = Entry(main_window, font=("Helvetica", 16, "bold"), width=5, borderwidth=1, relief="solid", validate="key", validatecommand=(validate_name_cmd, "%S"))
delete_item .grid(column=4,row=10)  
# jump to the setup_buttons function
setup_buttons()
# loop the whole programm 
main_window.mainloop()
