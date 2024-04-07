from tkinter import *
from threading import *
import re
import time

class Window:

    def __init__(self):

        self.root = Tk()
        self.root.geometry("1200x600")
        self.anchor = 8
        self.count = self.anchor
        self.bool = False
        self.mouse_pressed = False
        #self.hold_bg = "#000000"
        self.label_list = []
        #self.replace_list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        self.myLabel1 = Label(self.root, text="Hello World").grid(row=0,column=0)
        self.myLabel2 = Label(self.root, text="My Name is Luke").grid(row=1,column=0)
        self.b1 = Button(self.root, text="Small").grid(row=2, column=0)
        self.b2 = Button(self.root, text="Big w/ color", padx=50, pady=50, fg="red",bg="blue").grid(row=3,column=0)
        self.b3 = Button(self.root, text="Disabled", state=DISABLED).grid(row=4,column=0)
        #self.b4 = Button(self.root, text="Hold", bg=self.hold_bg, fg="#FFFFFF")
        #self.b4.grid(row=5,column=0)
        #self.b4.bind('<Button-1>', self.hold_thread)
        #self.b4.bind('<ButtonRelease-1>', self.release)
        self.root.bind('<Return>', self.get_text)
        self.b5 = Button(self.root, text="OFF", command=self.toggle, bg="red")
        self.b5.grid(row=5,column=0)
        self.e1 = Entry(self.root, width=30, borderwidth=3)
        self.e1.grid(row=6, column=0)
        self.exit = Button(self.root, text="Exit", command=self.root.quit)
        self.exit.grid(row=self.anchor-1,column=0)
        #self.b5 = Button(self.root, text="Print", command=self.get_text)
        #self.b5.grid(row=7, column=0)

    def toggle(self):

        if self.count == self.anchor + 5:

            for i in self.label_list:

                i.destroy()
                
            self.label_list = []
            self.count = self.anchor

        if self.bool:

            self.b5.configure(text="OFF",bg="red")
            self.label_list.append(Label(self.root, text="Pressed",font=("Arial",16)))
            self.label_list[-1].grid(row=self.count,column=0)                      
            self.bool = False
            self.count += 1

        else:

            self.b5.configure(text="ON",bg="green")
            self.label_list.append(Label(self.root, text="Pressed",font=("Arial",16)))
            self.label_list[-1].grid(row=self.count,column=0)
            self.bool = True
            self.count += 1

    def get_text(self, entry):

        if self.count == self.anchor + 5:

            for i in self.label_list:

                i.destroy()
                
            self.label_list = []
            self.count = self.anchor

        self.label_list.append(Label(self.root, text=self.e1.get(),font=("Arial",16)))
        self.label_list[-1].grid(row=self.count,column=0)                      
        self.bool = False
        self.count += 1
        self.e1.delete(0, END)
        #self.e1.instert(0, number)
        

"""
    def hold_thread(self, event):

        t1 = Thread(target=self.hold)
        t1.start()

    def hold(self):

        self.mouse_pressed = True
        while self.mouse_pressed:
            for i in range(len(self.replace_list)):
                time.sleep(1)
                if i == 15:
                    self.hold_bg = "#000000"
                    self.b4.configure(bg = self.hold_bg)
                else:
                    self.hold_bg = re.sub(self.replace_list[i], self.replace_list[i+1], self.hold_bg)
                    print(self.hold_bg)
                    print(i)
                    self.b4.configure(bg = self.hold_bg)
                
    def release(self, event):

        self.mouse_pressed = False
"""
    

if __name__ == "__main__":

    win1 = Window()

    win1.root.mainloop()
    
#myLabel1.grid(row=0,column=0)
#myLabel2.grid(row=1,column=0)

#myLabel.pack()

