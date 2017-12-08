one = 31
two = 30
months = ["January", "Febuary", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

x = [1, 3, 5, 7, 9, 11]
y = [4, 6, 8, 10, 12]
z = [2]

while True:
    month = int(input("""What month do you want to see?
|----------------|
| January  == 1  |
| Febuary  == 2  |
| March    == 3  |
| April    == 4  |
| May      == 5  |
| June     == 6  |
| July     == 7  |
| August   == 8  |
| September== 9  |
| October  == 10 |
| November == 11 |
| December == 12 |
|----------------|\n"""))
    if month in x:
        print ("There is %s days in %s" % (one, months[month - 1]))
        print ("______________________")
    elif month in y:
        print ("There is %s days in %s" % (two, months[month - 1]))
        print ("______________________")
    elif month in z:

        feb = int(input("What year do you want to see\n"))

        if feb % 4 == 0 and (feb % 100 != 0 or feb % 400 == 0):
            print ("There are 29 days in Febuary")
            print ("____________________________")

        else:
            print ("There are 28 days in Febuary")
            print ("______________________________")
    


