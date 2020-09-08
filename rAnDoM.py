import random
from tkinter import *
import datetime


class Countdown(Frame):
    """count down for typing practise"""
    def __init__(self, master):
        super().__init__(master)
        self.initialize()
        self.time()
        self.seconds_left = 0
        self._timer_on = False
        
        #self.start()

    def time(self): self.label.pack()

    def initialize(self):
        self.label = Label(self, text="00:00:00", bg = 'green', font = ("Helvetica", 15))
        self.begin = self.start

    def countdown(self):
        '''Update label based on the time left.'''
        self.label['text'] = self.convert_remainder()

        if self.seconds_left:
            self.seconds_left -= 1
            self._timer_on = self.after(1000, self.countdown)
        else:
            self._timer_on = False

    def start(self, button, entry):
        '''Start counting down'''
        self.rand = random.randint(30, 300)
        self.seconds_left = int(self.rand)   # seconds
        self.countdown()
        entry.config(state=NORMAL)
        button.config(command=lambda: [self.stop(button, entry)], text='PAUSE')
    
    def stop(self, button, entry):
        '''Stops after schedule from executing.'''
        if self._timer_on:
            self.after_cancel(self._timer_on)
            entry.config(state=DISABLED)
            button.config(command=lambda: [self.continue_(button, entry)], text='CONTINUE')
            self._timer_on = False

    def convert_remainder(self): return datetime.timedelta(seconds=self.seconds_left)

    def continue_(self, button, entry):
        self.countdown()
        entry.config(state=NORMAL)
        button.config(command=lambda: [self.stop(button, entry)], text='PAUSE')

def charcount(*args):
    output.config(state=NORMAL)
    output.delete(0.0, "end")
    words = entry.get(0.0, "end")
    c = len(words.replace(' ', ''))-1
    output.insert(INSERT, c)
    output.config(state=DISABLED)

def count():
    charcount()
    entry.bind('<KeyRelease>', charcount)


def run():
    global output
    global entry
    root = Tk()
    root.title("TSA 1.0")
    root.geometry('500x600')
    root.resizable (False, False)

    label = Label(root, text = "TYPE YOUR BEST, goodluck").pack()

    entry = Text(root, width = 450, height = 10, font = ("Helvetica", 16), wrap = "word", state=DISABLED)
    entry.focus_set()   
    entry.pack()
    output = Text(root, width = 10, height = 2, font = ('Helvetica', 16), wrap = 'word', state=DISABLED)
    output.pack()
    countdown = Countdown(root)
    countdown.pack()
    button = Button(root, text = "START")
    button.pack()
    button.config(command = lambda:[countdown.start(button, entry), count()])
    root.mainloop()
    
if __name__=='__main__':
    run()
