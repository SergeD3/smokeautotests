import string
import random

letters = string.ascii_uppercase
number = random.randint(10, 500)
rand_string = '_' + ''.join(random.choice(letters) for i in range(2, 5)) + '_' + str(number)
print(rand_string)


class AddUser:

    def __init__(self, uname, ulogin, uemail, uphone):
        self.uname = uname + str(rand_string)
        self.ulogin = ulogin + str(number)
        self.uemail = uemail
        self.uphone = uphone + str(number)