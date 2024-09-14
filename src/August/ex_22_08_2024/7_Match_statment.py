#Match statment is similar to switch in java
#match the op and execute the code

#Write a program to the user whcih browser he want to run automation
browser=input("Enter the name of the browser")
browser=browser.lower()
match browser:
    case "chrome":#match the browser with the case
        print("Running automation in chrome")
    case "firefox":
        print("Running automation in firefox")
    case "edge":
        print("Running automation in edge")
    case _:
    #default case
        print("Invalid browser")
person=input("Enter the person position")
person=person.lower()
match person:
    case "admin""architecture":
        print("You have full access")
    case "Manager":
        print("System level access")
    case "engineer":
        print("You have partial access")
    case _: #Default case
        print("No access")