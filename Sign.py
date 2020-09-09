"""Developed by Prasie James"""
import os
import tkinter as tk
from tkinter import *
from tkinter.messagebox import *

def register():
    global username
    global password
    global username_entry
    global password_entry
    global screen
    #root = Tk()
    screen = Toplevel(root)
    screen.title("signup")
    screen.geometry ("400x350")
    screen.resizable = (False, False)
    
    username = StringVar()
    password = StringVar()

    Label(screen, text = "ENTER YOUR DATA" , bg = "red", font = ("algerian", 19)).pack()
    Label(screen, text ="").pack()

    username_label = Label(screen, text = "*Username:*", bg = "yellow", font = ("helvetica", 16))
    username_label.pack()

    username_entry = Entry(screen, textvariable = username)
    username_entry.pack()

    password_label = Label(screen, text = "*Password:*", bg = "yellow", font = ("helvetica", 16))
    password_label.pack()

    password_entry = Entry(screen, textvariable = password, show = '*')
    password_entry.pack()

    Label(screen, text = "").pack()

    Button(screen,  text = "SIGN UP", width = 10, height = 1, bg = "red", command = register_user).pack()
    
def valid(name, password):return True if 4<=len (name and password)<=25 and (name, password)[0].isalpha() and (name, password)[-1] != '_' and all ([i.islower()or i.isupper() or i.isdigit() or i == '_' for i in (name, password)]) else False
 
def register_user():
    username_data = username.get()
    password_data = password.get()
    if os.path.isfile(username_data + ".txt") is False:
        #valid(username_data, password_data)
        if valid(username_data, password_data) is True:
            file = open(username_data + ".txt", "w+")
            file.write(username_data + "\n" + password_data)
            file.close()
    
            username_entry.delete(0, END)
            password_entry.delete(0, END)

            showinfo("SUCCESS!!", "Your sign up was successsful! :)")
            screen.destroy()
  
            #menu.run()
        else:
            showinfo("Sign up failed", "the username or/and password you entered is not valid\n our standard username and password must ...\n 1. It must be between 4 and 25 characters\n 2. it must start with a letter\n 3. it can only contain letters, numbers and the underscore character\n 4. it cannot end with an underscore ")
    else:
        showinfo("Sign up failed", "The username or/and password you entered already exists, please try another")
def log():
    global name
    global Password
    global username_Label
    global username_input
    global password_Label
    global password_input
    
    log = Toplevel(root)
    log.title("LOG IN")
    log.geometry ("400x350")
    log.resizable = (False, False)
    
    name = StringVar()
    Password = StringVar()

    Label(log, text = "ENTER YOUR DATA" , bg = "red", font = ("algerian", 19)).pack()
    Label(log, text ="").pack()

    username_Label = Label(log, text = "*Username:*", bg = "yellow", font = ("helvetica", 13))
    username_Label.pack()

    username_input = Entry(log, textvariable = name)
    username_input.pack()

    password_Label = Label(log, text = "*Password:*", bg = "yellow", font = ("helvetica", 13))
    password_Label.pack()

    password_input = Entry(log, textvariable = Password, show = '*')
    password_input.pack()

    Label(log, text = "").pack()

    Button(log,  text = "LOG IN", width = 10, height = 1, bg = "red", command = login).pack()


def login():
    #Label(log, text = "please wait verifying...", font = ("Helvetica", 15)).pack()
    name_data = name.get()
    Password_data = Password.get()
    username_input.delete(0, END)
    password_input.delete(0, END)
    try:
        with open(name_data + '.txt', 'r') as file:
        #if os.path.exists(name_data) is True:
            showinfo("SUCCESS", f"Welcome back {name_data} get ready for your adventure")
    except:
        showinfo("Error 404:", "An Error occured: INCORRECT or INVALID username or/and password\nyour data's where not found, try again but\n if you don't successfully login, a file has been corrupted ")


def account():
    global root
    global account
    root = Tk()
    root.geometry('600x500')
    root.title('login or signup')
    root.resizable = (False, False)
    
    Label(text = "LOGIN OR CREATE AN ACCOUNT", bg = "red", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text = "").pack()

    Button(text = "Login", height = "4", width = "60", command = log).pack()
    Label(text = "").pack()
    Button(text = "Sign up", height = "4", width = "60", command = register).pack()

if __name__=='__main__':
    account()
