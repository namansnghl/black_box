import tkinter as tk


########################### MENU ###############################

class Menu(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, bg=controller.bgColor[0], highlightbackground="black", highlightthickness=1)
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
                            padx=16, pady=7, cursor="hand2")
        dispBut = tk.Button(self,
                            bg=controller.bgColor[1], fg='#343434',
                            text='DISPLAY', font=controller.but,
                            command=lambda: controller.show_frame("display"),
                            activebackground=controller.bgColor[2],
                            relief=tk.SOLID,
                            borderwidth=0,
                            padx=16, pady=7, cursor="hand2")
        backupBut = tk.Button(self,
                              bg=controller.bgColor[1], fg='#343434',
                              text='BACKUP DATA', font=controller.but,
                              command=lambda: controller.show_frame("backup"),
                              activebackground=controller.bgColor[2],
                              relief=tk.SOLID,
                              borderwidth=0,
                              padx=16, pady=7, cursor="hand2")
        changePswdBut = tk.Button(self,
                                  bg=controller.bgColor[1], fg='#343434',
                                  text='CHANGE PASSCODES', font=controller.but,
                                  command=lambda: controller.show_frame("chPswd"),
                                  activebackground=controller.bgColor[2],
                                  relief=tk.SOLID,
                                  borderwidth=0,
                                  padx=16, pady=7, cursor="hand2")
        resetBut = tk.Button(self,
                             bg=controller.bgColor[1], fg='#343434',
                             text='RESET DATA', font=controller.but,
                             command=lambda: print("RESET"),
                             activebackground=controller.bgColor[2],
                             relief=tk.SOLID,
                             borderwidth=0,
                             padx=16, pady=7, cursor="hand2")

        head.place(relx=0.5, rely=0.1, y=50, anchor=tk.CENTER)
        feedBut.place(relx=0.5, rely=0.3, y=30, anchor=tk.CENTER, width=190, height=36)
        dispBut.place(relx=0.5, rely=0.3, y=100, anchor=tk.CENTER, width=190, height=36)
        backupBut.place(relx=0.5, rely=0.3, y=170, anchor=tk.CENTER, width=190, height=36)
        changePswdBut.place(relx=0.5, rely=0.3, y=240, anchor=tk.CENTER, width=190, height=36)
        resetBut.place(relx=0.5, rely=0.3, y=310, anchor=tk.CENTER, width=190, height=36)

        note1.place(relx=0.4, rely=0.3, y=30, x=-40, anchor=tk.CENTER)
        note2.place(relx=0.4, rely=0.3, y=100, x=-40, anchor=tk.CENTER)
        note3.place(relx=0.4, rely=0.3, y=170, x=-40, anchor=tk.CENTER)
        note4.place(relx=0.4, rely=0.3, y=240, x=-40, anchor=tk.CENTER)
        note5.place(relx=0.4, rely=0.3, y=310, x=-40, anchor=tk.CENTER)

        controller.exitButton(self)

        # Color theme changing
        noteTheme = tk.Button(self,
                              bg=controller.bgColor[1], fg='#343434',
                              text='SWITCH THEME', font=controller.notes,
                              command=controller.themeChanger,
                              activebackground=controller.bgColor[2],
                              relief=tk.RAISED,
                              borderwidth=0,
                              padx=10, pady=5, cursor="hand2")
        noteTheme.place(relx=0.07, rely=0.07, anchor=tk.CENTER)

        ### KEY BINDS ###

    def binds(self):
        self.controller.bind('1', lambda x: self.controller.show_frame("newEncrypt"))
        self.controller.bind('2', lambda x: self.controller.show_frame("display"))
        self.controller.bind('3', lambda x: self.controller.show_frame("backup"))
        self.controller.bind('4', lambda x: self.controller.show_frame("chPswd"))
        self.controller.bind('5', lambda x: print("RESET"))
