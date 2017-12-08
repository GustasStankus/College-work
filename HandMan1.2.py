import random
import string

# ================================= All Def Commands====================================

def HangMan(live):
      if live == 5:
            print ("""
---------------------------
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         | 
|                         |
|                         |
|                         |
|                         |
---------------------------
You have %s lives left""" % (live))
      elif live == 4:
            print ("""
---------------------------
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         | 
|                         |
|                         |
| ===============         |
| ======================  |
---------------------------
You have %s lives left""" % (live))
      elif live == 3:
            print ("""
---------------------------
|                         |
|   +------+              |
|   |      |              |
|   |      |              |
|   |                     |
|   |                     |
|   |                     | 
|   |                     |
|   |                     |
| ===============         |
| ======================  |
---------------------------
You have %s lives left""" % (live))
      elif live == 2:
            print ("""
---------------------------
|                         |
|   +------+              |
|   |      |              |
|   |      |              |
|   |      0              |
|   |                     |
|   |                     | 
|   |                     |
|   |                     |
| ===============         |
| ======================  |
---------------------------
You have %s lives left""" % (live))
      elif live == 1:
            print ("""
---------------------------
|                         |
|   +------+              |
|   |      |              |
|   |      |              |
|   |      0              |
|   |     /|\             |
|   |                     | 
|   |                     |
|   |                     |
| ===============         |
| ======================  |
---------------------------
You have %s lives left""" % (live))
      elif live == 0:
            print ("""
---------------------------
|                         |
|   +------+              |
|   |      |              |
|   |      |              |
|   |      0              |
|   |     /|\             |
|   |     / \             | 
|   |                     |
|   |                     |
| ===============         |
| ======================  |
---------------------------""")
      
def mainGame(changingWord, letterGuess):
      print ("The word that you have to guess %s"  % (" ".join(changingWord)))
      print ("The letters you guess =\n %s" % ("|".join(letterGuess)))
      global live
      HangMan(live)
      userGuess = input("What is your guess\n").upper()
      return userGuess

def putLetterInTheCorretPlace(userGuess, secretWord, changingWord):
    for i in range(len(secretWord)):
        if userGuess == secretWord[i]:
            changingWord[i] = userGuess
    return changingWord

def secretWordInDash(secretWord):
      for i in secretWord:
            changingWord.append("_")
      return changingWord
             
#========================= all the variables and list =================================
with open('ListOfWords.txt', 'r') as f:
    data = f.readlines()
    for word in data:
        listOfWords = word.split()
live = 5                                      
userChose = ""
secretWord = random.choice(listOfWords)
letterGuess = []
changingWord = []
addingWord = True
# =================================== Main Game ===========================================
print ("Wellcome to the HangMan game\n")
#        ----------------------------------------------------------------
#        ----------------- The part of the game wear you ----------------
#        ------------------------add words to the list ------------------
#        ----------------------------------------------------------------
print ("The list of words that you can guess is:\n%s\n" % (" | ".join(listOfWords).title()))
newWord = input("Do you want to add to the list of words or guess the word\n(ADD or GUESS)\n").upper()

while addingWord:
      if newWord == "ADD":
            newWord = input("What word do you want to add\n").upper()
            with open("ListOfWords.txt", "a") as addWord:
                  addWord.write(newWord + " ")
                  break
      elif newWord == "GUESS":
            addingWord = False
      else:
            newWord = input("type in \"Add\" or \"Guess\": ").upper()
#         ------------------------------------------------------------------
#         ------------------ The game statrs hear --------------------------
#         ------------------------------------------------------------------
changingWord = secretWordInDash(secretWord)
while live != 0 and secretWord != "".join(changingWord):
      userGuess = mainGame(changingWord, letterGuess)

      if len(userGuess) == len(secretWord) and userGuess == secretWord:
            changingWord = userGuess

      while userGuess in letterGuess:
            print ("The letter was alredy guessed")
            userGuess = input("===================\nWhat is your guess\n").upper()

      if len(userGuess) < len(secretWord) and len(userGuess) > 1:
            live -= 1

      if userGuess in secretWord:
            print ("Your letter was correct")
            changingWord = putLetterInTheCorretPlace(userGuess, secretWord, changingWord)
            letterGuess.append(userGuess)
      else:
            print("The letter was incorret")
            letterGuess.append(userGuess)
            live -= 1
      print ("==================")
#        ----------------------------------------------------------------     
#        --------------------- Win or Lose code -------------------------
#        ----------------------------------------------------------------
if live == 0:
      HangMan(live)
      print ("You Lose, The word was \"%s\"" % (secretWord).title())
else:
      print ("You Win")





