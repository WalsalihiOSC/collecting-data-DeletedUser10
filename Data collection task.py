
from tkinter import*
from tkinter import messagebox
"""Data collection task"""

class Variables:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone


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

        self.button1 = Button(self.frame1, text = "Show All", command=self.display_data)
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

        """ Radio buttons """
        self.radio_var = StringVar()
        self.radio_var.set(self.data.radios)

        for radio in self.data.radios:
            Radiobutton(self.frame2, text = radio, 
                        variable=self.radio_var, 
                        value=radio, bg = "White").grid(column=1, sticky=W)

        self.button2 = Button(self.frame2, text = "Enter Data", bg = "white", command=self.enter_data)
        self.button2.grid(row=5, padx=30)



    
    def enter_data(self):
        self.data.people_data.append(Variables(self.e1.get(), self.e2.get(), self.radio_var.get()))

        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.radio_var.set(None)


    """Creates frame 3"""
    def display_data(self):
        self.frame2.grid_forget()
        self.data_label.configure(text = "Displaying Person Data")
        self.frame3 = Frame(self.main_frame,highlightbackground="black", highlightthickness=1, 
                                        height=200, 
                                        width=300, bg = "White")
        self.frame3.grid(row=1, column=0)


        
        for data in self.data.people_data:
    
            self.framel = Frame(self.frame3, bg = "white" ,highlightbackground="black", highlightthickness=1, width=300)
            self.framel.grid(column=0)
            
            self.name_labl = Label(self.framel, text = "First name: ", bg = "white")
            self.age_labl = Label(self.framel, text = "Age: ", bg = "white")


            self.user_name = Label(self.framel, text = data.name, bg = "White")
            self.user_age = Label(self.framel, text = data.age, bg = "White")
            self.final_labl = Label(self.framel, text = f"{data.name} aged {data.age} \n has phone: {data.phone}", bg = "white")
            
            self.name_labl.grid(row=1, column=0, padx=10,pady=4)
            self.age_labl.grid(row=2, column=0, padx=10,pady=4)

            self.user_name.grid(row = 1, column=1, padx=20)
            self.user_age.grid(row = 2, column=1, padx=20)
            self.final_labl.grid(row=5, column=0, padx=10, pady=30, sticky=E)
    
        
        self.back_bttn = Button(self.frame3, text = "Add person ", bg = "White", command=self.back)
        self.back_bttn.grid(row=3, column=0)
        self.button1.grid_forget()




    
    def back(self):
        self.frame3.grid_forget()
        self.button1.grid(column=3, row=0, pady=10,sticky=NSEW)
        self.frame2.grid(row=1)
        
  

"""Ui class"""
class UI:
    def __init__(self, people_data = []):
        self.radios = ["No", "Yes"]
        self.people_data = people_data
        

def main():
    root = Tk()
    root.resizable(0,0)
    Interface(root)
    root.mainloop()

main()