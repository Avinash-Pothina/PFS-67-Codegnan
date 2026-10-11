import random,string
charc="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890@#$%^&!_+"
charac=string.ascii_letters+string.digits+string.punctuation
pasw=""
passw=""
for i in range(8):
    pasw+=random.choice(charc)
    passw+=random.choice(charac)
print(charc)
print("random password is:",pasw)
print(charac)
print("random password using string import is:",passw)

