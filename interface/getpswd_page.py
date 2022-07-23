import tkinter as tk


########################### DISPLAY PAGE ###############################

class display(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, bg=controller.bgColor[0], highlightbackground="black", highlightthickness=1)
        self.controller = controller
        head = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="DISPLAY",
                        font=controller.heading)
        keyword = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="KEYWORD HERE",
                           font=controller.subHead)
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
