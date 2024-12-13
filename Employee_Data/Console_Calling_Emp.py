# Here we will call our Model and DAO module to perform an actions on all the commands

from PDBC_ORM_Project.Employee_Data import Model_Emp_SetGet as MD
import DAO_Emp as D

Choice = ''
while(Choice != 'Exit'):
    print('----------------- ORM --------------------------')
    print('1. Insert Data.... Type Insert')
    print('2. Search All Data.... Type Search All')
    print('3. Search One Data.... Type Search One')
    print('4. Update Data.... Type Update')
    print('5. Delete All Data.... Type Delete All')
    print('6. Delete One Data.... Type Delete One')
    print('7. Exit Connection.... Type Exit')
    print('-------------------------------------------------------------------')

    Choice = input('Enter your choice as per above : ')

    print('-------------------------------------------------------------------')

    if(Choice == 'Insert'):
        E = MD.Employee()
        Emp = D.DAO()

        Emp.AutoId()
        print('Employee ID : ',Emp.MaxId)

        eName = input('Enter Employee Name : ')
        eDept = input('Enter Employee Department : ')
        eSalary = int(input('Enter Employee Salary : '))

        E.setEid(Emp.MaxId)
        E.setName(eName)
        E.setDept(eDept)
        E.setSalary(eSalary)

        Emp.InsertData(E)

        print('-----Record Inserted-----')


    elif(Choice == 'Search All'):
        Emp = D.DAO()
        List = Emp.SelectAllData()
        print('ID     Name     Dept    Salary')
        for row in List:
            print('-------------------------------------')
            print(row.getEid(),end='    ')
            print(row.getName(),end='    ')
            print(row.getDept(),end='     ')
            print(row.getSalary())


    elif(Choice == 'Search One'):
        Emp = D.DAO()
        eId = int(input('Enter Employee ID to search : '))
        Result = Emp.SelectOneData(eId)
        if(Result != None):
            print('ID     Name     Dept    Salary')
            print('-------------------------------------')
            print(Result.getEid(),end='    ')
            print(Result.getName(),end='    ')
            print(Result.getDept(),end='    ')
            print(Result.getSalary())
            print('-------------------------------------')
        else:
            print('-----No Record Found-----')


    elif(Choice == 'Update'):
        Emp = D.DAO()

        eId = int(input('Enter Employee ID to update the Data : '))
        Result = Emp.SelectOneData(eId)
        if (Result != None):
            print('ID     Name     Dept    Salary')
            print('-------------------------------------')
            print(Result.getEid(),end='    ')
            print(Result.getName(),end='    ')
            print(Result.getDept(),end='    ')
            print(Result.getSalary())
            print('-------------------------------------')

            Confirm = input('Are you sure, you want to update above data? (yes/no) : ')

            if(Confirm == 'yes'):
                eName = input('Enter new Name of Employee : ')
                eDept = input('Enter new Department of Employee : ')
                eSalary = int(input('Enter new Salary of Employee : '))

                E = MD.Employee()
                E.setEid(eId)
                E.setName(eName)
                E.setDept(eDept)
                E.setSalary(eSalary)

                Emp.UpdateData(E)

                print('-----Record Updated-----')

        else:
            print('-----No Record Found-----')


    elif(Choice == 'Delete All'):
        Emp = D.DAO()

        Confirm = input('Are you sure, you want to delete all Data? (yes/no) : ')

        if(Confirm == 'yes'):
            Emp.DeleteAllData()
            print('-----All Record Deleted-----')


    elif(Choice == 'Delete One'):
        Emp = D.DAO()

        eId = int(input('Enter Employee ID to Delete the record : '))
        Result = Emp.SelectOneData(eId)
        if(Result != None):
            print('ID     Name     Dept    Salary')
            print('-------------------------------------')
            print(Result.getEid(),end='    ')
            print(Result.getName(),end='    ')
            print(Result.getDept(),end='    ')
            print(Result.getSalary())
            print('-------------------------------------')

            Confirm = input('Are you sure, you want to delete above data? (yes/no) : ')

            if(Confirm == 'yes'):
                Emp.DeleteOneData(eId)
                print('-----Record Deleted-----')

        else:
            print('-----No Record Found-----')


    elif(Choice == 'Exit'):
        print('----------Connection Closed----------')

