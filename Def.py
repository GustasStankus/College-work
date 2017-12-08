from random import randint

def q1():
      def name(name1):
            return name1
      nameInput = input("What is your name?:\n")
      print ("Hello %s" % (name(nameInput).title()))
      print ("==============")

def q2():
      def randomNum():
            return randint(1,6)
      print ("The number from 1 to 6 is %s" % (randomNum()))
      print ("=============================")

def q3():
      def addone(num,num2):
            return num + num2
      num = int(input("what number do you want first\n"))
      num2 = int(input("what number do you want second\n"))
      print ("%s + %s = %s" % (num, num2, addone(num,num2)))
      print ("==============")

def q4():
      def addone(num,num2):
            return num - num2
      num = int(input("what number do you want first\n"))
      num2 = int(input("what number do you want second\n"))
      print ("%s - %s = %s" % (num, num2, addone(num,num2)))
      print ("==============")

def q5():
      def addone(num,num2):
            return num * num
      num = int(input("what number do you want first\n"))
      num2 = int(input("what number do you want second\n"))
      print ("%s * %s = %s" % (num, num2, addone(num,num2)))
      print ("==============")

def q6():
      def addone(num,num2):
            return num / num2
      num = int(input("what number do you want first\n"))
      num2 = int(input("what number do you want second\n"))
      print ("%s / %s = %s" % (num, num2, addone(num,num2)))
      print ("==============")

def q7():
      def addone(num):
            return num ** 2
      num = int(input("what number do you want first\n"))
      result = addone(num)
      print ("%s**2 = %s" % (num, addone(num)))
      print ("==============")
      
def q8():
      def addone(num,num2,num3):
            addNum = num + num2 + num3
            return addNum / 3
      num = int(input("what number do you want first\n"))
      num2 = int(input("what number do you want second\n"))
      num3 = int(input("what number do you want third\n"))
      result = addone(num,num2,num3)
      print ("The mean of %s, %s and %s is %s" % (num, num2, num3, result))
      print ("==================================")

def q9():
      def randomNum(x):
            return randint(1,x)
      num = int(input("What number do you want?\n"))
      print ("The number from 1 to %s is %s" % (num, randomNum(num)))
      print ("=============================")

def q10():
      def itmesTable(x,y):
            l = []
            for i in range(y+1):
                  num3 = x * i
                  l.append("%s * %s = %s" % (x, i, num3))
            return l
      num1 = int(input("What number times table do you want to see\n"))
      num2 = int(input("How big you want the times table to be\n"))
      for i in range(num2+1):
            print (itmesTable(num1,num2)[i])
      print("===================")


# 11
def q11():
      def GCD(x,y):
            listX = []
            for i in range(1, x+1):
                  zero = x % i
                  if zero == 0:
                        listX.insert(0,i)
            listY = []
            for i in range(1, y+1):
                  zero = y % i
                  if zero == 0:
                        listY.insert(0,i)
            listXY = []                    
            for i in listX and listY:
                  listXY.append(i)
            return listXY[1]
      num1 = int(input("what number do you want first\n"))
      num2 = int(input("what number do you want second\n"))

      print("The GCD of number %s and %s is %s" % (num1, num2, GCD(num1,num2)))
      print("=================================")



end = 0            
while end == 0:
      q = int(input("What question do you want to see\n"))
      if q == 1:
            q1()
      elif q == 2:
            q2()
      elif q == 3:
            q3()
      elif q == 4:
            q4()
      elif q == 5:
            q5()
      elif q == 6:
            q6()
      elif q == 7:
            q7()
      elif q == 8:
            q8()
      elif q == 9:
            q9()
      elif q == 10:
            q10()
      elif q == 11:
            q11()
      else:
            end = 1

      

