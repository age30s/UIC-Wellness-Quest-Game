# Adithya Prasad
# UIC Wellness Quest Game
import turtle
import random

# This is the UIC Wellness Quest! The below code programs
# a small game that provides tips on how college students
# can be happy and stay on top of work. At the end there 
# a short quiz to test what you learned.


global score
global spritelist
global dict
global linelist
global quizlist

score = 0
spritelist = []
dict = {}
quizlist = []

# opens the text file containing all the tips
# stored in a list with 20 elements
file = open("tips.txt")
lines = file.readlines()
file.close()
linelist = []
for each in lines:
  newline = each.split(':')
  for line in newline:
    linelist.append(line)

# lines 32-106 set up turtles for the quiz
# and for the text
# The order of turtles established determines
# which turtle will appear over what.
turtle.addshape("scorebox.gif")
scorebox = turtle.Turtle()
scorebox.penup()
scorebox.hideturtle()
scorebox.shape("scorebox.gif")
scorebox.goto(-288,260)


text = turtle.Turtle()
text.penup()
text.hideturtle()
text.goto(-330, 245)
text.color("black")


# sets up main character - bottom layer
turtle.addshape("sprite2.gif")
stickman = turtle.Turtle()
stickman.hideturtle()
stickman.shape("sprite2.gif")
stickman.penup()
stickman.goto(-100,100)


turtle.addshape('correct.gif')
correctans = turtle.Turtle()
correctans.hideturtle()
correctans.shape('correct.gif')
correctans.penup()



turtle.addshape('wrong.gif')
wrongans = turtle.Turtle()
wrongans.hideturtle()
wrongans.shape('wrong.gif')
wrongans.penup()


quiz = turtle.Turtle()
quiz.penup()
quiz.hideturtle()

turtle.addshape("D.gif")
letterD = turtle.Turtle()
letterD.hideturtle()
letterD.shape("D.gif")
letterD.penup()


turtle.addshape("C.gif")
letterC = turtle.Turtle()
letterC.hideturtle()
letterC.shape("C.gif")
letterC.penup()


turtle.addshape("B.gif")
letterB = turtle.Turtle()
letterB.hideturtle()
letterB.shape("B.gif")
letterB.penup()


turtle.addshape("A.gif")
letterA = turtle.Turtle()
letterA.hideturtle()
letterA.shape("A.gif")
letterA.penup()


turtle.addshape("congrats.gif")
congrats = turtle.Turtle()
congrats.hideturtle()
congrats.shape("congrats.gif")
congrats.penup()


# shows the UIC mascot with the text box
def tips():
  tip.showturtle()
  tip.penup()
  tip.goto(0,20)
  
  

# allows for texts and images to stay
# onscreen for some time
def stall(num):
  tt = turtle.Turtle()
  tt.hideturtle()
  tt.penup()
  tt.speed(1)
  tt.forward(num)

# randomly sends five turtles out of the ten different options 
# we have to random parts of the screen.
# Player objective is to collect these sprites.
def sprites():
  global setlist
  sprites = ["water.gif","sleep.gif","books.gif","socialize.gif","advisor.gif","goal.gif","coffee.gif","calender.gif","friend.gif","planner.gif"]
  setlist = []
  for i in range(5):
    x = random.randint(0,9)
    if x in setlist:
      while x in setlist:
        x = random.randint(0,9)
      setlist.append(x)
    else:
      setlist.append(x)
    turtle.addshape(sprites[x])
    name = turtle.Turtle()
    name.shape(sprites[x])
    name.penup()
    name.goto(random.randint(-300, 300),  random.randint(-200,200))
    spritelist.append(name)
    dict[x] = name
  
# Checks to see if the player coordinates are near a sprite and any time
# the player uses the arrow keys.
# If the player is near a sprite, it will hide the sprite to indicate the player has
# collected it and will display a tip that corresponds to the sprite.
# Ex: if the player picks up the pillow, it will display how many hours college
# students should sleep. 
def check():
  global score
  for i in range(len(spritelist)):
    if(stickman.distance(spritelist[i].xcor(), spritelist[i].ycor()) < 20):
      spritelist[i].hideturtle()
      spritelist[i].goto(700,300)
      score += 1
      text.clear()
      text.write("Score: "+str(score),False,align="left",font = ("Times New Roman",15,'normal'))
      for key in dict:
        if spritelist[i] == dict[key]:
          facts = turtle.Turtle()
          facts2 = turtle.Turtle()
          facts.penup()
          facts2.penup()
          facts.hideturtle()
          facts2.hideturtle()
          facts.goto(20, 130)
          facts2.goto(20,80)
          tips()
          num = key * 2
          facts.write(linelist[num], False, align='center', font=('Times New Roman', 10,'bold'))
          num += 1
          facts2.write(linelist[num], False, align ='center', font=('Times New Roman', 10, 'bold'))
          stall(1000)
          facts.clear()
          facts2.clear()
          tip.hideturtle()
      scored()
  
