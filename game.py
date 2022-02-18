import time
import random
import os


A = [0,1,2,3,4,5,6]
B = [0,1,2,3,4,5,6]

# user position
user = [0,3]

# Score
score = 0

# speed
SPEED = 0.5 # seconds

# 6x6 Graph]
for i in range(0,len(A)):
  for j in range(0, len(B)):
    print(f"({i},{j})", end="")
  print("\n")

# Obstacles
obs = [[5,1],[3,4], [6,2], [0,4], [2,3],[1,6],[4,6]]
while 1==1:
   for o in obs: 
    # Initiate current obstacle with the ordinate as c
      c = 6
      o[0]=c
      # choix = "Gauche"
      while c >= 0:
          # define the speed
          time.sleep(SPEED)
          # Operation: ordinate must receive the counter
          c = c - 1
          
          o[0]-=1
          # obstacle position 
          valeur = random.randint(-1, 1)
          user[1]-=valeur
          if user[1] == -1:
            user[1] = 6
          if user[1] == 7:
            user[1] = 0
          # position aleatoire generer par python
          print(f"position aleatoire: {user}")
          print(obs)
          
          # Score management inside the condition
          if o[0] == -1:            
            score+=10
            SPEED = SPEED * 0.5
          # rules of collision with the user
    
          if user == o:
            print ("vous avez perdu") 
            print (f"Votre score final est: {score}")
            os.system("python3 main.py")
            exit()
          # print(c)

