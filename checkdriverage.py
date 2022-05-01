def checkdriverage(inputage):
    if int(inputage) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(inputage) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(inputage) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")
