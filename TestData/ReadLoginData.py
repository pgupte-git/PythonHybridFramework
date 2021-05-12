import pytest

from Utilities import XlsUtil
from Configurations.readProperties import ReadConfig


class ReadLoginData:

    @staticmethod
    def getlogindata():
        Dict = {}
        xls_path = ReadConfig.get_xls_file()

        rows = XlsUtil.getrowcount(xls_path, 'LoginData')
        columns = XlsUtil.getcolumncount(xls_path, 'LoginData')
        print("Number of rows in a active sheet are", rows)
        print("Number of columns in a active sheet are", columns)

        # Logic to read the data from excel sheet we need to use two for loops one for row and one for column
        for r in range(2, rows + 1):
            for c in range(1, columns + 1):
                Dict[XlsUtil.readfirstrow(xls_path, c, 'LoginData')] = XlsUtil.readData(xls_path, r, c, 'LoginData')
        print([Dict])
        return ([Dict])




