## do not upload to repository

class Credentials:
    def __init__(self, usr, pwd):
        self.username = usr
        self.password = pwd


def SetMondoDB():
    creds= Credentials("YOUR_USERNAME_HERE","YOUR_PASSWORD_HERE")
    return creds
