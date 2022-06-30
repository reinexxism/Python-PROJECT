import random

name = input("What do I call you? : ")
top_of_range = input("Type a number(~100) : ")

# Checking process
if top_of_range.isdigit() :
  top_of_range = int(top_of_range)
  if top_of_range <= 0 :
    print("Please type a number larger than 0 next time")
    quit()
else : 
  print("Please type a number next time")
  quit()

random_num = random.randint(0, top_of_range)
how_many_guess = 0

while True:
  how_many_guess += 1
  user_guess = input("Guess what number is? : ")
  if user_guess.isdigit() :
    user_guess = int(user_guess)
  else : 
    print("Please type a number next time")
    continue

  if user_guess == random_num :
    print("You got it!")
    break
  elif user_guess > random_num :
    print("You were above the number!")
  else :
    print("You were below the number!")

print("{} got it in {} guesses".format(name, how_many_guess))
