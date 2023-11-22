import customtkinter as tk
import datetime
import mysql.connector

db = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'cliniclick_db')
mycur = db.cursor()

def palogin_verify_test(username_verify, password_verify):
    global results, results2, patient_lastname
    paun_verify = username_verify
    papw_verify = password_verify
    sql = 'select * from patienttbl where binary patient_username = %s and patient_password = %s'
    mycur.execute(sql,[(paun_verify),(papw_verify)])
    results = mycur.fetchall()
    
    mycur.execute('select patient_lastname from patienttbl where patient_username = ' + '\'' + paun_verify + '\'')
    results2 = mycur.fetchall()
    
    for row  in results2 :
        patient_lastname = ''.join(row)

def login_failed():
    global failed_main
    failed_main = tk.CTkToplevel()
    failed_main.attributes('-topmost', True)
    failed_main.title('Invalid')
    failed_main.geometry('200x100')
    
    error_label = tk.CTkLabel(failed_main, text = 'Invalid credentials')
    ok_button = tk.CTkButton(failed_main, text = 'Ok', command = fail_destroy)
    
    error_label.pack()
    ok_button.pack()
    
def fail_destroy():
    failed_main.destroy()
    
def register_user(lastname, firstname, middlename, birthdate, sex, contact, address, username, password):
    global lastname_info, firstname_info, middlename_info, birthdate_info, sex_info, contact_info, address_info, username_info, password_info, dateObject, new_date
    lastname_info = lastname
    firstname_info = firstname
    middlename_info = middlename
    birthdate_info = birthdate
    sex_info = sex
    contact_info = contact
    address_info = address
    username_info = username
    password_info = password
     
    new_date = str(birthdate_info)
    date_format = '%Y-%m-%d'
       
    try:
        dateObject = datetime.datetime.strptime(new_date, date_format)
        print(new_date)
        registration_validation()
        
    except ValueError:
        print('Error')   
        login_failed()
    
def registration_validation():
    if lastname_info == '' or firstname_info == '' or middlename_info == '' or birthdate_info == '' or sex_info == '' or contact_info == '' or username_info == '' or password_info == '':
        login_failed()

    else:
        mycur.execute('select patient_code from patienttbl')
        mycur.fetchall()
        
        conv_rowcount = str(mycur.rowcount + 1)
        value = '00000000' 
        conv_rowcount = str(conv_rowcount)
        temp = len(conv_rowcount)
        modified_value = value[:-temp]
        db.commit()
        sql = 'insert into patienttbl values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        t = ('PA' + modified_value + conv_rowcount, lastname_info, firstname_info, middlename_info, birthdate_info, sex_info, contact_info, address_info, username_info, password_info)
        mycur.execute(sql, t)
        db.commit()
        print("Register Success")   
    
def dropdownobj():
    global specialist_options, specialist_size, doctor_options, doctor_size, choice
    
    mycur.execute('select distinct doctor_specialty from doctortbl order by doctor_specialty')
    specialist_size = mycur.fetchall()
    
    specialist_options = [row[0] for row in specialist_size]
    
    mycur.execute('select doctor_lastname, doctor_firstname from doctortbl order by doctor_lastname asc')
    doctor_size = mycur.fetchall()
    print(specialist_options)
    
    doctor_options = []
   
    for row in doctor_size :
        last_name = row[0].strip()
        first_name = row[1].strip()
        full_name = last_name + ', ' + first_name
        
        doctor_options.append(full_name)

def drop_down_update(choice):
    global config_doctor_options
    config_doctor_options = []
        
    mycur.execute('select doctor_lastname, doctor_firstname from doctortbl where doctor_specialty = ' + '\'' + choice + '\'' +  ' order by doctor_lastname asc')
    doctor_size = mycur.fetchall()
    
    for row in doctor_size :
        last_name = row[0].strip()
        first_name = row[1].strip()
        full_name = last_name + ', ' + first_name
        
        config_doctor_options.append(full_name)
        print(config_doctor_options)

    
        
