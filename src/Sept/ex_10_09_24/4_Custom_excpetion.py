class Balence_low_exception:
    def __init__(self,message):
        self.message=message
        super.__init__(message)
balence=100
withdraw=int(input("Enter the amount"))
if balence<withdraw:
    raise (Balence_low_exception)
else:
    print("Remainign the amount",balence-withdraw)

