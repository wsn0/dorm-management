#Module.py

import tkinter as tk
from tkinter import messagebox
import csv


filepath = 'data_file_ourdorm_1.csv'
filepath2 = 'data_file_ourdorm_2.csv' 

def ownerMenu():
    global filepath
    Omain = tk.Tk()
    Omain.title('Our Dorm - main menu (Owner)')
    Omain.minsize(width=600,height=400)

    lb = tk.Label(master=Omain,text='Main menu',font=('Lucida Fax',19),bg="black",fg="white").grid(row=0,column=1,pady=15)

    with open(filepath,encoding='utf-8') as f:
        rd = csv.DictReader(f, delimiter=',')
        reader = list(rd)

        for i, room in enumerate(reader[1:4]):
            room_btn = tk.Button(master=Omain, text='Room ' + room['Room'], font=('Lucida Fax',15), width=20, height=10
                                 ,command=lambda myroom= room['Room']: (eachRoom(myroom),Omain.destroy()))
            room_btn.grid(row=1, column=i, padx=8, pady=6)

        for i, room in enumerate(reader[4:]):
            room_btn = tk.Button(master=Omain, text='Room ' + room['Room'], font=('Lucida Fax',15), width=20, height=10
                                 ,command=lambda myroom= room['Room']: (eachRoom(myroom), Omain.destroy()))
            room_btn.grid(row=2, column=i, padx=8, pady=6)




def Uty(myroom):
    global filepath2
    with open(filepath2 ,encoding='utf-8') as f:
        rd = csv.DictReader(f, delimiter=',')
        reader = list(rd)
        for k in reader:
            if k['Room'] == myroom:
                uty = tk.Tk()
                uty.title('Our Dorm - Utilities')
                uty.minsize(width=600,height=400)
                 
                lb = tk.Label(master=uty,text='Utilities',font=('Lucida Fax',20),bg="black",fg="white").grid(row=0,column=1,pady=15)

                lbroom = tk.Label(master=uty,text='Room ' + k['Room'],font=('Lucida Fax',18)
                              ,bg="black",fg="white").grid(row=1,column=1,pady=15)
        
                lbinfo = tk.Label(master=uty,text='Water is 22 Bath per Unit\n\nElectricity is 7 Bath per Unit'
                                  ,font=('Lucida Fax',10,'italic')).grid(row=2,column=1,pady=15)

                #Month
                lbMonth = tk.Label(master=uty,text='Month :',font=('Lucida Fax',13)).grid(row=4,padx=7,pady=15)
                Month = tk.StringVar()
                Month_inp = tk.Entry(uty,textvariable=Month,width=35,font=('Lucida Fax',13)).grid(row=4,column=1,padx=7,pady=10)
                
                #Water
                lbWaterUnit = tk.Label(master=uty,text='Water unit used :',font=('Lucida Fax',13)).grid(row=5,padx=7,pady=15)
                WaterUnit = tk.StringVar()
                WaterUnit_inp = tk.Entry(uty,textvariable=WaterUnit,width=35,font=('Lucida Fax',13)).grid(row=5,column=1,padx=7,pady=10)

                #Electricity
                lbElecUnit = tk.Label(master=uty,text='Electricity unit used :',font=('Lucida Fax',13)).grid(row=6,padx=7,pady=15)
                ElecUnit = tk.StringVar()
                ElecUnit_inp = tk.Entry(master=uty,textvariable=ElecUnit,width=35,font=('Lucida Fax',13)).grid(row=6,column=1,padx=7,pady=10)


                #Button
                sm_btn = tk.Button(master=uty,text='Calculate',font=('Lucida Fax',11),width=10
                    ,command=lambda: (uty.destroy(), Cal(myroom,WaterUnit,ElecUnit,Month)))
                sm_btn.grid(row=10,column=1,padx=15,pady=19)
                
                back_btn = tk.Button(master=uty,text='Back',font=('Lucida Fax',11),width=10
                    ,command=lambda: (uty.destroy(), ownerMenu()))
                back_btn.grid(row=0,column=0,padx=15,pady=19)

                

