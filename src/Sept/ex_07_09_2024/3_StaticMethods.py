# A static method is a method belong to class
# rather than instace of the class
#   *Static method can be called directly without the object
# This is generally what u do
class math_opr:
    def div(self, a, b):
        return a / b

    def add(self, a, b):
        return a + b


object_ref = math_opr()
output = object_ref.div(10, 5)
output_1 = object_ref.add(10, 5)
print(output)
print(output_1)


# This is static method
class math_opr:
    def div(self, a, b):
        return a / b

    @staticmethod
    def add(a, b):
        return a + b


# Non static obj is mandatory
object_ref = math_opr()
output = object_ref.div(10, 5)
print(output)
##no need of the object if you take static method
print(math_opr.div(0, 10, 5))
print(math_opr.add(10, 5))


class Read_from_excel:
    @staticmethod
    def read_excel():
        print("read from excel")

class TC:
    def test_Case(self):
        Read_from_excel.read_excel()

tc = TC()
tc.test_Case()

