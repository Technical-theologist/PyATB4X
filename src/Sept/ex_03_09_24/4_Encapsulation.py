class Myclass:
    # public var
    public_var = "I am public"  # public instance var


obj = Myclass()
print(obj.public_var)


class Myaccount:
    name = "kar"
    _ac_detail = "1234567890"  # Protected var
    __password = "1234"  # private var
    def ac(self):
       print(self.__password)

ac_holder = Myaccount()
print(ac_holder._ac_detail)
print(ac_holder.ac())


class Bank:
    def __init__(self, account_no, balence):
        self.balence = balence
        self.__account_no = account_no

    def deposite(self,amount):
        self.balence = self.balence+amount

    def check_balenece(self):
        print(self.balence)

    def show_acount_no(self, is_auth):
        if is_auth == True:
            print(self.__account_no)
        else:
            print("Not allowed")
    def __internal_method(self):
        print("private method")
        print(self.__account_no)


sbi = Bank(987124,25000)
sbi.show_acount_no(True)
sbi.deposite(200)
sbi.check_balenece()
# sbi.__internal_method() This is a private method
