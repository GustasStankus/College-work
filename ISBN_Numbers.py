end = ("no")
while end == ("no"):
    chose = int(input(""" Do you want to check the ISBN number?
Or do you want to calculate the last number of the ISBN?
|-------------|
|Check     = 1|
|Calculate = 0|
|-------------|
"""))
    if chose == 1:
        numList = str(input("What is your ISBN number\n"))
    
        if len(numList) == 10:
            addNum10 = (int(int(numList[0])*10 + int(numList[1])*9 + int(numList[2])*8
                        + int(numList[3])*7 + int(numList[4])*6 + int(numList[5])*5
                        + int(numList[6])*4 + int(numList[7])*3 + int(numList[8])*2))
        
            divNum10 = int(addNum10) % 11
            lastNum10 = 11 - int(divNum10)
            
            if lastNum10 == 11 and numList[9] == "x":
                lastNum10 = "x"           
            elif lastNum10 == 10 and numList[9] == "x":
                lastNum10 = "x"
            elif int(lastNum10 == 11 and numList[9]) == 0:
                lastNum10 = 0           
            elif int(lastNum10 == 10 and numList[9]) == 0:
                lastNum10 = 0
                print (lastNum10)
                
            if str(lastNum10) == str(numList[9]):
                print ("The ISBN number is valid")
            else:
                print ("The ISBN number is invalid")
                
        elif len(numList) == 13:
            addNum13 = (int(int(numList[0])*1 + int(numList[1])*3 + int(numList[2])*1
                        + int(numList[3])*3 + int(numList[4])*1 + int(numList[5])*3
                        + int(numList[6])*1 + int(numList[7])*3 + int(numList[8])*1
                        + int(numList[9])*3 + int(numList[10])*1 + int(numList[11])*3))

            divNum13 = int(addNum13) % 10
            lastNum13 = 10 - int(divNum13)
            lastNum13 = int(lastNum13)
            num = int(numList[12])
            
            if lastNum13 == 10 and numList[12] == "x":       
                lastNum13 = "x"
            elif lastNum13 == 10 and numList[12] == 0:       
                lastNum13 = 0
                
            if lastNum13 == num:
                print ("The ISBN number is valid")

            elif lastNum13 != num:
                print ("The ISBN number is invalid")
        elif (numList != 10) or (numList != 13):
            print ("The ISBN number is invalid")
            break

        end = input("""Do you want to end the program
    (yes or no)\n""")
        print ("--------------------------------------")
    elif chose == 0:
        numList = str(input("What is your ISBN number\n"))
        
        if len(numList) == 9:
            addNum10 = (int(int(numList[0])*10 + int(numList[1])*9 + int(numList[2])*8
                        + int(numList[3])*7 + int(numList[4])*6 + int(numList[5])*5
                        + int(numList[6])*4 + int(numList[7])*3 + int(numList[8])*2))
            
            divNum10 = int(addNum10) % 11
            lastNum10 = 11 - int(divNum10)
            print ("The last number of the ISBN number is %s" % (lastNum10))

        elif len(numList) == 12:
            addNum13 = (int(int(numList[0])*1 + int(numList[1])*3 + int(numList[2])*1
                        + int(numList[3])*3 + int(numList[4])*1 + int(numList[5])*3
                        + int(numList[6])*1 + int(numList[7])*3 + int(numList[8])*1
                        + int(numList[9])*3 + int(numList[10])*1 + int(numList[11])*3))

            divNum13 = int(addNum13) % 10
            lastNum13 = 10 - int(divNum13)
            print ("The last number of the ISBN number is %s" % (lastNum13))
        end = input("""Do you want to end the program
    (yes or no)\n""")
        print ("--------------------------------------")
            
