# Here we will create ORM Architecture Tool (DAO)

from PDBC_ORM_Project.Employee_Data import Model_Emp_SetGet as MD
import Connection_Emp as C


class DAO:
    def __init__(self):
        # Calling of Connection class
        self.Con = C.PDBC.Connection()
        # Object creation of Cursor class
        self.Cur = self.Con.cursor()

    # # Auto Generate ID code for Insert Command
    def AutoId(self):
        try:
            self.MaxId = 100
            Query = "select max(Eid) from emp"
            self.Cur.execute(Query)
            Result = self.Cur.fetchone()
            if(Result[0]==None):
                self.MaxId = self.MaxId + 1
            else:
                self.MaxId = Result[0] + 1
            return self.MaxId
        except Exception as msg:
            print(msg)

    # Insert Command
    def InsertData(self,E):
        try:
            Query = "insert into emp values(%d, '%s', '%s', %d)"
            Values = (E.getEid(),E.getName(), E.getDept(), E.getSalary())
            self.Cur.execute(Query % Values)
            self.Con.commit()
        except Exception as msg:
            print(msg)

    # Select Command for all data
    def SelectAllData(self):
        try:
            Mylist = []
            Query = "select * from emp"
            self.Cur.execute(Query)
            Result = self.Cur.fetchall()
            for row in Result:
                E = MD.Employee()
                E.setEid(row[0])
                E.setName(row[1])
                E.setDept(row[2])
                E.setSalary(row[3])
                Mylist.append(E)
            return Mylist
        except Exception as msg:
            print(msg)

    # Select Command for One data
    def SelectOneData(self,Eid):
        try:
            Query = "select * from emp where Eid=%d"
            self.Cur.execute(Query % Eid)
            Result = self.Cur.fetchone()
            if (self.Cur.rowcount > 0):
                E = MD.Employee()
                E.setEid(Result[0])
                E.setName(Result[1])
                E.setDept(Result[2])
                E.setSalary(Result[3])
            else:
                E = None
            return E
        except Exception as msg:
            print(msg)

    # Update Command
    def UpdateData(self,E):
        try:
            Query = "update emp set Name = '%s', Dept = '%s', Salary = %d where Eid = %d"
            Values = (E.getName(), E.getDept(), E.getSalary(), E.getEid())
            self.Cur.execute(Query % Values)
            self.Con.commit()
        except Exception as msg:
            print(msg)

    # Delete Command for All data
    def DeleteAllData(self):
        try:
            Query = "delete from emp"
            self.Cur.execute(Query)
            self.Con.commit()
        except Exception as msg:
            print(msg)

    # Delete Command for One data
    def DeleteOneData(self,Eid):
        try:
            Query = "delete from emp where Eid=%d"
            self.Cur.execute(Query % Eid)
            self.Con.commit()
        except Exception as msg:
            print(msg)

    # Connection Closing
    def __del__(self):
        self.Con.close()

