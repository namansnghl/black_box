import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3

####### THEMES #######
purpleTheme = ['#6A4065', '#ebdce9', '#E3CAE0', 'purple']
blueTheme = ['#12576E', '#C4D5DF', '#B5CAD7', 'blue']
winWidth = 850
winHeight = 700

########################### WINDOW CONTROLLER ###############################

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        ####### FONTS #######
        self.heading = ("Terminal", 20, "bold")
        self.subHead = ("Terminal", 14, "bold")
        self.notes = ("Terminal", 8)
        self.notesBig = ("Terminal", 9)
        self.fields = ("Terminal", 10)
        self.but = ("Terminal", 11)
        self.butBig = ("Terminal", 13)

        with open("theme.txt", 'r') as th:
            color = th.readlines()
        if color[0] == 'purple':
            self.bgColor = purpleTheme
        else:
            self.bgColor = blueTheme

        ####### WINDOW SETTINGS #######
        ws = self.winfo_screenwidth()  # width of the screen
        hs = self.winfo_screenheight()  # height of the screen
        self.title("Black Box")
        self.geometry('%dx%d+%d+%d' % (winWidth, winHeight, (ws/2) - (winWidth/2), (hs/2) - (winHeight/2)))
        self.minsize(winWidth, winHeight)
        self.maxsize(winWidth+150, winHeight+200)

        self.homew = 90
        self.homeh = 45

        #images
        self.img = ImageTk.PhotoImage(Image.open(f'img/{self.bgColor[-1]}Home.png').resize((self.homew, self.homeh), Image.ANTIALIAS))
        self.blue = ImageTk.PhotoImage(
            Image.open(f'img/blueColor.png').resize((self.homew, self.homeh), Image.ANTIALIAS))
        self.purp = ImageTk.PhotoImage(
            Image.open(f'img/purpleColor.png').resize((self.homew, self.homeh), Image.ANTIALIAS))

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        ####### FRAME STACK #######
        self.frames = {}
        for F in (loginPage, Menu, newEncrypt, display, backup, chPswd):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("loginPage")
        self.bind('<Escape>', lambda x: self.exitConfirmation())

    def exitConfirmation(self):
        response=messagebox.askyesno("Exit", "Do you want to Exit?")
        if response:
            self.destroy()

    def show_frame(self, page_name):
        '''RAISES FRAME TO TOP'''
        frame = self.frames[page_name]
        frame.tkraise()
        frame.focus_set()
        self.unbinder()
        frame.binds()

    def unbinder(self):
        self.unbind('<Return>')
        self.unbind('1')
        self.unbind('2')
        self.unbind('3')
        self.unbind('4')
        self.unbind('5')

    def themeChanger(self):
        response = messagebox.askyesno("Changing Theme", "The app will restart. Do you still want to change theme?")
        if response:
            with open("theme.txt", 'w+') as th:
                if self.bgColor[-1] == 'blue':
                    th.write('purple')
                else:
                    th.write('blue')
            refresh(self)

    def exitButton(self, frame):
        '''Common Exit Button for all screens'''
        note = tk.Label(self, bg=self.bgColor[0], fg=self.bgColor[1], text="(esc)", font=self.notes)
        exitBut = tk.Button(frame,
                            bg=self.bgColor[1], fg='#343434',
                            text='EXIT', font=self.but,
                            command=self.exitConfirmation,
                            activebackground=self.bgColor[2],
                            relief=tk.SOLID,
                            borderwidth=0,
                            padx=16, pady=7,
                            cursor="hand2")
        exitBut.place(relx=0.8, rely=0.8, y=65,x=25, anchor=tk.CENTER)
        note.place(relx=0.8, rely=0.8, y=65,x=-40, anchor=tk.CENTER)

    def homeButton(self, frame):

        buttn = tk.Button(frame, image=self.img,
                          bg=self.bgColor[0], command=lambda: self.show_frame('Menu'),
                          activebackground=self.bgColor[0],
                          relief=tk.SOLID,
                          borderwidth=0,
                          padx=0, pady=0,cursor="hand2")
        buttn.place(relx=0.1,rely=0.1,y=30,width=self.homew,height=self.homeh)


########################### LOGIN PAGE ###############################

class loginPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent,bg=controller.bgColor[0], highlightbackground="black", highlightthickness=1)
        self.controller = controller
        head = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="BLACK BOX", font=controller.heading)
        passcode1 = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="PASSCODE 1", font=controller.subHead)
        passcode2 = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="PASSCODE 2", font=controller.subHead)
        passcodeEntry1 = tk.Entry(self, show='*',bg=controller.bgColor[1], font=controller.fields)
        passcodeEntry2 = tk.Entry(self, show='*',bg=controller.bgColor[1], font=controller.fields)
        note = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="Enter Passcode in\ncorrect order", font=controller.notesBig,
                        justify=tk.LEFT,
                        bd=0.5, relief=tk.SOLID,
                        padx=15, pady=15)
        login = tk.Button(self,
                       bg=controller.bgColor[1], fg='#343434',
                       text='LOGIN', font=controller.but,
                       command=lambda: controller.show_frame("Menu"),
                       activebackground=controller.bgColor[2],
                       relief=tk.SOLID,
                       borderwidth=0,
                       padx=16, pady=7,cursor="hand2")
        entNote = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="(enter)", font=controller.notes)

        head.place(relx=0.5, rely=0.1, y=50, anchor=tk.CENTER)
        passcode1.place(relx=0.4, rely=0.3, y=30,x=-20, anchor=tk.CENTER)
        passcodeEntry1.place(relx=0.5, rely=0.3, y=30, x=80, anchor=tk.CENTER, width=210, height=30)
        passcode2.place(relx=0.4, rely=0.3, y=100,x=-20, anchor=tk.CENTER)
        passcodeEntry2.place(relx=0.5, rely=0.3, y=100, x=80, anchor=tk.CENTER, width=210, height=30)
        login.place(relx=0.5, rely=0.5, y=70, anchor=tk.CENTER)

        note.place(relx=0.15, rely=0.87, anchor=tk.CENTER)
        entNote.place(rely=0.5,relx=0.5,y=70,x=-70, anchor=tk.CENTER)
        self.focusHere=passcodeEntry1
        controller.exitButton(self)


        ### KEY BINDS & FOCUS###
    def binds(self):
        self.focusHere.focus_set()
        self.controller.bind('<Return>',lambda x: self.controller.show_frame("Menu"))


########################### MENU ###############################

class Menu(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent,bg=controller.bgColor[0], highlightbackground="black", highlightthickness=1)
        self.controller = controller
        head = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="MENU", font=controller.heading)
        note1 = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="1", font=controller.notesBig)
        note2 = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="2", font=controller.notesBig)
        note3 = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="3", font=controller.notesBig)
        note4 = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="4", font=controller.notesBig)
        note5 = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="5", font=controller.notesBig)
        feedBut = tk.Button(self,
                       bg=controller.bgColor[1], fg='#343434',
                       text='ENCRYPT NEW', font=controller.but,
                       command=lambda: controller.show_frame("newEncrypt"),
                       activebackground=controller.bgColor[2],
                       relief=tk.SOLID,
                       borderwidth=0,
                       padx=16, pady=7,cursor="hand2")
        dispBut = tk.Button(self,
                            bg=controller.bgColor[1], fg='#343434',
                            text='DISPLAY', font=controller.but,
                            command=lambda: controller.show_frame("display"),
                            activebackground=controller.bgColor[2],
                            relief=tk.SOLID,
                            borderwidth=0,
                            padx=16, pady=7,cursor="hand2")
        backupBut = tk.Button(self,
                            bg=controller.bgColor[1], fg='#343434',
                            text='BACKUP DATA', font=controller.but,
                            command=lambda: controller.show_frame("backup"),
                            activebackground=controller.bgColor[2],
                            relief=tk.SOLID,
                            borderwidth=0,
                            padx=16, pady=7,cursor="hand2")
        changePswdBut = tk.Button(self,
                            bg=controller.bgColor[1], fg='#343434',
                            text='CHANGE PASSCODES', font=controller.but,
                            command=lambda: controller.show_frame("chPswd"),
                            activebackground=controller.bgColor[2],
                            relief=tk.SOLID,
                            borderwidth=0,
                            padx=16, pady=7,cursor="hand2")
        resetBut = tk.Button(self,
                          bg=controller.bgColor[1], fg='#343434',
                          text='RESET DATA', font=controller.but,
                          command=lambda: print("RESET"),
                          activebackground=controller.bgColor[2],
                          relief=tk.SOLID,
                          borderwidth=0,
                          padx=16, pady=7, cursor="hand2")

        head.place(relx=0.5, rely=0.1, y=50, anchor=tk.CENTER)
        feedBut.place(relx=0.5, rely=0.3, y=30, anchor=tk.CENTER, width=190,height=36)
        dispBut.place(relx=0.5, rely=0.3,y=100, anchor=tk.CENTER, width=190,height=36)
        backupBut.place(relx=0.5, rely=0.3,y=170, anchor=tk.CENTER, width=190,height=36)
        changePswdBut.place(relx=0.5, rely=0.3,y=240, anchor=tk.CENTER, width=190,height=36)
        resetBut.place(relx=0.5, rely=0.3,y=310, anchor=tk.CENTER, width=190,height=36)

        note1.place(relx=0.4, rely=0.3, y=30,x=-40, anchor=tk.CENTER)
        note2.place(relx=0.4, rely=0.3, y=100,x=-40, anchor=tk.CENTER)
        note3.place(relx=0.4, rely=0.3, y=170,x=-40, anchor=tk.CENTER)
        note4.place(relx=0.4, rely=0.3, y=240,x=-40, anchor=tk.CENTER)
        note5.place(relx=0.4, rely=0.3,y=310,x=-40, anchor=tk.CENTER)

        controller.exitButton(self)

        #Color theme changing
        noteTheme = tk.Button(self,
                          bg=controller.bgColor[1], fg='#343434',
                          text='SWITCH THEME', font=controller.notes,
                          command=controller.themeChanger,
                          activebackground=controller.bgColor[2],
                          relief=tk.RAISED,
                          borderwidth=0,
                          padx=10, pady=5, cursor="hand2")
        noteTheme.place(relx=0.07,rely=0.07,anchor=tk.CENTER)

        ### KEY BINDS ###
    def binds(self):
        self.controller.bind('1', lambda x: self.controller.show_frame("newEncrypt"))
        self.controller.bind('2', lambda x: self.controller.show_frame("display"))
        self.controller.bind('3', lambda x: self.controller.show_frame("backup"))
        self.controller.bind('4', lambda x: self.controller.show_frame("chPswd"))
        self.controller.bind('5', lambda x: print("RESET"))


