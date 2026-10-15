import turtle
wn=turtle.Screen()   #this creates drawing window screen
wn.bgcolor("light green")  #it makes screen background color as light green
wn.title("Turtle")   #it writes title for our turtle program
skk=turtle.Turtle()   #creating turtle with skk
skk.speed(5)   #it states the turtle drawing speed
'''skk.forward(100)    #it moves the turtle forward to 100 pixels in whihc direction it faces.
#turtle.done()  #Output will be shown and quits immediately if we didnt write turtle done() statement


for i in range(4):
    skk.forward(50)
    skk.right(90)  #here 90 represent how many degrees should the cursor turn like turning 45 degrees or 90 degrees
turtle.done()   #keeps the window open after the execution
skk.penup()   #lifting the pen so it doesnt draw a line
skk.goto(-75,150)   #(x,y) move 150 pixels straight up in y axis and moves 75 pixels right in x axis
skk.pendown()  #puttign the pen back down so it is ready to draw
for i in range(8):
    skk.left(45)
    skk.forward(100)
    skk.right(90)
    skk.forward(100)
turtle.done()


#star turtle
skk.left(75)
skk.forward(100)
for i in range(4):
    skk.right(144)
    skk.forward(100)
turtle.done()

#inside outside block

skk.color("blue")
skk.right(90)
skk.forward(75)
a=0
for i in range(15):
    skk.left(90)
    skk.fd(100+a)   #forward=fd
    a+=25
turtle.done()

#Circle
for i in range(2):
    skk.circle(5*i)  #it draws circle wiht radius 5 
    skk.circle(-5*i) #it draws circle wiht radius to its right cox=z the radius is in negative
    skk.left(i)  #it turns only 1 degree left whihc cannot be seen wiht a naked eye
turtle.done()


skk.write("avinash",align="center",font=("Courier",20,"bold"))   #writes the given text and aligns to display in center wiht Courier font in bold of size 20
turtle.done()


for i in range(4):
    skk.write("Hello")
    skk.circle(50,360)  #skk.circle(radius of the circle, degrees of the circle)
turtle.done()

#print staemnts prints its positions
print(skk.position())
skk.fd(100)
print(skk.position())
skk.fd(100)
print(skk.position())
skk.right(90)
skk.fd(100)
print(skk.position())
skk.right(90)
skk.fd(100)
print(skk.position())
turtle.done()'''


