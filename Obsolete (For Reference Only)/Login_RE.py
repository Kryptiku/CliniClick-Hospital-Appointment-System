import tkinter as tk
from tkcalendar import *
import mysql.connector
from subprocess import call
import datetime
import os

os.system('cls')
db = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'cliniclick_db')
mycur = db.cursor()


def main_screen():
    global main
    main = tk.Tk()
    main.title('Cliniclick')
    main.geometry('525x200')
    welcome_label = tk.Label(main, text = 'Welcome to the Cliniclick Log-In Portal', font = 'calibri 24', bg = 'sky blue', fg = 'black', width = 500)
    welcome_label.pack()
    
    login_button = tk.Button(main, text = 'Log-In', bg = 'sky blue', font = 'bold', command = login)
    register_button = tk.Button(main, text = 'Register', bg = 'sky blue', font = 'bold', command = registration)
    
    footer_label = tk.Label(main, text = 'Developed By Cliniclick™')
    
    login_button.pack(pady = 15)
    register_button.pack()
    footer_label.pack(side = 'bottom', pady = 5)
    main.mainloop()

def login():
    for child in main.winfo_children():
        child.destroy()
    global username_verify, password_verify
    username_verify = tk.StringVar()
    password_verify = tk.StringVar()
    
    main.title('Log-in Portal')
    login_label = tk.Label(main, text = 'Log-In Portal', bg = 'sky blue', fg = 'black', font = 'bold', width = 300)
    login_label.pack()
    
    username_label = tk.Label(main, text = 'Username: ')
    username_entry = tk.Entry(main, textvariable = username_verify)
    
    password_label = tk.Label(main, text = 'Password: ')
    password_entry = tk.Entry(main, textvariable = password_verify, show = '*')
    
    login_button = tk.Button(main, text = 'Log-In', bg = 'sky blue', command = login_verify)
    
    username_label.pack(pady = 10)
    username_entry.pack()
    password_label.pack(pady = 10)
    password_entry.pack()
    login_button.pack(pady = 10)
    
def registration():
    global lastname
    global firstname
    global middlename
    global birthdate
    global sex 
    global contact
    global address
    global username
    global password
    global registration_main
    registration_main = tk.Toplevel(main)
    registration_main.title('Registration Portal')
    registration_main.geometry()
    
    lastname = tk.StringVar()
    firstname = tk.StringVar()
    middlename = tk.StringVar()
    birthdate = tk.StringVar()
    sex = tk.StringVar()
    contact = tk.StringVar()
    address = tk.StringVar()
    username = tk.StringVar()
    password = tk.StringVar()   
    
    title_label = tk.Label(registration_main, text = 'Register your account', bg = 'sky blue', fg = 'black', font = 'calibri', width = 35)
    title_label.grid(row = 0, columnspan = 3, pady = 10, sticky = 'n')

    label_lastname = tk.Label(registration_main, text = 'Last Name:')
    entry_lastname = tk.Entry(registration_main, textvariable = lastname)
    label_lastname.grid(row = 1, column = 0, sticky = 'e', pady = 5, padx = 5)
    entry_lastname.grid(row = 1, column = 1, pady  =5, padx = 5)

    label_firstname = tk.Label(registration_main, text = 'First Name:')
    entry_firstname = tk.Entry(registration_main, textvariable = firstname)
    label_firstname.grid(row = 2, column = 0, sticky = 'e', pady = 5, padx = 5)
    entry_firstname.grid(row = 2, column = 1, pady = 5, padx = 5)
    
    label_middlename = tk.Label(registration_main, text = 'Middle Name: ')
    entry_middlename = tk.Entry(registration_main, textvariable = middlename)
    label_middlename.grid(row = 3, column = 0, sticky = 'e', pady = 5, padx = 5)
    entry_middlename.grid(row = 3, column = 1, pady = 5, padx = 5)

    global entry_birthdate
    label_birthdate = tk.Label(registration_main, text = 'Birth Date: ')
    entry_birthdate = tk.Entry(registration_main, textvariable = birthdate)
    button_birthdate = tk.Button(registration_main, text = 'Select Date', bg = 'sky blue', command = date_picker)
    label_birthdate.grid(row = 4, column = 0, sticky = 'e', pady = 5, padx = 5)
    entry_birthdate.grid(row = 4, column = 1, pady = 5, padx = 5)
    button_birthdate.grid(row = 4, column = 2, sticky = 'w', padx = 5)

    label_sex = tk.Label(registration_main, text = 'Sex: ')
    entry_sex = tk.Entry(registration_main, textvariable = sex)
    label_sex.grid(row = 5, column = 0, sticky = 'e', pady = 5, padx = 5)
    entry_sex.grid(row = 5, column = 1, pady = 5, padx = 5)

    label_contact = tk.Label(registration_main, text = 'Contact Number: ')
    entry_contact = tk.Entry(registration_main, textvariable = contact)
    label_contact.grid(row = 6, column = 0, sticky = 'e', pady = 5, padx = 5)
    entry_contact.grid(row = 6, column = 1, pady = 5, padx = 5)

    label_address = tk.Label(registration_main, text='Address: ')
    entry_address = tk.Entry(registration_main, textvariable = address)
    label_address.grid(row = 7, column = 0, sticky = 'e', pady = 5, padx = 5)
    entry_address.grid(row = 7, column = 1, pady = 5, padx = 5)

    label_username = tk.Label(registration_main, text = 'Username: ')
    entry_username = tk.Entry(registration_main, textvariable = username)
    label_username.grid(row = 8, column = 0, sticky ='e', pady = 5, padx = 5)
    entry_username.grid(row = 8, column = 1, pady = 5, padx = 5)

    label_password = tk.Label(registration_main, text = 'Password: ')
    entry_password = tk.Entry(registration_main, textvariable = password, show = '*')
    label_password.grid(row = 9, column = 0, sticky = 'e', pady = 5, padx = 5)
    entry_password.grid(row = 9, column = 1, pady = 5, padx = 5)

    register_button = tk.Button(registration_main, text = 'Register', bg = 'sky blue', command = register_user)
    register_button.grid(row = 10, columnspan = 3, sticky = 's', pady = 10)

    registration_main.mainloop()
    
