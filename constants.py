import configparser

config = configparser.ConfigParser()
config.read("config.ini")

ACTIVE = False
TRIGGERED = False
RECEIVE_MAIL = config.get("DEFAULT", "receiveMail")
SEND_MAIL = config.get("DEFAULT", "sendMail")
