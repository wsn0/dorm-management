#Module.py

import tkinter as tk
from tkinter import messagebox
import csv

filepath = 'renter_info.csv'
filepath2 = 'utilities_info.csv'

def renterMenu(mymail,myiden):
    global filepath
    
    Rmain = tk.Tk()
    Rmain.title('Our Dorm - main menu (Renter)')
    Rmain.minsize(width=600,height=400)

    
    with open(filepath,encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',')
        lines = list(reader)
        
        for i in lines:
            if i['Email'] == mymail and i['Id'] == myiden:
                lbroom = tk.Label(master=Rmain,text='Room ' + i['Room'],font=('Lucida Fax',21)
                                  ,bg="black",fg="white").grid(row=1,column=1,pady=15)
                
                inf_btn = tk.Button(master=Rmain,text='My info',font=('Lucida Fax',15),width=20, height=10
                        ,command=lambda:(Rmain.destroy(), Inf(mymail,myiden)))
                inf_btn.grid(row=2,column=0,padx=30,pady=12)
                
                uti_btn = tk.Button(master=Rmain,text='Utilities',font=('Lucida Fax',15),width=20, height=10
                        ,command=lambda myroom= i['Room']:(Rmain.destroy(), eachRoomUty(myroom,mymail,myiden)))
                uti_btn.grid(row=2,column=2,padx=30,pady=12)
                
                break

        
def Inf(mymail,myiden):
    global filepath
    
    info = tk.Tk()
    info.title('Our Dorm - My info')
    info.minsize(width=600,height=400)

    lb = tk.Label(master=info,text='My info',font=('Lucida Fax',20),bg="black",fg="white").grid(row=0,column=1,pady=15)
    info_txt = tk.Text(master=info,height=20, width=52)
    info_txt.grid(row=2,column=1,pady=15)

    with open(filepath,encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',')
        lines = list(reader)

        for row in lines:
            if row['Email'] == mymail and row['Id'] == myiden:
                for key, value in row.items():
                    txt = '{} : {}' .format(key, value) +'\n'
                    info_txt.insert(tk.END, txt)
                break
    back_btn = tk.Button(master=info,text='Back',font=('Lucida Fax',11),width=10, height=1
                         ,command=lambda: (info.destroy(), renterMenu(mymail,myiden)))
    back_btn.grid(row=0,column=0,padx=15,pady=19)


def eachRoomUty(myroom,mymail,myiden):
    global filepath2
    with open(filepath2 ,encoding='utf-8') as f:
        rd = csv.DictReader(f, delimiter=',')
        reader = list(rd)

        for z in reader:
            if z['Room'] == myroom:
                roomUty = tk.Tk()
                roomUty.title('Our Dorm - Room ' + z['Room'] + ' (Utilities)')
                roomUty.minsize(width=600,height=400)
                lb = tk.Label(master=roomUty,text='Room ' + z['Room'],font=('Lucida Fax',19)
                              ,bg="black",fg="white").grid(row=0,column=1,pady=15)

                lbMonth = tk.Label(master=roomUty,text=z['Month'],font=('Lucida Fax',15)).grid(row=1,column=1,pady=15)
                
                lbinfo = tk.Label(master=roomUty,text='Water is 22 Bath per Unit\n\nElectricity is 7 Bath per Unit'
                                  ,font=('Lucida Fax',10, 'italic')).grid(row=2,column=1,pady=15)
                

                lbWaterUnitUsed = tk.Label(master=roomUty,text='Water unit used : '+ z['Water_unit'] +' Unit'
                                           ,font=('Lucida Fax',13)).grid(row=3,column=1,pady=15)
                lbWaterBill = tk.Label(master=roomUty,text='Water Bill : '+ z['Water_bill'] +' Bath'
                                       ,font=('Lucida Fax',13)).grid(row=4,column=1,pady=5)
                        
                lbWaterUnitUsed = tk.Label(master=roomUty,text='Electricity unit used : '+ z['Electric_unit'] +' Unit'
                                           ,font=('Lucida Fax',13)).grid(row=5,column=1,pady=20)
                lbWaterUnitUsed = tk.Label(master=roomUty,text='Electricity Bill : '+ z['Electric_bill'] +' Bath'
                                           ,font=('Lucida Fax',13)).grid(row=6,column=1,pady=5)

                lbTotal = tk.Label(master=roomUty,text='Total '+ z['Total'] +' Bath'
                                   ,font=('Lucida Fax',13),bg="black",fg="white").grid(row=7,column=1,pady=20)
                       
        
        back_btn = tk.Button(master=roomUty,text='Back',font=('Lucida Fax',11),width=10, height=1
                         ,command=lambda: (roomUty.destroy(), renterMenu(mymail,myiden)))
        back_btn.grid(row=0,column=0,padx=6)
    