def login_verify():
    user_verify = username_verify.get()
    pass_verify = password_verify.get()
    sql = 'select * from patienttbl where binary patient_username = %s and patient_password = %s'
    mycur.execute(sql,[(user_verify),(pass_verify)])
    results = mycur.fetchall()
    if results:
        for i in results:
            logged_main()
            break
    else:
        login_failed()
        
def register_user():
    
    lastname_info = lastname.get()
    firstname_info = firstname.get()
    middlename_info = middlename.get()
    birthdate_info = birthdate.get()
    sex_info = sex.get()
    contact_info = contact.get()
    address_info = address.get()
    username_info = username.get()
    password_info = password.get()
    
    if lastname_info == '' or firstname_info == '' or middlename_info == '' or birthdate_info == '' or sex_info == '' or contact_info == '' or username_info == '' or password_info == '':
        incomplete_field_error()

    else:
        mycur.execute('select patient_code from patienttbl')
        mycur.fetchall()
        conv_rowcount = str(mycur.rowcount + 1)
        value = '00000000' 
        conv_rowcount = str(conv_rowcount)
        temp = len(conv_rowcount)
        modified_value = value[:-temp]
        db.commit()
        sql = 'insert into patienttbl values (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)'
        t = ('PA' + modified_value + conv_rowcount, lastname_info, firstname_info, middlename_info, birthdate_info, sex_info, contact_info, address_info, username_info, password_info)
        mycur.execute(sql, t)
        db.commit()
        register_success()

def logged_main():
    for child in main.winfo_children():
        child.destroy()
        
    new_user = str(username_verify.get())
    mycur.execute('select patient_lastname from patienttbl where patient_username = ' + '\'' + new_user + '\'')
    result = mycur.fetchall()
    
    for row  in result :
        patient_lastname = ''.join(row)
    
    main.title('Welcome')
    main.geometry('525x300')
    welcome_label = tk.Label(main, text = 'Welcome {} '.format(patient_lastname + '!'), fg = 'green', font = 'bold')
    appointment_button = tk.Button(main, text = 'Register Appointment', bg = 'sky blue', font = 'bold', command = appointment)
    history_button = tk.Button(main, text = 'View History', bg = 'sky blue', font = 'bold', command = history)
    prescription_button = tk.Button(main, text = 'View Prescrptions', bg = 'sky blue', font = 'bold')
    log_out_button = tk.Button(main, text = 'Log-Out', bg = 'grey', command = logged_destroy)
    
    welcome_label.pack(pady = 10)
    appointment_button.pack(pady = 10)
    history_button.pack(pady = 10)
    prescription_button.pack(pady = 10)
    log_out_button.pack(pady = 10)
    
    main.mainloop()
    