#Cal + save Data
def Cal(myroom ,WaterUnit,ElecUnit,Month):
    global filepath2

    Water_Unit = float(WaterUnit.get())
    Elec_Unit = float(ElecUnit.get())
    WaterBill = Water_Unit * 22
    ElecBill = Elec_Unit * 7
    TotalBill = WaterBill + ElecBill

    
    with open(filepath2, 'r', encoding='utf-8') as f:
        rd = csv.DictReader(f)
        reader = list(rd)

        for y in reader:
            if y['Room'] == myroom:
                y['Month'] = Month.get()
                y['Water_unit'] = WaterUnit.get()
                y['Electric_unit'] = ElecUnit.get()
                y['Water_bill'] = WaterBill
                y['Electric_bill'] = ElecBill
                y['Total'] = TotalBill

                
    with open(filepath2, 'w', encoding='utf-8', newline='') as f:
        header = ['Room', 'Month', 'Water_unit', 'Electric_unit', 'Water_bill', 'Electric_bill', 'Total']
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(reader)

    eachRoomUty(myroom)



def eachRoomUty(myroom):
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

                lbWaterUnitUsed = tk.Label(master=roomUty,text='Water unit used : '+ z['Water_unit'] +' Unit'
                                           ,font=('Lucida Fax',13)).grid(row=2,column=1,pady=15)
                lbWaterBill = tk.Label(master=roomUty,text='Water Bill : '+ z['Water_bill'] +' Bath'
                                       ,font=('Lucida Fax',13)).grid(row=3,column=1,pady=5)
                        
                lbWaterUnitUsed = tk.Label(master=roomUty,text='Electricity unit used : '+ z['Electric_unit'] +' Unit'
                                           ,font=('Lucida Fax',13)).grid(row=4,column=1,pady=15)
                lbWaterUnitUsed = tk.Label(master=roomUty,text='Electricity Bill : '+ z['Electric_bill'] +' Bath'
                                           ,font=('Lucida Fax',13)).grid(row=5,column=1,pady=5)

                lbTotal = tk.Label(master=roomUty,text='Total '+ z['Total'] +' Bath',font=('Lucida Fax',11)
                                   ,bg="black",fg="white").grid(row=6,column=1,pady=20)
                       

        Record_btn = tk.Button(master=roomUty,text='Record',font=('Lucida Fax',11),width=10
                    ,command=lambda: (roomUty.destroy(), Uty(myroom)))
        Record_btn.grid(row=10,column=1,padx=15,pady=19)
        
        Menu_btn = tk.Button(master=roomUty,text='Menu',font=('Lucida Fax',11),width=10, height=1
                         ,command=lambda: (roomUty.destroy(), ownerMenu()))
        Menu_btn.grid(row=0,column=0,padx=6)





    
    
#save Edit Renter Info
def edtIng(myroom,nm,nicknm,ag,bday,nid,ntel,nmail,nmi,nmo):
    global filepath
    
    with open(filepath, 'r', encoding='utf-8') as f:
        rd = csv.DictReader(f)
        reader = list(rd)

        for j in reader:
            if j['Room'] == myroom:
                j['Name'] = nm.get()
                j['Nickname'] = nicknm.get()
                j['Age'] = ag.get()
                j['Birthday'] = bday.get()
                j['Id'] = nid.get()
                j['Email'] = nmail.get()
                j['Tel'] = ntel.get()
                j['Enter'] = nmi.get()
                j['Leave'] = nmo.get()

    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        header = ['Room', 'Fee', 'Name', 'Nickname', 'Age', 'Birthday',
                  'Tel', 'Id', 'Email', 'Enter', 'Leave']
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(reader)

    eachRoom(myroom)

        
