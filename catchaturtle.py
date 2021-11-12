# a121_catch_a_turtle.py
#-----import statements-----
import turtle 
import random as rand
import leaderboard as lb
class error(Exception):
  pass
#-----game configuration----
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("What is your name? ")
wn = turtle.Screen()
wn.bgcolor("green")
while True:
  try:
    game_difficulty = input("difficulty 1, 2, or 3: ")
    if game_difficulty == "1":
      spot_size = 5
      spot_speed = 1
    elif game_difficulty == "2":
      spot_size = 3
      spot_speed = 5
    elif game_difficulty == "3":
      spot_size = 1
      spot_speed = 0
    else:
      raise error(Exception)
    break
  except error:
    print("enter only the difficulties of 1, 2, or 3")
spot_shape = "circle"
spot_fillcolor = "blue"
score = 0
font_setup = ("Arial",20,"bold")
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----initialize turtle-----
counter =  turtle.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-600,350)
counter.pendown()
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(600,350)
score_writer.pendown()
spot = turtle.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_fillcolor)
spot.speed(spot_speed)
#-----game functions--------
# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
def update_score():
  global score
  score += 1
  score_writer.write(score,font=font_setup)
def move(xx,yy):
  spot.penup()
  spot.goto(xx,yy)
  spot.pendown()
def spot_clicked(x,y):
  yaxi = rand.randint(-350,250)
  xaxi = rand.randint(-450,250)
  global timer_up
  if timer_up == False:
    score_writer.clear()
    update_score()
    spot.hideturtle()
    move(xaxi,yaxi)
    spot.showturtle()
  else:
    spot.hideturtle()

#-----events----------------
spot.onclick(spot_clicked)
wn.ontimer(countdown, counter_interval)
wn.mainloop()
