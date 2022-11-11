while True:
  import random
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  print("Welcome to the MyPassword Generator!")
  nr_letters= int(input("How many letters would you like in your password?\n")) 
  nr_symbols = int(input(f"How many symbols would you like?\n"))
  nr_numbers = int(input(f"How many numbers would you like?\n"))

  for letter in letters:
    ranLetters = random.choices(letters, k=nr_letters)
   
  for symbol in symbols:
    ranSymbols = random.choices(symbols, k=nr_symbols)

  for number in numbers:
    ranNumbers = random.choices(numbers, k=nr_numbers)

# mergedPassList joins the letters symbols and numbers into one list.
  mergedPassList = ranLetters + ranSymbols + ranNumbers
#lets the user see the characters that will be used to create their final password
# while loop below allows user to restart program if they dont like the randomly selected set of characters
  while True:
    acceptData = input(f'Your password will be generated from the following:{mergedPassList}. To use these randomly selected characters, type "accept". To decline and select new random characters, type anything else: ').lower()

    if acceptData != "accept":
      break
    else:
      easyOrHard = input("Do you want an easy or hard password?: ")

      easy_or_hard = easyOrHard.lower()

      if easy_or_hard != "easy" and easy_or_hard != "hard":
        print('Please type either "easy" or "hard".')
      elif easy_or_hard == "easy":
        easyPassword = ''.join(mergedPassList)
        print(f"Your password is: {easyPassword} ")
      elif easy_or_hard == "hard":
        random.shuffle(mergedPassList) #you cannot save this as = to a variable, it will return none.
        finalPassword = ''.join(mergedPassList)
        print(f"Your password is: {finalPassword} ")
