
        
def main():
    from random import randint 
    end = 1
    rand = randint(6,15)
    while end != 0:
        print("""
|---|---|---|---|
| 0 |       | ! |
|   |   |   |   |
|       |   |   |
|   |   |---|   |
|   |           |
|---|---|---|---|
0 = you""") # starting point

        num1 = input("""
|=============|
|hi = "Hello" |
|print hi     |
|=============|
What will be printed out?
""")
        if num1 == "Hello":
            print ("===============")
            print ("You are correct")
            def move1():
                move = input("Which way do you want to move?\ndown, up, left or right\n").lower()
                if move == "down":
                    print ("""
|---|---|---|---|
|   |       | ! |
|===|   |   |   |
| 0     |   |   |
|   |   |---|   |
|   |           |
|---|---|---|---|""")
                else:
                    print ("==========================")
                    print ("You can not move that way")
                    print ("==========================")
                    move1()
            move1()
        else:
            print("The answer is incorrect")
            print("=======================")
            print("You Game now got reset")
            main()
            
# move 2
        
        num1 = input("""
|=========================================|
|user = int(input("What is your number")) |
|if user > 5:                             |
|    print("The number is bigger than 5") |
|elif user < 5:                           |
|    print("The number is smaller than 5")|
|=========================================|
What will be printed out if the user puts in %s?
""" % (rand))
        if num1 == "The number is bigger than 5" or "The number is bigger than 5 ":
            print ("===============")
            print ("You are correct")
            def move2():
                move = input("Which way do you want to move?\ndown, up, left or right\n").lower()
                if move == "down":
                    print ("""
|---|---|---|---|
|   |       | ! |
|===|   |   |   |
|       |   |   |
|===|   |---|   |
| 0 |           |
|---|---|---|---|
    Game Over""")
                    end = 0
                    exit()
                elif move == "right":
                    print("""
|---|---|---|---|
|   |       | ! |
|===|   |   |   |
|   | 0 |   |   |
|   |   |---|   |
|   |           |
|---|---|---|---|""")
                else:
                    print ("==========================")
                    print ("You can not move that way ")
                    print ("==========================")
                    move2()
            move2()
        else:
            print("The answer is incorrect")
            print("=======================")
            print("You Game now got reset")
            main()
# move 3
        num1 = input("""
|======================|
|word = "Hello World"  |
|print (word.find("e"))|
|======================|
What will be printed out?
""")
        def move3():
            print ("""
|---|---|---|---|
|   | 0     | ! |
|===|===|   |   |
|   |   |   |   |
|   |   |---|   |
|   |           |
|---|---|---|---|
""")
        def move4():
            print ("""
|---|---|---|---|
|   |       | ! |
|===|   |   |   |
|   |   |   |   |
|   |===|---|   |
|   | 0         |
|---|---|---|---|
""")
        if num1 == "1":
            print ("===============")
            print ("You are correct")
            move = input("Which way do you want to move?\n down, up, left or right\n").lower()
            if move == "up":
                new = 1
                move3()
            elif move == "down":
                new = 0
                move4()
            else:
                move5 = 1
                while move5 == 1:
                    print ("=========================")
                    print ("You can not move that way")
                    print ("=========================")
                    move = input("Which way do you want to move?\ndown, up, left or right\n").lower()
                    if move == "up":
                        new = 1
                        move5 = 0
                        move3()
                    elif move == "down":
                        new = 0
                        move5 = 0
                        move4()
                
        else:
            print("The answer is incorrect")
            print("=======================")
            print("You Game now got reset")
            main()

# move 4
        num1 = input("""
|============================================|
|word1 = "Good"                              |
|word2 = "Morning"                           |
|word3 = "to you!"                           |
|sentence = word1 + " " + word2 + " " +word3 |
|print sentence                              |
|============================================|
What will be printed out?
""")
        if num1 == "Good Morning to you!":
            print ("===============")
            print ("You are correct")

            def move6():
                move = input("Which way do you want to move?\ndown, up, left or right\n").lower()
                if move == "right":
                    print ("""
|---|---|---|---|
|   |   | 0 | ! |
|===|===|   |   |
|   |   |   |   |
|   |   |---|   |
|   |           |
|---|---|---|---|
""")
                elif move == "right" and new == 0:
                    print ("""
|---|---|---|---|
|   |       | ! |
|===|   |   |   |
|   |   |   |   |
|   |===|---|   |
|   |   | 0     |
|---|---|---|---|
""")
                else:
                    print ("==========================")
                    print ("You can not move that way ")
                    print ("==========================")
                    move6()
            move6()
            
        else:
            print("The answer is incorrect")
            print("=======================")
            print("You Game now got reset")
            main()

# move 5
    
        num1 = input("""
|=====================================|
|name = input('What is your name?\n') |
|print ("Hi, %s." % (name))           |
|=====================================|
The user puts in Bob
What will be printed out?
""")
        if num1 == "Hi, Bob.":
            print ("===============")
            print ("You are correct")

            def move7():
                move = input("Which way do you want to move?\ndown, up, left or right\n").lower()
                if move == "down" and new == 1:
                    print ("""
|---|---|---|---|
|   |   |   | ! |
|===|===|===|   |
|   |   | 0 |   |
|   |   |---|   |
|   |           |
|---|---|---|---|
    Game Over""")
                    
                    exit()
                if move == "right" and new == 0:
                    print ("""
|---|---|---|---|
|   |       | ! |
|===|   |   |   |
|   |   |   |   |
|   |===|---|   |
|   |   |   | 0 |
|---|---|---|---|
""")
                else:
                    print ("==========================")
                    print ("You can not move that way ")
                    print ("==========================")
                    move7()
            move7()
        else:
            print("The answer is incorrect")
            print("=======================")
            print("You Game now got reset")
            main()
# move 6
        num1 = input("""
=============
num = 25 
num_sqrt = num ** 0.5
print('%s' % (num_sqrt))
=============
What will be printed out?
""")
        if num1 == "5":
            print ("You are correct")
            def move8():
                move = input("Which way do you want to move?\n down, up, left or right\n").lower()
                if move == "up":
                    print ("""
|---|---|---|---|
|   |       | ! |
|===|   |   |   |
|   |   |   | 0 |
|   |===|---|===|
|   |   |   |   |
|---|---|---|---|
""")
                else:
                    print ("==========================")
                    print ("You can not move that way\n")
                    print ("==========================")
                    move8()
            move8()
        else:
            print("The answer is incorrect")
            print("=======================")
            print("You Game now got reset")
            main()
# muve 7
        num1 = input("""
|===============|
|def cube(x):   |
|    return x**3|
|===============|
That do you need to type into the
program to get 8
""")
        if num1 == "cube(2)":
            print ("===============")
            print ("You are correct")
            def move9():
                move = input("Which way do you want to move?\n down, up, left or right\n").lower()
                if move == "up":
                    print ("""
|---|---|---|---|
|   |       | 0 |
|===|   |   |===|
|   |   |   |   |
|   |===|---|===|
|   |   |   |   |
|---|---|---|---|
""")
                else:
                    print ("==========================")
                    print ("You can not move that way\n")
                    print ("==========================")
                    move9()
            move9()
            end = 0
        else:
            print("The answer is incorrect")
            print("=======================")
            print("You Game now got reset")
            main()
            end = 0

start = input("            Hello and Welcome to the Py-Maze")
if start == "":
    start = input("This is a game that will teach you the bigging of Python")
    if start == "":
        print ("                  Okay lets start")
        main()
