from .chg_pswd_page import *
from .generate_backup_page import *
from .getpswd_page import *
from .index_page import *
from .login_page import *
from .pswdform_page import *
from PIL import Image, ImageTk
from tkinter import messagebox


def start_gui():
    app = App()
    app.mainloop()


def refresh_gui(root):
    root.destroy()
    start_gui()


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

        with open("./theme.txt", 'r') as th:
            color = th.readlines()
        if color[0] == 'purple':
            self.bgColor = purpleTheme
        else:
            self.bgColor = blueTheme

        ####### WINDOW SETTINGS #######
        ws = self.winfo_screenwidth()  # width of the screen
        hs = self.winfo_screenheight()  # height of the screen
        self.title("Black Box")
        self.geometry('%dx%d+%d+%d' % (winWidth, winHeight, (ws / 2) - (winWidth / 2), (hs / 2) - (winHeight / 2)))
        self.minsize(winWidth, winHeight)
        self.maxsize(winWidth + 150, winHeight + 200)

        self.homew = 90
        self.homeh = 45

        # images
        self.img = ImageTk.PhotoImage(
            Image.open(f'img/{self.bgColor[-1]}Home.png').resize((self.homew, self.homeh), Image.ANTIALIAS))
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
        response = messagebox.askyesno("Exit", "Do you want to Exit?")
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
            refresh_gui(self)

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
        exitBut.place(relx=0.8, rely=0.8, y=65, x=25, anchor=tk.CENTER)
        note.place(relx=0.8, rely=0.8, y=65, x=-40, anchor=tk.CENTER)

    def homeButton(self, frame):

        buttn = tk.Button(frame, image=self.img,
                          bg=self.bgColor[0], command=lambda: self.show_frame('Menu'),
                          activebackground=self.bgColor[0],
                          relief=tk.SOLID,
                          borderwidth=0,
                          padx=0, pady=0, cursor="hand2")
        buttn.place(relx=0.1, rely=0.1, y=30, width=self.homew, height=self.homeh)
