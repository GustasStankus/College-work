import string

def code():
      validInput = False
      while not validInput:
            plainText = input("What is your text?\n").lower()
      # just "text" OR " "

            problem = False
            for letter in plainText:
                if letter not in string.printable:
                    problem = True
                    print ("ERROR your text invalid")
                    print ("=======================")
                    break
            if not problem:
                  validInput = True
            
      # Code For Shift           
      validInput = False
      while not validInput:
            shift = input("How much do you want to shift\n")
            try:
                  shift = int(shift)
                  if shift > 26:
                        shift = shift % 26
                  validInput = True
            except ValueError:
                  print ("That was not a valid number")
                  print ("===========================")
            
      
      # Main Code
      cipherText = ""
      for i in plainText:
            asciiNumRep = ord(i) + int(shift)
            if i != " ":
                  while  asciiNumRep > 122:
                        asciiNumRep -= 26
                  while asciiNumRep < 97:
                        asciiNumRep += 26
                  cipherText += chr(asciiNumRep)
                  
            elif i == " " or "," or "." or "!" or "?" or "-":
                  cipherText += i

      

      print ("""Your code is:
%s""" % (cipherText))

def decode():
      validInput = False
      while not validInput:
            plainText = input("What is your text?\n").lower()
      # just "text" OR " "

            problem = False
            for letter in plainText:
                if letter not in string.printable:
                    problem = True
                    print ("ERROR your text invalid")
                    print ("=======================")
                    break
            if not problem:
                  validInput = True

      # Decode the text
      cipherText = ""
      plainText2 = []
      end = 0
      while end != 10:
            for x in range(1,26):
                  for i in plainText:
                        if i != " ":
                              newText = chr(ord(i) + x)
                              cipherText += newText
                              
                        else:
                              cipherText += i

                        plainText2.append(cipherText)
        
                        print (plainText2)
            end += 1
decode()
