import random
print("rock paper scissors game with computer :")
round=int(input("How many rounds you wanna play? :"))
i=1
p=0
c=0
for i in range(round):
    game=input('''Enter 'r' for rock,'s' for scissors,'p' for paper :''')    
    if(game=='r'):
        print("you chose rock")
        print('''    _____
---'   __)
      (_____)
      (_____)
      (____)
---.__(___)''')
    elif(game=='s'):
        print("you chose scissors")
        print('''    _____
---'   __)____
          ____)
       ________)
      (____)
---.__(___)''')
    else:
        print("you chose paper")
        print('''    _____
---'   __)____
          ____)
          _____)
         _____)
---.__________)''')
    
    t="psr"
    counter=random.choice(t)
    if(counter=='r'):
        print("computer chose rock")
        print('''    _____
---'   __)
      (_____)
      (_____)
      (____)
---.__(___)''')
    elif(counter=='s'):
        print("computer chose scissors")
        print('''    _____
---'   __)____
          ____)
       ________)
      (____)
---.__(___)''')
    else:
        print("computer chose paper")
        print('''    _____
---'   __)____
          ____)
          _____)
         _____)
---.__________)''')
    if(game==counter):
        print("Its a tie")
    elif(game=='r' and counter=='s')or(game=='s' and counter=='p')or(game=='p' and counter=='r'):
        print("You won")
        p=p+1
    elif(counter=='r' and game=='s')or(counter=='s' and game=='p')or(counter=='p' and game=='r'):
        print("you lost")
        c=c+1
print("The final scores are :")
print(f"Player's score   :{p}")
print(f"Computer's score :{c}")