# lines 191-209 set up the movement keys
# This allows the player character to move
# in different directions
def up():
  stickman.setheading(90)
  stickman.forward(10)
  check()
  
def down():
  stickman.setheading(270)
  stickman.forward(10)
  check()

def left():
  stickman.setheading(180)
  stickman.forward(10)
  check()

def right():
  stickman.setheading(0)
  stickman.forward(10)
  check()

# calls for the quizwrite function which
# displays the quiz questions
def scoreadder():
  quizwrite()
  
# if the user clicks on the correct choice, this function
# is called. It will display a correct message.
# and add one to a variable count.
# if count is over 3, the quiz ends.
def correct(x,y):
  global score
  global count
  correctans.goto(-10,215)
  correctans.showturtle()
  stall(600)
  correctans.hideturtle()
  quiz.clear()
  count += 1
  if count <= 3:
    scoreadder()
  else:
    letterD.hideturtle()
    letterC.hideturtle()
    letterB.hideturtle()
    letterA.hideturtle()
    mascot = turtle.Turtle()
    turtle.addshape('uicmascot.gif')
    mascot.penup()
    mascot.goto(0,0)
    mascot.shape('uicmascot.gif')
    congrats.goto(-10,215)
    congrats.showturtle()
    
# This function runs if the score is equal to 5. It sets
# up the letters on the screen for the answer choices
# also continues the quiz if the user clicks the right answer
def quizstart():
  global score
  global count
  letterD.goto(250,-160)
  letterD.showturtle()

  letterC.goto(100,-160)
  letterC.showturtle()

  letterB.goto(-100,-160)
  letterB.showturtle()
  
  letterA.goto(-250,-160)
  letterA.showturtle()

  count = 0
  if score == 5:
    quizwrite()
    
  
    

# Displays the quiz questions. These are based off the sprites
# and do not repeat but are random for each runthrough of the game.
def quizwrite(): 
  global score
  global quizlist
  global setlist
  global repeat
  quiz.goto(-222, -53)
  quiz.color("black")
  randomizer = random.choice(setlist)
  if randomizer in repeat:
    while randomizer in repeat:
      randomizer = random.choice(setlist)
    repeat.append(randomizer)
  else:
    repeat.append(randomizer)
  if randomizer == 0:
    quiz.write(q1, False, align='left', font=('Times New Roman', 20))
    letterA.onclick(wrong,btn=1, add=None)
    letterB.onclick(correct,btn=1, add=None)
    letterC.onclick(wrong,btn=1, add=None)
    letterD.onclick(wrong,btn=1, add=None)
  elif randomizer == 1:
    quiz.write(q2, False, align='left', font=('Times New Roman', 20))
    letterA.onclick(wrong,btn=1, add=None)
    letterB.onclick(wrong,btn=1, add=None)
    letterC.onclick(correct,btn=1, add=None)
    letterD.onclick(wrong,btn=1, add=None)
  elif randomizer == 2:
    quiz.write(q3, False, align='left', font=('Times New Roman', 20))
    letterA.onclick(correct,btn=1, add=None)
    letterB.onclick(wrong,btn=1, add=None)
    letterC.onclick(wrong,btn=1, add=None)
    letterD.onclick(wrong,btn=1, add=None)
  elif randomizer == 3:
    quiz.write(q4, False, align='left', font=('Times New Roman', 20))
    letterA.onclick(wrong,btn=1, add=None)
    letterB.onclick(correct,btn=1, add=None)
    letterC.onclick(wrong,btn=1, add=None)
    letterD.onclick(wrong,btn=1, add=None)
  elif randomizer == 4:
    quiz.write(q5, False, align='left', font=('Times New Roman', 20))
    letterA.onclick(wrong,btn=1, add=None)
    letterB.onclick(wrong,btn=1, add=None)
    letterC.onclick(correct,btn=1, add=None)
    letterD.onclick(wrong,btn=1, add=None)
  elif randomizer == 5:
    quiz.write(q6, False, align='left', font=('Times New Roman', 20))
    letterA.onclick(wrong,btn=1, add=None)
    letterB.onclick(wrong,btn=1, add=None)
    letterC.onclick(correct,btn=1, add=None)
    letterD.onclick(wrong,btn=1, add=None)
  elif randomizer == 6:
    quiz.write(q7, False, align='left', font=('Times New Roman', 20))
    letterA.onclick(wrong,btn=1, add=None)
    letterB.onclick(wrong,btn=1, add=None)
    letterC.onclick(correct,btn=1, add=None)
    letterD.onclick(wrong,btn=1, add=None)
  elif randomizer == 7:
    quiz.write(q8, False, align='left', font=('Times New Roman', 20))
    letterA.onclick(wrong,btn=1, add=None)
    letterB.onclick(correct,btn=1, add=None)
    letterC.onclick(wrong,btn=1, add=None)
    letterD.onclick(wrong,btn=1, add=None)
  elif randomizer == 8:
    quiz.write(q9, False, align='left', font=('Times New Roman', 20))
    letterA.onclick(wrong,btn=1, add=None)
    letterB.onclick(wrong,btn=1, add=None)
    letterC.onclick(correct,btn=1, add=None)
    letterD.onclick(wrong,btn=1, add=None)
  elif randomizer == 9:
    quiz.write(q10, False, align='left', font=('Times New Roman', 20))
    letterA.onclick(correct,btn=1, add=None)
    letterB.onclick(wrong,btn=1, add=None)
    letterC.onclick(wrong,btn=1, add=None)
    letterD.onclick(wrong,btn=1, add=None)
  
  
