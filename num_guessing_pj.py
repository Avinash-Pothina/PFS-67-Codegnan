import random
print("welcome to number guessing game")
print("the number you have to guess in the range of 0-100")
print("you have only 7 chances to guess the number")
print("good luck")
print()
def game():
 a=random.randint(0,100)
 for i in range(1,8):
  print("chance",i)
  b=int(input("guess the number: "))
  if b<a:
    print(b,"is less than the guessing number")
  elif b>a:
    print(b,"is greater than the guessing number")
  else:
    print("congratulations you have guessed the correct number",a)
    break
  print()
 else:
  print("sorry you ran out of chances")
  print("the number is",a)
  print("better luck next time")
c=0
def regame():	
 game()
 def rgame():
  global c
  if c>0:
   d=input("please enter (y/n):")
  else:
   d=input("do you want to play again (y/n): ").lower()
  if d=='y' or d=='yes':
    return regame()
  elif d=='n' or d=='no':
    pass
  else:
    c+=1
    return rgame()
 global c
 c-=c
 rgame()
regame()
print("thank you for playing game")