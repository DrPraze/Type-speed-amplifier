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
        #self.rand = random.randint(30, 300)
        self.seconds_left = int(30)   # seconds
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
    show_text()
    entry.bind('<KeyRelease>', charcount)

def show_text(*args):
    show.config(state=NORMAL)
    text = ['the', 'cat', 'explosion', 'with', 'complexities', 'introvert', 'agonize', 'typing', 'extremely', 'unpleasant', 'surplus', 'sprint', 'pneumonoultramicroscopicsilicovolcanoconiosis', 'goodness', 'extraordinary', 'terrific', 'generation', 'artificial', 'intelligence', 'science', 'technology', 'spectacular', 'problem', 'solving', 'mathematical', 'physics', 'solution', 'out', 'of', 'chemistry']
    _text = random.sample(text, len(text))
    show.insert(INSERT, _text)
    show.config(state=DISABLED)

def run():
    global show
    global output
    global entry
    root = Tk()
    root.title("TSA 1.0/ 30secs bullet")
    root.geometry('600x700')
    root.resizable (False, False)

    label = Label(root, text = "You've got ONLY 30 seconds, goodluck", bg = 'green').pack()

    show = Text(root, width = 450, height = 10, font = ("Calibri", 16), wrap = "word", bg = 'white', foreground = 'black', state = DISABLED)
    show.pack()
    entry = Text(root, width = 450, height = 10, font = ("Helvetica", 16), wrap = "word", bg = 'white', foreground = 'black', state=DISABLED)
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
