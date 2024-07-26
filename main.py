import random
from game_data import data
from art import logo, vs
def game():
  print(logo)
  score = 0
  gameContinue = True
  while gameContinue:
    celebrity1 = random.choice(data)
    celebrity2 = random.choice(data)
    while celebrity1 == celebrity2:
      celebrity2 = random.choice(data)
    
    celebrity_name1 = celebrity1["name"]
    celebrity_follower1 = celebrity1["follower_count"]
    celebrity_description1 = celebrity1["description"]
    celebrity_country1 = celebrity1["country"]
    print(f"Compare A: {celebrity_name1}, a {celebrity_description1}, from {celebrity_country1}")
    print(vs)
    
    celebrity_name2 = celebrity2["name"]
    celebrity_follower2 = celebrity2["follower_count"]
    celebrity_de2 = celebrity2["description"]
    celebrity_country2 = celebrity2["country"]
    print(f"Compare B: {celebrity_name2}, a {celebrity_de2},from {celebrity_country2}")
    
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_choice == "a":
      if celebrity_follower1 > celebrity_follower2:
        score += 1
        clear()
        print(logo)
        print(f"You're right! Current score: {score}")
      else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        gameContinue = False
    elif user_choice == "b":
      if celebrity_follower2 > celebrity_follower1:
        score += 1
        clear()
        print(logo)
        print(f"You're right! Current score: {score}")
      else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        gameContinue = False
    elif user_choice == "exit":
      print("Thanks for playing!")
      gameContinue = False
    else:
      clear()
      print("Invalid input, Enter A or B")
      print(logo)
game()