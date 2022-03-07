import random
from game_data import data
from replit import clear
from art import logo,vs

def format_data(account):
  """Takes the account data and returns the printable format."""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  """Take the user guess and follower counts and returns if they got it right."""
  return guess == "a" if a_followers > b_followers else guess == "b"

print(logo)
score = 0
game_should_continue = False
account_b = random.choice(data)

while not game_should_continue:

  account_a = account_b
  account_b = random.choice(data)

  while account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")


  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]

  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  clear()
  print(logo)

  if is_correct:
    score += 1
    print(f"Youre right! Current score: {score}")
  else:
    game_should_continue = True
    print(f"Sorry, tha's wrong. Final score: {score}")

