import tkinter as tk


########################### ADDING NEW RECORD PAGE ###############################

class newEncrypt(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, bg=controller.bgColor[0], highlightbackground="black", highlightthickness=1)
        self.controller = controller

        head = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="FEED NEW",
                        font=controller.heading)
        keyword = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="KEYWORD",
                           font=controller.subHead)
        string = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="STRING",
                          font=controller.subHead)
        keywordEntry = tk.Entry(self, bg=controller.bgColor[1], font=controller.fields)
        stringEntry = tk.Text(self, bg=controller.bgColor[1], font=controller.fields)
        note1 = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1],
                         text="Relax! Your strings \nare Encrypted before\nstoring.\n\nBut it is important to\nremember your Keyword\nto search & display\nthe String.",
                         font=controller.notesBig, justify=tk.LEFT,
                         bd=0.5, relief=tk.SOLID,
                         padx=20, pady=20, )
        note2 = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1],
                         text="Keywords are recommended to be a single word.",
                         font=controller.notes, justify=tk.LEFT, relief=tk.SOLID, bd=0)
        saveBut = tk.Button(self,
                            bg=controller.bgColor[1], fg='#343434',
                            text='SAVE', font=controller.but,
                            activebackground=controller.bgColor[2], command=lambda: print("save click"),
                            relief=tk.SOLID,
                            borderwidth=0,
                            padx=16, pady=7, cursor="hand2")
        entNote = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="(enter)",
                           font=controller.notes)

        head.place(relx=0.5, rely=0.1, y=50, anchor=tk.CENTER)
        keyword.place(relx=0.3, rely=0.3, y=30, x=-20, anchor=tk.CENTER)
        string.place(relx=0.3, rely=0.5, y=-30, x=-20, anchor=tk.CENTER)
        keywordEntry.place(relx=0.4, rely=0.3, y=30, x=140, anchor=tk.CENTER, width=350, height=30)
        stringEntry.place(relx=0.4, rely=0.5, y=45, x=140, anchor=tk.CENTER, width=350, height=200)
        note1.place(relx=0.15, rely=0.85, anchor=tk.CENTER)
        note2.place(relx=0.4, rely=0.3, x=100, anchor=tk.CENTER)
        saveBut.place(relx=0.7, rely=0.8, y=65, x=-40, anchor=tk.CENTER)
        entNote.place(relx=0.6, rely=0.8, y=65, x=-30, anchor=tk.CENTER)
        controller.homeButton(self)
        controller.exitButton(self)
        self.focusHere = keywordEntry

    ### KEY BINDS & FOCUS###
    def binds(self):
        self.focusHere.focus_set()
        self.controller.bind('<Return>', lambda x: print("save click"))
