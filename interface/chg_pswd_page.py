import tkinter as tk


########################### CHANGE PASSWORD ###############################
class chPswd(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, bg=controller.bgColor[0], highlightbackground="black", highlightthickness=1)
        self.controller = controller
        head = tk.Label(self, bg=controller.bgColor[0], fg=controller.bgColor[1], text="CHANGE PASSCODES",
                        font=controller.heading)

        head.place(relx=0.5, rely=0.1, y=50, anchor=tk.CENTER)
        controller.homeButton(self)
        controller.exitButton(self)

    ### KEY BINDS ###
    def binds(self):
        pass
