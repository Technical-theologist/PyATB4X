from abc import ABC, abstractmethod
# Abstraction is hiding the mehtod of the class
#hiding the class by using the abstraction method

class PyATBC(ABC):
    def register(self):
        print("registration is req")
    @abstractmethod
    def course(self):
        pass
class person(PyATBC):
    def course(self):
        print("Amount payed")
amit=person()
amit.course()


class Engine(ABC):
    @abstractmethod
    def gear_box(self):
        pass

    @abstractmethod
    def varient(self):
        pass
class Car(Engine):
    def start(self):
        print("start engine")
    def gear_box(self):
        print("6 gear")
    def varient(self):
        print("V8")

polo=Car()
polo.gear_box()

class excel_reader(ABC):
    @abstractmethod
    def read_from_excel(self):
        pass
class Browser(excel_reader):
    @abstractmethod
    def open_browser(self):
        pass
    def close_browser(self):
        pass
class Test_case(Browser):
    def read_from_excel(self):
       print("read from excel")
    def  open_browser(self):
        print("start browser")
    def close_browser(self):
        print("Close Browser")
    def run_t_c(self):
        self.read_from_excel()
        self.open_browser()
        self.close_browser()
tc1=Test_case()
tc1.run_t_c()

