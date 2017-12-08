import string

validInput = False
while not validInput:
      plainText = input("What is your text?\n").lower()
      # just "text" OR " "

      problem = False
      
      for letter in plainText:
          if letter not in string.ascii_lowercase and letter != " ":
              problem = True
              print ("ERROR your text invalid")
              print ("=======================")
              break
      if not problem:
            validInput = True
            
validInput = False
while not validInput:
      shift = input("How much do you want to shift\n")
      try:
            shift = int(shift)
            validInput = True
      except ValueError:
            print ("That was not a valid number")
            print ("===========================")

# Main Code
cipherText = ""
for i in plainText:
      asciiNum = chr(ord(i) + int(shift))
      cipherText += asciiNum

print ("""Your code is:
%s""" % (cipherText))
