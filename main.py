import random 
from art import logo 
from replit import clear

#print(logo)

###### BLACKJACK GAME ######

#below are the set of cards and function that randomly chooses a card
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
  return random.choice(cards)


# users and computers list of cards
user_cards = []
computer_cards = []

user_cards.append(deal_card())
user_cards.append(deal_card())
computer_cards.append(deal_card())
computer_cards.append(deal_card())


# function that calculates the sum of the users or computers cards
def calculate_score(list_of_cards):
  if len(list_of_cards) == 2:
    if sum(list_of_cards) == 21:
      return 0
  for i in list_of_cards:
    if i == 11 and sum(list_of_cards) > 21:
      return sum(list_of_cards) - 10
  return sum(list_of_cards)
   
print(user_cards)
print(calculate_score(user_cards))


# loop that checks users score
run = True
while run:
  if calculate_score(user_cards) == 0 or calculate_score(user_cards) == 21:
    clear()
    print(logo)
    print(f"Congratulations you have won with {calculate_score(user_cards)} points")
    run = False
  elif calculate_score(user_cards) < 21:
    next_card = input("Do you want to draw another card? Type 'yes' or 'no'")
    if next_card == "yes":
      user_cards.append(deal_card())
      clear()
      print(logo)
      print(user_cards)
      print(calculate_score(user_cards))
    elif next_card == "no":
      run = False 
  elif calculate_score(user_cards) > 21:
    clear()
    print(logo)
    print(user_cards)
    print("You have lost")
    run = False


# loop that checks computers score
run_comp = True 
while run_comp:
  if calculate_score(computer_cards) < 17:
    computer_cards.append(deal_card())
  elif calculate_score(computer_cards) == 21:
    run_comp = False
  else:
    run_comp = False


# below are print statements on the console 
user = calculate_score(user_cards)
computer = calculate_score(computer_cards)

clear()
#print(logo)
print(user_cards)
print(f"User score is: {user}")
print(computer_cards)
print(f"Computer score is: {computer}")


# function that checks who won the game, user or computer
def compare(user_score, computer_score):
  if user_score == computer_score:
    print("It's a draw!")
  elif computer_score == 0:
    print("Computer has a BlackJack. Computer wins!")
  elif user_score == 0:
    print("User has a BlackJack. User wins!")
  elif user_score > 21:
    print("Computer wins")
  elif computer_score > 21:
   print("User wins!")
  elif user_score > computer_score:
    print("User wins!")
  else:
    print("Computer wins!")


# function collout 
print()
compare(user, computer)

#