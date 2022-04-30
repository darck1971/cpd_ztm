from dobcheck import dobcheck
from driving import driving
from listslicer import listslicer
from passwordchecker import passwordchecker
from picture import picture

while True:
  program_choice = input("""Please choose which program you want to run:\n 
    1. Date of Birth  
    2. Driving  
    3. List Slicer  
    4. Password Checker  
    5. Picture
    0. Exit Program 
\n""")
  
  #This is horrible code I know. Python doesn't have case/switch statements (uses match) until 3.10. Replit currently uses 3.08 - I've done it this way and included the way it should be done in comments
  if program_choice == "1":
    dobcheck()
  elif program_choice == "2":
    driving()
  elif program_choice == "3":
    listslicer()
  elif program_choice == "4":
    passwordchecker()
  elif program_choice == "5":
    picture()
  elif program_choice == "0":
    break
  else:
      print("Invalid choice")

#Using a multiline string to comment out this code. Python will look at this as a string but since it's not assigned to anything it will ignore it
"""
match program_choice:
  case "1":
    dobcheck()
  case "2":
    driving()
  case "3":
    listslicer()
  case "4":
    passwordchecker()
  case "5":
    picture()
  case "0":
    break
  case _:
    print "Invalid choice"
"""