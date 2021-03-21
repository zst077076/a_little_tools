
import configparser

config = configparser.ConfigParser()
config.read("..\\data\\config.ini")

# "获取配置文件的path"
user =config.get("account","user")
passwd =config.get("account","passwd")

