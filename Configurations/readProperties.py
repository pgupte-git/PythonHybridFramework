import configparser
import os
from pathlib import Path

config = configparser.RawConfigParser()
settings_file = 'config.ini'
config_folder = os.path.dirname(__file__)
full_config_file_path = os.path.join(config_folder, settings_file)
#print(full_config_file_path)
config.read(full_config_file_path)


class ReadConfig:
    @staticmethod
    def getUsername():
        username = config.get("admin Login info", "username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("admin Login info", "password")
        return password

    @staticmethod
    def getimagepath():
        image_url = os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir),config.get("Screenshot folder path",
                                                                                               "image_path"))
        return image_url

    @staticmethod
    def get_application_logs():
        log_file_url = os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir), config.get("Application Logs file path",
                                                                                                   "log_file_path"))
        return log_file_url

    @staticmethod
    def get_xls_file():
        xlsfilepath = os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir), config.get("Data driven excel file path",
                                                                                                  "excel_file_path"))
        return xlsfilepath
