"""Developed by Praise James"""
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import one, three, five, fifteen, thirty, hour, RaNdOm
import sign

sign.account()
root = Tk()
class MENU(tk.Button):
    
    def __init__(self, master, **kw):
        root.title("Type Speed Amplifier 1.0")
        root.geometry('600x500')
        root.resizable(False, False)
        root.configure(bg = "Green")
        #hover buttons
        tk.Button.__init__(self, master = master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
    
    def on_enter(self, e): self['background'] = self['activebackground']
    
    def on_leave(self, e): self['background'] = self.defaultBackground


def ShowAbout(): showinfo("TSA1.0", "This program is written by Praise James, solely for the purpose of coding practice\n it was done to improve typing speed for the users\nNOTE: this apk does not teach typing, in fact, it is not for total noobs in typing\n it is made intermediate typist soleley for improving typing speed and accuracy\n Not all the recources that are used in this programme was made by the devveloper\n in this accord the developer would like to give credit to 'emm... my friend that does graphics'  for the background\n images used herein :)")

def quitApp(): root.destroy()#exit

def One():one.run()

def Three():three.run()

def Five():five.run()

def Fifteen():fifteen.run()

def Thirty():thirty.run()

def Hour():hour.run()

def Random():RaNdOm.run()

#set background image
#filename = 'images/background.png'
canvas = tk.Canvas(root, width = 600, height = 500)
canvas.pack()
#tk_img = PhotoImage(file = filename)
#canvas.create_image(250, 150, image = tk_img)

#buttons with hover effects
btn0 = MENU(root, text = "Profile",width = 10, height = 0, font = ('helvetica', 15, 'bold', 'underline', 'italic'), bg = 'green', foreground = 'aliceblue', activebackground = 'gold',
            highlightbackground = "#bce8f1", highlightthickness = 0.5, relief = tk.SOLID, borderwidth = "2", command = None)
btn0win = canvas.create_window(470, 9, anchor = 'nw', window = btn0)


btn1 = MENU(root, text = "1min\n (bullet)",width = 10, height = 0, font = ('helvetica', 15, 'bold', 'underline', 'italic'), bg = 'green', foreground = 'aliceblue', activebackground = 'gold',
            highlightbackground = "#bce8f1", highlightthickness = 0.5, relief = tk.SOLID, borderwidth = "2", command = One)
btn1win = canvas.create_window(90, 51, anchor = 'nw', window = btn1)

btn2 = MENU(root, text = "3mins\n (bullet)",width = 10, height = 0, font = ('helvetica', 15, 'bold', 'underline', 'italic'), bg = 'green', foreground = 'aliceblue', activebackground = 'gold',
            highlightbackground = "#bce8f1", highlightthickness = 0.5, relief = tk.SOLID, borderwidth = "2", command = Three)
btn2win = canvas.create_window(250, 51, anchor = 'nw', window = btn2)

btn3 = MENU(root, text = "5mins\n (blitz)",width = 10, height = 0, font = ('helvetica', 15, 'bold', 'underline', 'italic'), bg = 'green', foreground = 'aliceblue', activebackground = 'gold',
            highlightbackground = "#bce8f1", highlightthickness = 0.5, relief = tk.SOLID, borderwidth = "2", command = Five)
btn3win = canvas.create_window(410, 51, anchor = 'nw', window = btn3)

btn4 = MENU(root, text = "15min\n (blitz)",width = 10, height = 0, font = ('helvetica', 15, 'bold', 'underline', 'italic'), bg = 'green', foreground = 'aliceblue', activebackground = 'gold',
            highlightbackground = "#bce8f1", highlightthickness = 0.5, relief = tk.SOLID, borderwidth = "2", command = Fifteen)
btn4win = canvas.create_window(90, 141, anchor = 'nw', window = btn4)

btn5 = MENU(root, text = "30min\n (rapid)",width = 10, height = 0, font = ('helvetica', 15, 'bold', 'underline', 'italic'), bg = 'green', foreground = 'aliceblue', activebackground = 'gold',
            highlightbackground = "#bce8f1", highlightthickness = 0.5, relief = tk.SOLID, borderwidth = "2", command = Thirty)
btn5win = canvas.create_window(250, 141, anchor = 'nw', window = btn5)

btn6 = MENU(root, text = "1hr\n (classic)",width = 10, height = 0, font = ('helvetica', 15, 'bold', 'underline', 'italic'), bg = 'green', foreground = 'aliceblue', activebackground = 'gold',
            highlightbackground = "#bce8f1", highlightthickness = 0.5, relief = tk.SOLID, borderwidth = "2", command = Hour)
btn6win = canvas.create_window(410, 141, anchor = 'nw', window = btn6)

btn7 = MENU(root, text = "TYPE GAME",width = 10, height = 0, font = ('helvetica', 15, 'bold', 'underline', 'italic'), bg = 'green', foreground = 'aliceblue', activebackground = 'gold',
            highlightbackground = "#bce8f1", highlightthickness = 0.5, relief = tk.SOLID, borderwidth = "2", command = None)
btn7win = canvas.create_window(90, 231, anchor = 'nw', window = btn7)

btn8 = MENU(root, text = "CHALLENGE\n (ONLINE)",width = 10, height = 0, font = ('helvetica', 15, 'bold', 'underline', 'italic'), bg = 'green', foreground = 'aliceblue', activebackground = 'gold',
            highlightbackground = "#bce8f1", highlightthickness = 0.5, relief = tk.SOLID, borderwidth = "2", command = None)
btn8win = canvas.create_window(250, 231, anchor = 'nw', window = btn8)

btn9 = MENU(root, text = "RANDOM#",width = 10, height = 0, font = ('helvetica', 15, 'bold', 'underline', 'italic'), bg = 'green', foreground = 'aliceblue', activebackground = 'gold',
            highlightbackground = "#bce8f1", highlightthickness = 0.5, relief = tk.SOLID, borderwidth = "2", command = Random)
btn9win = canvas.create_window(410, 231, anchor = 'nw', window = btn9)

btn10 = MENU(root, text = "CUSTOM PRACTISE",width = 35, height = 0, font = ('helvetica', 15, 'bold', 'underline', 'italic'), bg = 'green', foreground = 'aliceblue', activebackground = 'gold',
            highlightbackground = "#bce8f1", highlightthickness = 0.5, relief = tk.SOLID, borderwidth = "2", command = None)
btn10win = canvas.create_window(90, 361, anchor = 'nw', window = btn10)

btn11 = MENU(root, text = "ABOUT AND CREDITS",width = 35, height = 0, font = ('helvetica', 15, 'bold', 'underline', 'italic'), bg = 'green', foreground = 'aliceblue', activebackground = 'gold',
            highlightbackground = "#bce8f1", highlightthickness = 0.5, relief = tk.SOLID, borderwidth = "2", command = ShowAbout)
btn11win = canvas.create_window(90, 404, anchor = 'nw', window = btn11)

btn12 = MENU(root, text = "QUIT !",width = 35, height = 0, font = ('helvetica', 15, 'bold', 'underline', 'italic'), bg = 'green',foreground = 'aliceblue', activebackground = 'gold',
            highlightbackground = "#bce8f1", highlightthickness = 0.5, relief = tk.SOLID, borderwidth = "2", command = quitApp)
btn12win = canvas.create_window(90, 447, anchor = 'nw', window = btn12)

root.mainloop()
