#Author: David Delatycki, XinYue(Cici) Wang
#Date: 11/18/2020
#Description: an Audio-Visual Language Learning App for Blackfoot

#import a bunch of stuff
import sys
import helper
import replit

high_scores = {"town": 0,"restaurant": 0,"home": 0,"family": 0,"greetings": 0}

current_scene = "town"

#a bunch of predefined long phrases to be used up later
intro = "Oki(Hello)! Welcome to Brocket, Alberta! I can teach you some Blackfoot while you are here!"

available_features = "Do you want to learn some words around you(learn),\nperform speech synthesis(speech),\nhave me test you(test), see your high scores(score), \ngo somewhere else(move), or leave(exit)? "




#display town scene as initial scene
helper.show_scene(current_scene)

print(intro)

#set a control varible for the while loop
user_continue = True

while user_continue:
  # get user response
  response = input(available_features).lower().strip("!?,. ")
  replit.clear()

  if response == "learn":
    learn_counter = 0
    helper.learn(current_scene,learn_counter)

  elif response == "speech":
    helper.speech()

  elif response == "test":
    test_score = helper.test(current_scene)
    high_scores = helper.set_high_score(current_scene, test_score, high_scores)
    
  elif response == "move":
    new_scene = helper.move()
    helper.show_scene(new_scene)
    current_scene = new_scene

  elif response == "score":
    helper.show_high_score(high_scores)

  elif response == "exit":
    user_continue = False
  
  else:
    print("Sorry, I am unable to understand " + response)

sys.exit()

