# Helper functions for Blackfoot project
# CMPT 120
# Nov. 12, 2020
import wave
import random
import cmpt120image
import replit
# import os
from replit import audio
from time import sleep


def concat(infiles, outfile):
    """
  Input: 
  - infiles: a list containing the filenames of .wav files to concatenate,
    e.g. ["hello.wav","there.wav"]
  - outfile: name of the file to write the concatenated .wav file to,
    e.g. "hellothere.wav"
  Output: None
  """
    data = []
    for infile in infiles:
        w = wave.open(infile, 'rb')
        data.append([w.getparams(), w.readframes(w.getnframes())])
        w.close()
    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])
    output.close()


#Author: David Delatycki, XinYue(Cici) Wang
#Date: 11/28/2020
#Description: below are our defined functions to be used in the program


#learn function
def learn(scene_name,learn_time):
  learn_first_time_intro = "Great, let's learn! Look around here and tell me a word in English.\nWhat do you want to learn the Blackfoot word for? Type it in English, or type done to finish. "
  learn_intro = "What do you want to learn the Blackfoot word for? "

  translations = open("translation.csv")
  scene_words = {}

  for line in translations:
    data = line.split(",")
    if data[0] == scene_name:
      scene_words[data[1]] = data[2].replace('\n', '')
     
  keep_learning = True

  while keep_learning:
    if learn_time == 0:
      eng_input = input(learn_first_time_intro + learn_intro).lower().strip("!?,. ")
      learn_time += 1
    else:
      eng_input = input(learn_intro).lower().strip("!?,. ")


    valid_word = False

    for key, value in scene_words.items():
      if eng_input == key:
        valid_word = True
        bf_output = value
        print(bf_output)
        audio.play_file("sounds/" + key + ".wav")
        sleep(3)
      elif eng_input == "done":
        replit.clear()
        keep_learning = False

    if valid_word:
      replit.clear()
      return learn(scene_name,learn_time)
    elif not valid_word and keep_learning:
      print("Sorry, I don't know that one. Try another word!")
      sleep(2)
      replit.clear()


#speech synthesis function
def speech():
  speech_intro = "Create your sentence using words we have learnt so far!\n\n" 
  #speech_help = "1.1. Time words: Yesterday/Today/Tomorrow/This morning/This evening\n1.2. Question: Who/Where 2. Verbs: I went/I will eat/I will go\n3. Misc words: Please pass the/and"
  # speech_intruction = "Use '+' sign to separate valid words, no space between '+' signs.\nEg. Today+I will eat+oranges\nType 'done' to go back to main menu\n"

  translations = open("translation.csv")
  available_words = []

  for line in translations:
    data = line.split(",")
    available_words.append(data[1])

  keep_creating_sentences = True


  while keep_creating_sentences:
    # print(speech_intro + speech_help + speech_intruction)
    print(speech_intro)
    user_speech = input("Now try creating a sentence yourself! ").lower().strip("!@,.? ").split("+")

    if user_speech == "done":
      replit.clear()
      keep_creating_sentences = False


    valid_sentence = False
    valid_words = 0
    
    for words in user_speech:
      if words in available_words:
        valid_words += 1

    if valid_words == len(user_speech):
        valid_sentence = True


    if valid_sentence:
      print("wuhu")
      outfile = ''
      for i in range(len(user_speech)):
        outfile += user_speech[i]
      outfile += '.wav'

      infiles = []
      for word in user_speech:
        word += '.wav'
        new_word = 'sounds/' + word
        infiles.append(new_word)

      concat(infiles, outfile)
      audio.play_file(outfile)
      # os.remove(outfile)

    elif (not valid_sentence and keep_creating_sentences) or (not valid_words):
      print("Sorry, not valid sentense")
      #sleep(2)
      #replit.clear()




# main test function 
def test(scene_name):
    test_features = "Would you like a (fill-in) the blanks test or a (multiple-choice) test? "

    translations = open("translation.csv")
   
    scene_words = {}

    for line in translations:
        data = line.split(",")
        if data[0] == scene_name:
            
            scene_words[data[1]] = data[2].replace('\n', '')

    keep_asking = True

    while keep_asking:
        choice = input(test_features).lower().strip("!?,. ")

        if choice == "fill-in":
            return fill_in_test(scene_name, scene_words)
        elif choice == "multiple-choice":
            return mc_test(scene_name, scene_words)
        else:
            print("Sorry, I don't know that one. Try another option!")


# fill in the blanks test
def fill_in_test(scene_name, scene_words):
    score = 0
    for x in range(10):
      random_word = random.choice(list(scene_words))
      audio.play_file("sounds/" + random_word + ".wav")
      choice = input("What is " + scene_words[random_word] + "? ").lower().strip("!?,. ")
      
      if choice ==  random_word:
        print("Good Job!")
        score += 1
      else:
        print("Nope! it's", random_word)
    
    input("You got " + str(score) + "/10 right! Press <enter> ")
    return score


# multiple choice test
def mc_test(scene_name, scene_words):
    score = 0
    for x in range(10):
      sample = random.sample(list(scene_words), 3)
      random_word = random.choice(sample)
      audio.play_file("sounds/" + random_word + ".wav")
      print("What is " + scene_words[random_word] + "? ")
      print(" - ", sample[0])
      print(" - ", sample[1])
      print(" - ", sample[2])
      choice = input().lower().strip("!?,. ")
      if choice ==  random_word:
        print("Good Job!")
        score += 1
      else:
        print("Nope! it's", random_word)
    
    input("You got " + str(score) + "/10 right! Press <enter> ")
    return score


# set high score
def set_high_score(scene, score, high_scores):
  new_high_scores = high_scores
  for key, value in high_scores.items():
    if scene == key:
      if score > new_high_scores[key]:
        new_high_scores[key] = score
        print("New High Score!")
  return new_high_scores


# show high score
def show_high_score(high_scores):
  print("Your current high scores")
  for key, value in high_scores.items():
    print(key.capitalize(),": ",str(value),"/10", sep='')
    

# main test function 
def move():
    move_features = "Where do you want to go (Town/Restaurant/Home/Family/Greetings)? "
    keep_asking = True
    while keep_asking:
        choice = input(move_features).lower().strip("!?,. ")

        if choice == "town" or choice == "restaurant" or choice == "home" or choice == "family" or choice == "greetings":
            return choice
        else:
            print("Sorry, I don't know that one. Try another scene!")


# shows a scene
def show_scene(scene):
  display_scene = cmpt120image.getImage("images/" + scene + ".png")
  cmpt120image.showImage(display_scene, "Let's Learn BlackFoot!")

