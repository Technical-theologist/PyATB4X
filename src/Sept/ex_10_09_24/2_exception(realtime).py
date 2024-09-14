import os
try:
    full_path=os.getcwd()
    print(full_path)
    file_path=full_path+"/text.txt"
    file=open(file_path,'r')
    print(file.read())
except FileNotFoundError as fnf:
    print("Provide proper file")
finally:print("Executed properly")
