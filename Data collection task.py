from tkinter import*
from tkinter import messagebox
"""Data collection task"""
class Interface:
    def __init__(self, parent):
        self.data = UI()
        self.main_frame = Frame(parent)
        self.main_frame.grid()
        
        self.frame1 = Frame(self.main_frame, highlightbackground="black", 
                                    highlightthickness=1, 
                                    height=60, 
                                    width=300, bg = "Pink")

        self.frame1.grid(column=0, row = 0, padx=2, pady=2)
        self.frame1.grid_propagate(0)
        
        self.data_label = Label(self.frame1, text = "Collecting Person Data", bg="pink")
        self.data_label.grid(row=0, column=0, padx=10)
        ghost_Label = Label(self.frame1, text = "               ", bg = "Pink").grid(column=2, row=0)

        self.button1 = Button(self.frame1, text = "Show All", command=self.frame_3)
        self.button1.grid(column=3, row=0, pady=10,sticky=NSEW)

        self.frame2 = Frame(self.main_frame, highlightbackground="black", highlightthickness=1, 
                                    height=200, 
                                    width=300, bg = "White")
        self.frame2.grid(row=1, column=0)
        self.frame2.grid_propagate(0)
        
        self.l1 = Label(self.frame2, text = "First name:", bg = "white")
        self.l1.grid(row=0, column=0,padx=10, pady=5, sticky=W)
        self.l2 = Label(self.frame2, text = "Age:",bg = "White")
        self.l2.grid(row=1, column=0, pady = 10, padx=10, sticky=W)
        self.l3 = Label(self.frame2, text = "Do you have a mobile phone?", bg = "White")
        self.l3.grid(row=2, column=0, padx=10, pady=10)

        self.e1 = Entry(self.frame2)
        self.e1.grid(row=0, column=1, sticky=W)
        self.e2 = Entry(self.frame2)
        self.e2.grid(row = 1, column=1, sticky=W)

        self.radio_var = StringVar()
        self.radio_var.set(self.data.radios)

        for radio in self.data.radios:
            Radiobutton(self.frame2, text = radio, 
                        variable=self.radio_var, 
                        value=radio, bg = "White").grid(column=1, sticky=W)

        self.button2 = Button(self.frame2, text = "Enter Data", bg = "white", command=self.check)
        self.button2.grid(row=5, padx=30)


    """Creates frame 3"""
    def frame_3(self):
        self.frame2.grid_forget()
        
        self.data_label.configure(text = "Displaying Person Data")
        self.frame3 = Frame(self.main_frame,highlightbackground="black", highlightthickness=1, 
                                    height=200, 
                                    width=300, bg = "White")
        self.frame3.grid(row=1, column=0)
        self.frame3.grid_propagate(0)

        self.name_labl = Label(self.frame3, text = "First name: ", bg = "white")
        self.name_labl.grid(row=0, column=0, padx=20,pady=4)
        self.user_name = Label(self.frame3, text = "Not entered yet", bg = "White")
        self.user_name.grid(row = 0, column=1, padx=30)

        self.age_labl = Label(self.frame3, text = "Age: ", bg = "white")
        self.age_labl.grid(row=1, column=0, padx=20,pady=4)
        self.user_age = Label(self.frame3, text = "Not entered yet", bg = "White")
        self.user_age.grid(row = 1, column=1, padx=30)

        self.final_labl = Label(self.frame3, text = "", bg = "white")
        self.final_labl.grid(row=2, column=1)

        self.back_bttn = Button(self.frame3, text = "Add person ", bg = "White", command=self.back)
        self.back_bttn.grid(row=3, column=0)

        self.display_data()
    
    def back(self):
        self.frame3.grid_forget()
        self.frame2.grid()

    def enter_data(self):
        self.data.name.append(self.e1.get())
        self.data.age.append(self.e2.get())
        
        "Radio_button"
        if self.data.has_phone(self.radio_var.get()):
            self.data.phones.append("doesn't have a mobile phone")
        else:
            self.data.phones.append("has a mobile phone")

        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.radio_var.set(None)

    def check(self):
        self.err_check = 0
        
        if len(self.e1.get())== 0:
            messagebox.showerror("name","name is required")
            self.err_check = 1
        elif len(self.e2.get()) == 0:
            messagebox.showerror("age", "age is required")
        else:
            if self.err_check == 0:
                self.enter_data()

    def display_data(self):
        self.user_name.configure(text = self.data.name,bg = "white")
        self.user_age.configure(text = self.data.age,bg = "white")
        self.final_labl.configure(text = f"{str(*self.data.name)} {str(*self.data.phones)}")


"""Ui class"""
class UI:
    def __init__(self):
        self.radios = ["No","Yes"]
        self.name = []
        self.age= []
        self.phones = []
    
    def has_phone(self, answer):
       return answer == self.radios[0]
    

def main():
    root = Tk()
    root.resizable(0,0)
    Interface(root)
    root.mainloop()

main()