# This runs if the user clicks on the wrong answer
# Displays a message that says the user should try again.
def wrong(x,y):
  wrongans.goto(-10,215)
  wrongans.showturtle()
  stall(600)
  wrongans.hideturtle()
  
# Starts if the user collects all five sprites and score = 5
# Sets up the quiz screen
def scored():
  global score
  global repeat
  repeat = []
  if score >= 5:
    text.clear()
    scorebox.hideturtle()
    stickman.hideturtle()
    s.bgpic('quiz.gif')
    stall(500)
    s.bgpic('quiz2.gif')
    stall(500)
    s.bgpic('quiztemplate.gif')
    quizstart()

# Quiz Questions:   
q1 = "What is a benefit of drinking \n enough water every day?\n A) Improves taste buds\n B) Improves digestive efficiency\n C) Improves vision\n D) Stops bad breath"
q2 = "How much sleep do most college \n students need a night?\n A) 5\n B) 6\n C) 7\n D) 8"
q3 = "How long should your study \n breaks be?\n A) 5-10 minutes\n B) 15-20 minutes\n C) 30 minutes\n D) 1 hour"
q4 = "How can you meet people \n on campus?\n A) Paying attention in class\n B) Joining a club or sport\n C) Keeping to yourself\n D) By completing assignments"
q5 = "Who can help with\n academic complications?\n A) Teacher's assistants\n B) Other students\n C) Academic advisor\n D) The dean of students" 
q6 = "Which is a way to stay motivated?\n A) Drinking enough water\n B) Using a calendar\n C) Setting goals\n D) Talking to an advisor"
q7 = "What should you limit daily \n caffeine to?\n A) 200mg\n B) 300mg \n C) 400mg\n D) 500mg"
q8 = "What can be used to stay on top\n of your assignments?\n A) UIC portal\n B) A calendar\n C) A calculator\n D) A notebook"
q9 = "Which of the following\n help to build a routine?\n A) Going to class\n B) Drinking coffee\n C) Making a schedule\n D) Your advisor"
q10 = "Which is the best place to \n make friends? \n A) In class\n B) In the library \n C) At your friends house \n D) At home"  

# Sets up the screen and the dimensions for the game
s = turtle.Screen()
s.setup(700,600)
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(-250,250)

# Starts the game. Randomly pics a background out of three different ones
if score < 4:
  s.bgpic('wellness.gif')
  stall(1000)
  int = random.randint(1,3)
  if int == 1:
    s.bgpic('grass.gif')
    stickman.showturtle()
    scorebox.showturtle()
    text.write("Score: " + str(score), False, align='left', font=('Times New Roman', 15))
  elif int == 2:
    s.bgpic('city.gif')
    stickman.showturtle()
    scorebox.showturtle()
    text.write("Score: " + str(score), False, align='left', font=('Times New Roman', 15))
  elif int == 3:
    s.bgpic('chicago.gif')
    stickman.showturtle()
    scorebox.showturtle()
    text.write("Score: " + str(score), False, align='left', font=('Times New Roman', 15))
  sprites()

# sets up turtle for the UIC mascot and tip box. This is the last turtle 
# added because it should lay on top of all the other turtles in the game
turtle.addshape("tipBOX.gif")
tip = turtle.Turtle()
tip.hideturtle()
tip.shape('tipBOX.gif')
# sets up movement
s.listen()
  
s.onkey(up,"Up")
s.onkey(down,"Down")
s.onkey(left,"Left")
s.onkey(right,"Right")

turtle.mainloop() 
