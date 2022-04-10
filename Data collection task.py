from tkinter import*
"""Data collection task"""
class Interface:
    def __init__(self, parent):
        self.data = UI()
        main_frame = Frame(parent)
        main_frame.grid()
        
        frame1 = Frame(main_frame, highlightbackground="black", 
                                    highlightthickness=1, 
                                    height=60, 
                                    width=300, bg = "Pink")

        frame1.grid(column=0, row = 0, padx=2, pady=2)
        frame1.grid_propagate(0)
        
        data_label = Label(frame1, text = "Collecting Person Data", bg="pink")
        data_label.grid(row=0, column=0, padx=10)
        ghost_Label = Label(frame1, text = "               ", bg = "Pink").grid(column=2, row=0)

        button1 = Button(frame1, text = "Show All")
        button1.grid(column=3, row=0, pady=10,sticky=NSEW)

        frame2 = Frame(main_frame, highlightbackground="black", highlightthickness=1, 
                                    height=200, 
                                    width=300, bg = "White")
        frame2.grid(row=1, column=0)
        frame2.grid_propagate(0)
        
        l1 = Label(frame2, text = "First name:", bg = "white")
        l1.grid(row=0, column=0,padx=10, pady=5, sticky=W)
        l2 = Label(frame2, text = "Age:",bg = "White")
        l2.grid(row=1, column=0, pady = 10, padx=10, sticky=W)
        l3 = Label(frame2, text = "Do you have a mobile phone?", bg = "White")
        l3.grid(row=2, column=0, padx=10, pady=10)

        e1 = Entry(frame2)
        e1.grid(row=0, column=1, sticky=W)
        e2 = Entry(frame2)
        e2.grid(row = 1, column=1, sticky=W)

        self.radio_var = StringVar()
        self.radio_var.set(self.data.radios)

        for radio in self.data.radios:
            Radiobutton(frame2, text = radio, 
                        variable=self.radio_var, 
                        value=radio, bg = "White",
                        command=self.phone).grid(column=1, sticky=W)

        button2 = Button(frame2, text = "Enter Data", bg = "white")
        button2.grid(row=5, padx=30)

    
    def phone(self):
        pass


class UI:
    def __init__(self):
        self.radios = ["No","Yes"]

def main():
    root = Tk()
    root.resizable(0,0)
    Interface(root)
    root.mainloop()

main()