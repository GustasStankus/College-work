
def main():
    end = 1
    score = 0
    while end == 1:
        from random import randint

        Rock = u"\u25A0" # 2
        Paper = u"\uFE4F" # 3
        Scissors = u"\u2702" # 1
        comChose = randint(1,3)
        print (comChose)

        # the code starts 
        perChose = int(input(""" You chose first
Scissors = 1
Rock = 2
Paper = 3
\n"""))
        if perChose == 1:
            print ("You chose %s" % (Scissors))
            if perChose == comChose:
                print ("It was Tie. The computer chose %s" % (perChose))
                score = score
            elif comChose == 2:
                print ("You lost. The computer %s" % (Rock))
                score = score
            elif comChose == 3:
                print ("You win. The computer %s" % (Paper))
                score += 1
                
        elif perChose == 2:
            print ("You chose %s" % (Rock))
            if perChose == comChose:
                print ("It was Tie. The computer chose %s" % (perChose))
                score = score
            elif comChose == 3:
                print ("You Win. The computer %s" % (Scissors))
                score += 1
            elif comChose == 1:
                print ("You lost. The computer %s" % (Paper))
                score = score
            
        elif perChose == 3:
            print ("You chose %s" % (Paper))
            if perChose == comChose:
                print ("It was Tie. The computer chose %s" % (perChose))
                score = score
            elif comChose == 3:
                print ("You lost. The computer %s" % (Scissors))
                score = score
            elif comChose == 1:
                print ("You win. The computer %s" % (Rock))
                score = score
        else:
            print ("The number invalid")

        print ("Your score is %s" % (score))
        print ("-----------------------------")
        end = int(input("""Do you want to end
yes = 0
no  = 1
"""))
            
