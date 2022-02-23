import random
# Random Number Guesser Game
# Pick a random number within a range and have the user try to guess it.

the_number = random.randint(1,200)

print("Welcome to the Random Number Guess Game")
print("The number is between 1 and 200")
user_guess = input("Guess the number ")

while user_guess != the_number:
  user_guess = input("Guess the number ")
  if user_guess.isalpha():
    user_guess = int(user_guess)
    if user_guess < the_number:
        print("It's too low")
    if user_guess > the_number:
        print("It's too high")
      
  else:
    print("That's not a number, please try again!")
    user_guess = input("Guess the number ")
    

over = False


#input should only be a number




print("You Win")
    