########################### ADDING NEW RECORD PAGE ###############################

class newEncrypt(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, bg=controller.bgColor[0], highlightbackground="black", highlightthickness=1)
        self.controller = controller

        head = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="FEED NEW", font=controller.heading)
        keyword = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="KEYWORD", font=controller.subHead)
        string = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="STRING", font=controller.subHead)
        keywordEntry = tk.Entry(self, bg=controller.bgColor[1], font=controller.fields)
        stringEntry = tk.Text(self, bg=controller.bgColor[1], font=controller.fields)
        note1 = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1],
                         text="Relax! Your strings \nare Encrypted before\nstoring.\n\nBut it is important to\nremember your Keyword\nto search & display\nthe String.",
                         font=controller.notesBig, justify=tk.LEFT,
                         bd=0.5,relief=tk.SOLID,
                         padx=20, pady=20,)
        note2 = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1],
                         text="Keywords are recommended to be a single word.",
                         font=controller.notes, justify=tk.LEFT,relief=tk.SOLID,bd=0)
        saveBut = tk.Button(self,
                          bg=controller.bgColor[1], fg='#343434',
                          text='SAVE', font=controller.but,
                          activebackground=controller.bgColor[2],command=lambda: print("save click"),
                          relief=tk.SOLID,
                          borderwidth=0,
                          padx=16, pady=7,cursor="hand2")
        entNote = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="(enter)", font=controller.notes)

        head.place(relx=0.5, rely=0.1, y=50, anchor=tk.CENTER)
        keyword.place(relx=0.3, rely=0.3, y=30, x=-20, anchor=tk.CENTER)
        string.place(relx=0.3, rely=0.5,y=-30, x=-20, anchor=tk.CENTER)
        keywordEntry.place(relx=0.4, rely=0.3, y=30, x=140, anchor=tk.CENTER, width=350, height=30)
        stringEntry.place(relx=0.4, rely=0.5, y=45, x=140, anchor=tk.CENTER, width=350, height=200)
        note1.place(relx=0.15, rely=0.85, anchor=tk.CENTER)
        note2.place(relx=0.4, rely=0.3, x=100, anchor=tk.CENTER)
        saveBut.place(relx=0.7, rely=0.8, y=65,x=-40, anchor=tk.CENTER)
        entNote.place(relx=0.6, rely=0.8, y=65,x=-30, anchor=tk.CENTER)
        controller.homeButton(self)
        controller.exitButton(self)
        self.focusHere=keywordEntry


    ### KEY BINDS & FOCUS###
    def binds(self):
        self.focusHere.focus_set()
        self.controller.bind('<Return>', lambda x: print("save click"))

