def driving():
  age = 17
  old_enough = (age >= 17)
  have_license = True

  if not old_enough:
    print ("You are too young to drive")
  elif have_license:
    print("You can drive")
  else:
    print("You can't drive")