def infoEdit(myroom):
    global filepath
    with open(filepath,encoding='utf-8') as f:
        rd = csv.DictReader(f, delimiter=',')
        reader = list(rd)
        for k in reader:
            if k['Room'] == myroom:
                edit = tk.Tk()
                edit.title('Edit info')
                edit.minsize(width=600,height=400)
                lb = tk.Label(master=edit,text='Room ' + k['Room'],font=('Lucida Fax',19)
                              ,bg="black",fg="white").grid(row=0,column=1,pady=15)

                #new name section
                new_name = tk.Label(master=edit,text='Name',font=('Lucida Fax',13)).grid(row=1,pady=15)
                nm = tk.StringVar()
                nm_inp = tk.Entry(master=edit,textvariable=nm,width=35,font=('Lucida Fax',12)).grid(row=1,column=1,padx=7,pady=10)
                
                #new nickname section
                new_nickname = tk.Label(master=edit,text='Nickname',font=('Lucida Fax',13)).grid(row=2)
                nicknm = tk.StringVar()
                nicknm_inp = tk.Entry(master=edit,textvariable=nicknm,width=35,font=('Lucida Fax',12)).grid(row=2,column=1,padx=7,pady=10)
                
                #new age section
                new_age = tk.Label(master=edit,text='Age',font=('Lucida Fax',13)).grid(row=3)
                ag = tk.StringVar()
                ag_inp = tk.Entry(master=edit,textvariable=ag,width=35,font=('Lucida Fax',12)).grid(row=3,column=1,padx=7,pady=10)
                
                #new birthday section
                new_bday = tk.Label(master=edit,text='Birthday',font=('Lucida Fax',13)).grid(row=4)
                bday = tk.StringVar()
                bday_inp = tk.Entry(master=edit,textvariable=bday,width=35,font=('Lucida Fax',12)).grid(row=4,column=1,padx=7,pady=10)
                
                #new id section
                new_id = tk.Label(master=edit,text='ID',font=('Lucida Fax',13)).grid(row=5)
                nid = tk.StringVar()
                nid_inp = tk.Entry(master=edit,textvariable=nid,width=35,font=('Lucida Fax',12)).grid(row=5,column=1,padx=7,pady=10)
                
                #new tel section
                new_tel = tk.Label(master=edit,text='Tel.',font=('Lucida Fax',13)).grid(row=6)
                ntel = tk.StringVar()
                ntel_inp = tk.Entry(master=edit,textvariable=ntel,width=35,font=('Lucida Fax',12)).grid(row=6,column=1,padx=7,pady=10)
                
                #new email section
                new_email = tk.Label(master=edit,text='Email',font=('Lucida Fax',13)).grid(row=7)
                nmail = tk.StringVar()
                nmail_inp = tk.Entry(master=edit,textvariable=nmail,width=35,font=('Lucida Fax',12)).grid(row=7,column=1,padx=7,pady=10)

                #new move in section 
                new_mi = tk.Label(master=edit,text='Enter',font=('Lucida Fax',13)).grid(row=8)
                nmi = tk.StringVar()
                nmi_inp = tk.Entry(master=edit,textvariable=nmi,width=35,font=('Lucida Fax',12)).grid(row=8,column=1,padx=7,pady=10)

                #new move out section
                new_mo = tk.Label(master=edit,text='Leave',font=('Lucida Fax',13)).grid(row=9)
                nmo = tk.StringVar()
                nmo_inp = tk.Entry(master=edit,textvariable=nmo,width=35,font=('Lucida Fax',12)).grid(row=9,column=1,padx=7,pady=10)


                sm_btn = tk.Button(master=edit,text='Submit',font=('Lucida Fax',11),width=10
                                   ,command=lambda:(edit.destroy(), edtIng(myroom,nm,nicknm,ag,bday,nid,ntel,nmail,nmi,nmo)))
                sm_btn.grid(row=10,column=1,padx=15,pady=19)

    
                back_btn = tk.Button(master=edit,text='Back',font=('Lucida Fax',11),width=10
                             ,command=lambda: (edit.destroy(), eachRoom(myroom)))
                back_btn.grid(row=0,column=0,padx=15,pady=19)
                

def eachRoom(myroom):
    global filepath
    with open(filepath,encoding='utf-8') as f:
        rd = csv.DictReader(f, delimiter=',')
        reader = list(rd)

        for i in reader:
            if i['Room'] == myroom:
                room = tk.Tk()
                room.title('Our Dorm - Room ' + i['Room'])
                room.minsize(width=600,height=400)
                lb = tk.Label(master=room,text='Room ' + i['Room'],font=('Lucida Fax',19)
                              ,bg="black",fg="white").grid(row=0,column=1,pady=15)
                
                info_txt = tk.Text(master=room,height=20, width=52)
                info_txt.grid(row=2,column=1,pady=15)

                for row in reader:
                    if row['Room'] == myroom:
                        for key, value in row.items():
                            txt = '{} : {}' .format(key, value) +'\n'
                            info_txt.insert(tk.END, txt)
                        break
                
        back_btn = tk.Button(master=room,text='Back',font=('Lucida Fax',11),width=10, height=1
                         ,command=lambda: (room.destroy(), ownerMenu()))
        back_btn.grid(row=0,column=0,padx=20)

        edit_btn = tk.Button(master=room,text='Edit',font=('Lucida Fax',11),width=10, height=1
                         ,command=lambda: (room.destroy(), infoEdit(myroom)))
        edit_btn.grid(row=2,column=0,padx=20)

        ut_btn = tk.Button(master=room,text='Utilities',font=('Lucida Fax',11),width=10, height=1
                       ,command=lambda: (room.destroy(), eachRoomUty(myroom)))
        ut_btn.grid(row=1,column=0,padx=20)

        