########################### DISPLAY PAGE ###############################

class display(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, bg=controller.bgColor[0], highlightbackground="black", highlightthickness=1)
        self.controller = controller
        head = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="DISPLAY", font=controller.heading)
        keyword = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="KEYWORD HERE", font=controller.subHead)
        keywordEntry = tk.Entry(self, bg=controller.bgColor[1], font=controller.fields)
        searchButt = tk.Button(self,
                            bg=controller.bgColor[1], fg='#343434',
                            text='Look Up', font=controller.but,
                            activebackground=controller.bgColor[2], command=lambda: print("Search in DB"),
                            relief=tk.SOLID,
                            borderwidth=0,
                            padx=16, pady=7, cursor="hand2")

        searchButt.place(relx=0.6, rely=0.3, y=30, x=140, anchor=tk.CENTER)
        keywordEntry.place(relx=0.4, rely=0.3, y=30, x=100, anchor=tk.CENTER, width=280, height=30)
        keyword.place(relx=0.3, rely=0.3, y=30, x=-40, anchor=tk.CENTER)
        head.place(relx=0.5, rely=0.1, y=50, anchor=tk.CENTER)
        controller.homeButton(self)
        controller.exitButton(self)
        self.focusHere = keywordEntry

    ### KEY BINDS & FOCUS###
    def binds(self):
        self.focusHere.focus_set()
        self.controller.bind('<Return>', lambda x: print("Search DB"))

########################### BACKUP PAGE ###############################

class backup(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, bg=controller.bgColor[0], highlightbackground="black", highlightthickness=1)
        self.controller = controller
        head = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="BACKUP", font=controller.heading)
        expBut = tk.Button(self,
                            bg=controller.bgColor[1], fg='#343434',
                            text='EXPORT', font=controller.but,
                            command=lambda: print("Export"),
                            activebackground=controller.bgColor[2],
                            relief=tk.SOLID,
                            borderwidth=0,
                            padx=16, pady=7, cursor="hand2")
        impBut = tk.Button(self,
                            bg=controller.bgColor[1], fg='#343434',
                            text='IMPORT', font=controller.but,
                            command=lambda: print("Import"),
                            activebackground=controller.bgColor[2],
                            relief=tk.SOLID,
                            borderwidth=0,
                            padx=16, pady=7, cursor="hand2")
        note1 = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="1", font=controller.notesBig)
        note2 = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="2", font=controller.notesBig)
        note3 = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="Exports will be in \nEncrytion Format\n\nImport file must be the\nfile generated by\nthis software",
                         font=controller.notesBig,
                        justify=tk.LEFT,
                        bd=0.5, relief=tk.SOLID,
                        padx=15, pady=15)

        head.place(relx=0.5, rely=0.1, y=50, anchor=tk.CENTER)
        expBut.place(relx=0.5, rely=0.3, y=80, anchor=tk.CENTER, width=190, height=36)
        impBut.place(relx=0.5, rely=0.3, y=180, anchor=tk.CENTER, width=190, height=36)
        note1.place(relx=0.4, rely=0.3, y=80,x=-30, anchor=tk.CENTER)
        note2.place(relx=0.4, rely=0.3, y=180,x=-30, anchor=tk.CENTER)
        note3.place(relx=0.15, rely=0.87, anchor=tk.CENTER)
        controller.homeButton(self)
        controller.exitButton(self)

    ### KEY BINDS ###
    def binds(self):
        self.controller.bind('1', lambda x: print("Import"))
        self.controller.bind('2', lambda x: print("Export"))

########################### CHANGE PASSWORD ###############################
class chPswd(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, bg=controller.bgColor[0], highlightbackground="black", highlightthickness=1)
        self.controller = controller
        head = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="CHANGE PASSCODES", font=controller.heading)

        head.place(relx=0.5, rely=0.1, y=50, anchor=tk.CENTER)
        controller.homeButton(self)
        controller.exitButton(self)

    ### KEY BINDS ###
    def binds(self):
        pass



########################### DATABASE ###############################
'''
class mydb:
    def __init__(self):
        self.conn = sqlite3.connect('black_box.db')
        self.c = self.conn.cursor()
        self.c.cursor("CREATE TABLE CODES()")

    def commitChanges(self):
        self.conn.commit()

    def closeConnection(self):
        self.conn.close()
'''
def start_gui():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    def refresh(root):
        root.destroy()
        start_gui()

    start_gui()

