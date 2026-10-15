import random
print("welcome to word guessing game")
print("you'll be having 5 chances")
print("all the best\n")
a=['carbon dioxide','magnesium','photosynthesis','smartwatch','Indian flag']
b=random.choice(a)
for i in range(5):
   print("\nchance",i+1,": ",end="")
   c=input()
   for j in b:
      z=[]
      if c==j:
         #print(c,end="")
         z.append(c)
      else:
         #print("_",end="")
         z.append("_")
      #for k in z:
      print()
print("\nyou lost the game answer is:",b)