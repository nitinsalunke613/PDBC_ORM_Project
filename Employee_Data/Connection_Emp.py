# Here we will establish a connection of Python and Database using Connect class

from MySQLdb import *

class PDBC:
    @staticmethod
    def Connection():
        Con = Connect(host='localhost',user='root',password='NitinSQL@123',database='employee_data')
        return Con

