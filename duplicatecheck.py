def duplicatecheck():
  some_list = ['a','b','c','b','d','m','n','n']
  dup_list = []
  
  for letter in some_list:
    letter_count = some_list.count(letter)
    if letter_count > 1:
      dup_list.append(letter)
      if dup_list.count(letter) == 1:
        print(f"{letter} has {letter_count} instances")