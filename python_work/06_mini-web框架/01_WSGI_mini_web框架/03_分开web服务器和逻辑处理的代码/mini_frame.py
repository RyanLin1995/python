import time


def login():
    return "{}:welcome to our website".format(time.ctime())


def register():
    return "{}:welcome to register".format(time.ctime())


def profile():
    return "{}:welcome to profile".format(time.ctime())


def application(file_name):
    if file_name == "/login.py":
        return login()
    if file_name == "/register.py":
        return register()
    if file_name == "/profile.py":
        return profile()
    else:
        return "{}:page not found".format(time.ctime())
