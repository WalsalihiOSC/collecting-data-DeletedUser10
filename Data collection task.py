from tkinter import*
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
        
        l1 = Label(self.frame2, text = "First name:", bg = "white")
        l1.grid(row=0, column=0,padx=10, pady=5, sticky=W)
        l2 = Label(self.frame2, text = "Age:",bg = "White")
        l2.grid(row=1, column=0, pady = 10, padx=10, sticky=W)
        l3 = Label(self.frame2, text = "Do you have a mobile phone?", bg = "White")
        l3.grid(row=2, column=0, padx=10, pady=10)

        e1 = Entry(self.frame2)
        e1.grid(row=0, column=1, sticky=W)
        e2 = Entry(self.frame2)
        e2.grid(row = 1, column=1, sticky=W)

        self.radio_var = StringVar()
        self.radio_var.set(self.data.radios)

        for radio in self.data.radios:
            Radiobutton(self.frame2, text = radio, 
                        variable=self.radio_var, 
                        value=radio, bg = "White",
                        command=self.phone).grid(column=1, sticky=W)

        button2 = Button(self.frame2, text = "Enter Data", bg = "white")
        button2.grid(row=5, padx=30)

    
    def phone(self):
        pass

    def frame_3(self):
        self.frame2.grid_forget()
        
        self.data_label.configure(text = "Displaying Person Data")
        frame3 = Frame(self.main_frame,highlightbackground="black", highlightthickness=1, 
                                    height=200, 
                                    width=300, bg = "White")
        frame3.grid(row=1, column=0)
        frame3.grid_propagate(0)

        name_labl = Label(frame3, text = "First name: ", bg = "white")
        name_labl.grid(row=0, column=0, padx=20,pady=4)
        user_name = Label(frame3, text = "Not entered yet", bg = "White")
        user_name.grid(row = 0, column=1, padx=30)

        age_labl = Label(frame3, text = "Age: ", bg = "white")
        age_labl.grid(row=1, column=0, padx=20,pady=4)
        user_age = Label(frame3, text = "Not entered yet", bg = "White")
        user_age.grid(row = 1, column=1, padx=30)




class UI:
    def __init__(self):
        self.radios = ["No","Yes"]
        self.name = []
        self.age= []
    
    def has_phone(self):
        pass
    

def main():
    root = Tk()
    root.resizable(0,0)
    Interface(root)
    root.mainloop()

main()