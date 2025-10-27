import os
import py3xui

class Autorize_Data :
    URL = os.environ["3X-UI_URL"]
    Login = os.environ["3X-UI_Login"]
    Password = os.environ["3X-UI_Password"]

api = py3xui.Api(Autorize_Data.URL, Autorize_Data.Login, Autorize_Data.Password)
api.login()