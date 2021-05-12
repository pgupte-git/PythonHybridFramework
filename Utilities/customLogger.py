import inspect
import os
import logging

from Configurations.readProperties import ReadConfig


class LogGen:

    @staticmethod
    def getLogger():
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)

        #log_dir = os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir), 'PythonHybridFramework/Logs/application.log')

        fileHandler = logging.FileHandler(ReadConfig.get_application_logs()+"TestScript_Run.log")
        print(fileHandler)

        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)


        logger.setLevel(logging.DEBUG)
        return logger
