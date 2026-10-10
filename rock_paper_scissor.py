a=input("Enter choice: ").lower().strip()
b=input("Enter choice: ").lower().strip()
if((a=="rock" and b=="paper") or (a=="paper" and b=="rock")):
    print("paper wins")
elif((a=="rock" and b=="scissor") or (a=="scissor" and b=="rock")):
    print("rock wins")
elif((a=="paper" and b=="scissor") or (a=="scissor" and b=="paper")):
    print("scissor wins")
else:
    print("Draw match")