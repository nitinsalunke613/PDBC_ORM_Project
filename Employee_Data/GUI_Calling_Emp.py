# Here we will design our GUI for Employee

from tkinter import *
import DAO_Emp as D
import Model_Emp_SetGet as M
from tkinter import messagebox
from tkinter import simpledialog

class EmpGUI:
    def __init__(self):
        # Label Creation
        self.label1 = Label(root,text='Employee ID',fg='Black',font=('Arial',15,'bold'))
        self.label1.place(x=80,y=80)
        self.label2 = Label(root,text='Employee Name',fg='Black',font=('Arial',15,'bold'))
        self.label2.place(x=80,y=140)
        self.label3 = Label(root,text='Employee Department',fg='Black',font=('Arial',15,'bold'))
        self.label3.place(x=80,y=200)
        self.label4 = Label(root,text='Employee Salary',fg='Black',font=('Arial',15,'bold'))
        self.label4.place(x=80,y=260)
        self.label5 = Label(root,text='',fg='Red',font=('Arial',15,'bold'))
        self.label5.place(x=180,y=480)

        # Entry Widget Creation
        self.eId = IntVar()
        self.entry1 = Entry(root,textvariable=self.eId,fg='Blue',font=('Courier',15))
        self.entry1.place(x=340,y=80)

        self.eName = StringVar()
        self.entry2 = Entry(root,textvariable=self.eName,fg='Blue',font=('Courier',15))
        self.entry2.place(x=340,y=140)

        self.eDept = StringVar()
        self.entry3 = Entry(root,textvariable=self.eDept,fg='Blue',font=('Courier',15))
        self.entry3.place(x=340,y=200)

        self.eSalary = IntVar()
        self.entry4 = Entry(root,textvariable=self.eSalary,fg='Blue',font=('Courier',15))
        self.entry4.place(x=340,y=260)

        # Button Creation
        self.button1 = Button(root,text='Auto ID',width=10,bg='Grey',fg='White',
                              font=('Consolas',10,'bold'),command=lambda : self.ButtonClick(1))
        self.button1.place(x=600,y=80)
        self.button2 = Button(root,text='Insert Data',width=12,bg='Grey',fg='White',
                              font=('Consolas',13,'bold'),command=lambda : self.ButtonClick(2))
        self.button2.place(x=50,y=350)
        self.button3 = Button(root,text='Search Data',width=12,bg='Grey',fg='White',
                              font=('Consolas',13,'bold'),command=lambda : self.ButtonClick(3))
        self.button3.place(x=200,y=350)
        self.button4 = Button(root,text='Search All Data',width=15,bg='Grey',fg='White',
                              font=('Consolas',11,'bold'),command=lambda: self.ButtonClick(4))
        self.button4.place(x=195,y=420)
        self.button5 = Button(root,text='Update Data',width=12,bg='Grey',fg='White',
                              font=('Consolas',13,'bold'),command=lambda : self.ButtonClick(5))
        self.button5.place(x=500,y=350)
        self.button6 = Button(root,text='Delete Data',width=12,bg='Grey',fg='White',
                              font=('Consolas',13,'bold'),command=lambda : self.ButtonClick(6))
        self.button6.place(x=350,y=350)
        self.button4 = Button(root,text='Delete All Data',width=15,bg='Grey',fg='White',
                              font=('Consolas',11,'bold'),command=lambda: self.ButtonClick(7))
        self.button4.place(x=345, y=420)
        self.button7 = Button(root,text='Save Data',width=12,bg='Grey',fg='White',
                              font=('Consolas',13,'bold'),command=lambda : self.ButtonClick(8))
        self.button7.place(x=50,y=420)
        self.button8 = Button(root,text='Exit',width=12,bg='Grey',fg='White',
                              font=('Consolas',13,'bold'),command=lambda: self.ButtonClick(9))
        self.button8.place(x=500,y=420)


    def ButtonClick(self,Value):
        if (Value == 1):
            Emp = D.DAO()
            self.entry1.delete(0, END)
            self.entry2.delete(0, END)
            self.entry3.delete(0, END)
            self.entry4.delete(0, END)
            self.label5['text'] = ' '
            Emp.AutoId()
            messagebox.showinfo(title='Auto ID',message='Your Employee ID will be : {}'.format(Emp.MaxId))
            self.eId.set(Emp.MaxId)

        elif (Value == 2):
            Emp = D.DAO()
            E = M.Employee()
            E.setEid(self.eId.get())
            E.setName(self.eName.get())
            E.setDept(self.eDept.get())
            E.setSalary(self.eSalary.get())

            Emp.InsertData(E)

            self.label5['text'] = 'Record Inserted....{} row affected'.format(Emp.Cur.rowcount)

        elif (Value == 3):
            Emp = D.DAO()
            eid = simpledialog.askinteger(title='Employee ID',prompt='Enter Employee ID to search Record : ')
            Result = Emp.SelectOneData(eid)
            if (Result != None):
                self.eId.set(Result.getEid())
                self.eName.set(Result.getName())
                self.eDept.set(Result.getDept())
                self.eSalary.set(Result.getSalary())
            else:
                self.entry1.delete(0,END)
                self.entry2.delete(0,END)
                self.entry3.delete(0,END)
                self.entry4.delete(0,END)
                self.label5['text'] = 'No Record Found'

        elif (Value == 4):
            Emp = D.DAO()
            self.new_root = Toplevel(root)
            self.new_root.geometry('500x500')
            self.new_root.maxsize(500,500)
            self.new_root.minsize(500,500)
            self.new_root.title('All Employee Record')
            self.new_root.iconbitmap('Emp.ico')

        elif (Value == 5):
            Emp = D.DAO()
            eid = simpledialog.askinteger(title='Employee ID', prompt='Enter Employee ID to Update Data : ')
            Result = Emp.SelectOneData(eid)
            if (Result != None):
                self.eId.set(Result.getEid())
                self.eName.set(Result.getName())
                self.eDept.set(Result.getDept())
                self.eSalary.set(Result.getSalary())
            else:
                self.entry1.delete(0,END)
                self.entry2.delete(0,END)
                self.entry3.delete(0,END)
                self.entry4.delete(0,END)
                self.label5['text'] = 'No Record Found'

        elif (Value == 6):
            Emp = D.DAO()
            eid = simpledialog.askinteger(title='Delete Window',prompt='Enter Employee ID to Delete the record : ')
            Result = Emp.SelectOneData(eid)
            if (Result != None):
                self.eId.set(Result.getEid())
                self.eName.set(Result.getName())
                self.eDept.set(Result.getDept())
                self.eSalary.set(Result.getSalary())

                Choice = messagebox.askyesnocancel(title='Delete Window'
                                                   ,message='Are you sure, you want to Delete this record?')
                if (Choice == True):
                    Emp.DeleteOneData(eid)
                    self.label5['text'] = 'Record Deleted....{} row affected'.format(Emp.Cur.rowcount)

            else:
                self.entry1.delete(0,END)
                self.entry2.delete(0, END)
                self.entry3.delete(0, END)
                self.entry4.delete(0, END)

                self.label5['text'] = 'No Record Found'

        elif (Value == 7):
            Emp = D.DAO()
            Confirm = messagebox.askyesnocancel(title='Delete All Window'
                                                ,message='Are you sure, you want to delete all record of the table?')
            if (Confirm == True):
                Emp.DeleteAllData()
                self.label5['text'] = ('All record Deleted....{} row affected'.format(Emp.Cur.rowcount))

        elif (Value == 8):
            Emp = D.DAO()
            Confirm = messagebox.askyesnocancel(title='Save Window'
                                                ,message='Are you sure, you want to save this record?')
            if (Confirm == True):
                E = M.Employee()
                E.setEid(self.eId.get())
                E.setName(self.eName.get())
                E.setDept(self.eDept.get())
                E.setSalary(self.eSalary.get())

                Emp.UpdateData(E)

                self.label5['text'] = 'Record Saved....{} row affected'.format(Emp.Cur.rowcount)

        elif (Value == 9):
            Confirm = messagebox.askyesnocancel(title='Exit Window'
                                                ,message='Are you sure, you want to exit this window?')
            if (Confirm == True):
                root.destroy()


root = Tk()

root.geometry('700x550')
root.maxsize(700,550)
root.minsize(700,550)
root.title('Employee Data')
root.iconbitmap('Emp.ico')

EG = EmpGUI()

root.mainloop()

