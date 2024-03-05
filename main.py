import tkinter as tk
from tkinter import messagebox
import csv
import owner
import renter

filepath = 'data_file_ourdorm_1.csv'

#checking section
def mainMenu():

    mymail = strm.get()
    myiden = stri.get()


    with open(filepath,encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',')
        lines = list(reader)

        if mymail == lines[0]['Email'] and myiden == lines[0]['Id']:
            owner.ownerMenu()
            root.destroy()
            
        elif any(line['Email'] == mymail for line in lines[1:]) and any(line['Id'] == myiden for line in lines[1:]):
            renter.renterMenu(mymail, myiden)
            root.destroy()
            
        else:
            messagebox.askretrycancel("Error", "Your E-mail and Id are incorrect")


#log-in section

root = tk.Tk()
root.title('Our Dorm')
root.minsize(width=600, height=400)

lb = tk.Label(master=root,text='Welcome to Our Dorm!',font=('Lucida Fax',20), bg="black",fg="white").pack(pady=25)

lbEmail = tk.Label(master=root,text='- Email -',font=('Lucida Fax',12)).pack(pady = 20)
strm = tk.StringVar()
mail_inp = tk.Entry(master=root,textvariable=strm,width=25,font=('Lucida Fax',12)).pack(pady = 0)


lbID = tk.Label(master=root,text='- Id -',font=('Lucida Fax',12)).pack(pady = 20)
stri = tk.StringVar()
id_inp = tk.Entry(master=root,textvariable=stri,width=25,font=('Lucida Fax',12)).pack(pady = 0)


sub_btn = tk.Button(master=root,text='Submit',font=('Lucida Fax',10), width=13,height=1
                    ,command=mainMenu)
sub_btn.pack(pady = 20)

root.mainloop()






