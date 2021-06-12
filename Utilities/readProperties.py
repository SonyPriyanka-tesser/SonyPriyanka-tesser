import configparser
#By default in python configparser package is installed no need to install it seperately
#configparser is a pakage in that RawConfigParser is a class for that class we are creating a object
#with the help of Object we read config properties by giving config.read("config properties path")
config=configparser.RawConfigParser()
config.read("C:\\Users\\sonup\\PycharmProjects\\Project\\Configurations\\config.ini")

class ReadConfig:
    #every config variable should have seperate class we have 3 varables in config so will create 3 class
    #there is no need of creating object to call respective class if we use static method
    #getApplicationURL is a method will get a information from common info of base URL in config properties
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUsername():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password

    @staticmethod
    def getServer():
        server = config.get('common info', 'server')
        return server

    @staticmethod
    def getPortNumber():
        portnumber = config.get('common info', 'portnumber')
        return portnumber

    @staticmethod
    def getDatabases():
        Database = config.get('common info', 'Database')
        return Database

    @staticmethod
    def getUser():
        user = config.get('common info', 'user')
        return user

    @staticmethod
    def getPass():
        pwd= config.get('common info', 'pwd')
        return pwd

