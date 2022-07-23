import tkinter as tk


########################### LOGIN PAGE ###############################

class loginPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, bg=controller.bgColor[0], highlightbackground="black", highlightthickness=1)
        self.controller = controller
        head = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="BLACK BOX",
                        font=controller.heading)
        passcode1 = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="PASSCODE 1",
                             font=controller.subHead)
        passcode2 = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="PASSCODE 2",
                             font=controller.subHead)
        passcodeEntry1 = tk.Entry(self, show='*', bg=controller.bgColor[1], font=controller.fields)
        passcodeEntry2 = tk.Entry(self, show='*', bg=controller.bgColor[1], font=controller.fields)
        note = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1],
                        text="Enter Passcode in\ncorrect order", font=controller.notesBig,
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
                          padx=16, pady=7, cursor="hand2")
        entNote = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="(enter)",
                           font=controller.notes)

        head.place(relx=0.5, rely=0.1, y=50, anchor=tk.CENTER)
        passcode1.place(relx=0.4, rely=0.3, y=30, x=-20, anchor=tk.CENTER)
        passcodeEntry1.place(relx=0.5, rely=0.3, y=30, x=80, anchor=tk.CENTER, width=210, height=30)
        passcode2.place(relx=0.4, rely=0.3, y=100, x=-20, anchor=tk.CENTER)
        passcodeEntry2.place(relx=0.5, rely=0.3, y=100, x=80, anchor=tk.CENTER, width=210, height=30)
        login.place(relx=0.5, rely=0.5, y=70, anchor=tk.CENTER)

        note.place(relx=0.15, rely=0.87, anchor=tk.CENTER)
        entNote.place(rely=0.5, relx=0.5, y=70, x=-70, anchor=tk.CENTER)
        self.focusHere = passcodeEntry1
        controller.exitButton(self)

        ### KEY BINDS & FOCUS###

    def binds(self):
        self.focusHere.focus_set()
        self.controller.bind('<Return>', lambda x: self.controller.show_frame("Menu"))
