def yoda():
    print ("""
                    |========================|
                    |  Good, Day Hmmmm Have  |
                    |========================|
                     \        ____
                       \    _.' :  `._
                        .-.'`.  ;   .'`.-.
               __      / : ___ ;  /___ ;        __
             ,'_ ""--.:__;".-.";: :".-.":__;.--"" _`,
             :' `.t""--.. '<@.`;_  ',@>` ..--""j.' `;
                  `:-.._J '-.-'L__ `-- ' L_..-;'
                    "-.__ ;  .-"  "-.  : __.-"
                        L ' /.------. ' J
                         "-.   "--"   .-"
                        __.l"-:_JL_;-";.__
                     .-j/'.;  ;       / .'"-.
                   .' /:`. "-.:     .-" .';  `.
                .-"  / ;  "-. "-..-" .-"  :    "-.
             .+"-.  : :      "-.__.-"      ;-._
          
""")

def main():
    from random import randint
    end = 0
    while end == 0:
        line = (input("""Type the sentence that you want to be translated to Yoda
|==============|
| ? = question |
| ! = statement|
| . = regular  |
|==============|
""")).lower()
        live = randint(1, 10)
        newLine = line.split()
        newNewLine = line

        if live == 5:
            print ("Yoda is confused?")
            print (yoda())
            exit()
        
        elif 'not' in newLine:
            if len(newLine) == 3:
                newLine.remove("not")
                u = ' '.join(newLine[1:]).rstrip('!?.')
                print ('%s, %s... %s' % (u[0].upper() + u[1:],
                                            ['I', newLine[0].lower()][newLine[0] != 'I'],
                                            "Hmmm... Not"))
            elif len(newLine) == 2:
                newLine.remove("not")
                u = ' '.join(newLine[0:]).rstrip('!?.')
                print ('%s... %s' % (u[0:].upper(), "Hmmm... Not"))

            elif len(newLine) == 1:
                print ("Hmmm Not")
                
            else:
                newLine.remove("not")
                u = ' '.join(newLine[2:]).rstrip('!?.')
                print ('%s, %s %s... %s...' % (u[0].upper() + u[1:],
                                ['I', newLine[0].lower()][newLine[0] != 'I'],
                                newLine[1], "Hmmmm... Not"))
                
        elif 'can\'t' in newLine:
            if len(newLine) == 3:
                newLine.remove("can\'t")
                u = ' '.join(newLine[1:]).rstrip('!?.')
                print ('%s, %s... %s' % (u[0].upper() + u[1:],
                                            ['I', newLine[0].lower()][newLine[0] != 'I'],
                                            "Can not"))
            elif len(newLine) == 2:
                newLine.remove("can\'t")
                u = ' '.join(newLine[0:]).rstrip('!?.')
                print ('%s... %s' % (u[0:].upper(), "Can Not"))

            elif len(newLine) == 1:
                print ("Can Not")
                
            else:
                newLine.remove("can\'t")
                u = ' '.join(newLine[2:]).rstrip('!?.')
                print ('%s, %s %s... %s...' % (u[0].upper() + u[1:],
                                ['I', newLine[0].lower()][newLine[0] != 'I'],
                                newLine[1], "Can not"))
        elif "?" in newNewLine:
            if len(newLine) == 3:
                u = ' '.join(newLine[2:]).rstrip('!?.')
                print ('%s, %s... %s' % (u[0].upper() + u[1:],
                                            ['I', newLine[0].lower()][newLine[0] != 'I'],
                                            "Hmmm"))
            elif len(newLine) == 2:
                u = ' '.join(newLine[0:]).rstrip('!?.')
                print ('%s... %s' % (u[0:].upper(), "Hmmm"))

            elif len(newLine) == 1:
                print (newLine)
                
            else:
                u = ' '.join(newLine[2:]).rstrip('!?.')
                print ('%s, %s %s... %s...' % (u[0].upper() + u[1:],
                                ['I', newLine[0].lower()][newLine[0] != 'I'],
                                newLine[1], "Hmmmmm"))
                
        elif "!" in newNewLine:
            if len(newLine) == 3:
                u = ' '.join(newLine[1:]).rstrip('!?.')
                print ('%s, %s... %s' % (u[0].upper() + u[1:],
                                            ['I', newLine[0].lower()][newLine[0] != 'I'],
                                            "Yes"))
            elif len(newLine) == 2:
                u = ' '.join(newLine[0:]).rstrip('!?.')
                print ('%s... %s' % (u[0:].upper(), "Yes"))

            elif len(newLine) == 1:
                print (newLine)
                
            else:
                u = ' '.join(newLine[2:]).rstrip('!?.')
                print ('%s, %s %s... %s...' % (u[0].upper() + u[1:],
                                ['I', newLine[0].lower()][newLine[0] != 'I'],
                                newLine[1], "Yes"))
        elif len(newLine) == 3:
            u = ' '.join(newLine[2:]).rstrip('!?.')
            print ('%s, %s %s... %s...' % (u[0].upper() + u[1:],
                                ['I', newLine[0].lower()][newLine[0] != 'I'],
                                newLine[1], "Hmmm... Yes"))
        else:
            print (' '.join(newLine).rstrip('!?.'))
            

        print ("-----------------------------")
        end = int(input(""" Do you want to end the program
|=======|
|yes = 1|
|no  = 0|
|=======|
"""))
        if end == 1:
            yoda()
        