def login_failed():
    global failed_main
    failed_main = tk.Toplevel(main)
    failed_main.title('Invalid')
    failed_main.geometry('200x100')
    
    error_label = tk.Label(failed_main, text = 'Invalid credentials', fg = 'red', font = 'bold')
    ok_button = tk.Button(failed_main, text = 'Ok', bg = 'grey', command = fail_destroy)
    
    error_label.pack()
    ok_button.pack()

def incomplete_field_error():
    global error
    error = tk.Toplevel(main)
    error.title('Error')
    error.geometry('200x100')
    field_error_label = tk.Label(error, text = 'All fields are required', fg = 'red', font = 'bold')
    ok_button = tk.Button(error, text = 'Ok',bg = 'grey', command = error_destroy)
    
    field_error_label.pack()
    ok_button.pack()

def register_success():
    global registered
    registered = tk.Toplevel(registration_main)
    registered.title('Success')
    registered.geometry()
    successful_label = tk.Label(registered, text = 'Registration successful!', fg = 'green', font = 'bold', width = 40)
    ok_button = tk.Button(registered, text = 'Ok', bg = 'grey', command = registered_destroy)
    
    successful_label.pack()
    ok_button.pack()

def date_picker():
    global calendar, calendar_main
    calendar_main = tk.Toplevel(registration_main)
    calendar_main.title('Select Date')
    calendar_main.geometry()
    calendar = Calendar(calendar_main, selectmode = 'day',date_pattern = 'y-mm-dd')
    calendar.pack(pady = 5, padx = 10)

    calendar_button = tk.Button(calendar_main, text = 'Confirm', bg = 'sky blue', command = lambda: [birthdate_entry (calendar.get_date()), calendar_destroy()])
    calendar_button.pack(pady = 5)

def calendar_destroy():
    calendar_main.destroy()
        

def error_destroy():
    error.destroy()

def registered_destroy():
    registered.destroy()
    registration_main.destroy()
    
def logged_destroy():
    main.destroy()
    main_screen()

def  birthdate_entry(text):
    entry_birthdate.delete(0, tk.END)
    entry_birthdate.insert(0, text)
    return

def fail_destroy():
    failed_main.destroy()
    
def history():
    call(['python', 'Login\History.py'])
    
def appointment():
    for child in main.winfo_children():
        child.destroy()
    
    user = str(username_verify.get())
    mycur.execute('select patient_code from patienttbl where patient_username = ' + '\'' + user + '\'')
    result = mycur.fetchall()
    
    for row  in result :
        patient_code = ''.join(row)
        
    main.title('Appointment')
    main.geometry()
    
    register_label = tk.Label(main, text = 'Appointment Registration', bg = 'sky blue', fg = 'black', font = 'bold', width = 50)
    register_label.pack()
    
    patient_label = tk.Label(main, text = patient_code, bg = 'sky blue', fg = 'black', font = 'bold', width = 50)
    patient_label.pack()
    
    appointment_button = tk.Button(main, text = 'Enter', bg = 'sky blue', fg = 'black', command = time_validation)
    appointment_button.pack()
    
    global time, date
    time = tk.StringVar()
    
    label_time = tk.Label(main, text='Time: ')
    entry_time = tk.Entry(main, textvariable = time)
    
    label_time.pack()
    entry_time.pack()
    
    
    date = tk.StringVar()
    label_date = tk.Label(main, text='Date: ')
    entry_date = tk.Entry(main, textvariable = date)
    
    label_date.pack()
    entry_date.pack()
    
def time_validation():
    global timeObject, new_time, formatted_time

    new_time = str(time.get())
    formatted_time = new_time.upper()
    time_format = '%I:%M %p'
    
    try:
        timeObject = datetime.datetime.strptime(formatted_time, time_format)
        print(formatted_time)
    
    except ValueError:
        validation_fail()
        
def validation_fail():
    failed_main = tk.Toplevel(main)
    failed_main.title('Invalid Entry')
    failed_main.geometry()
    
    error_label = tk.Label(failed_main, text = 'Incorrect Time', fg = 'red', font = 'bold', width = 20)
    ok_button = tk.Button(failed_main, text = 'Ok', bg = 'grey', command = fail_destroy)
    
    error_label.pack()
    ok_button.pack()
    
main_screen()   