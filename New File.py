rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print("Welcome to the Rock, Paper & Scissors Game!!")
a = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for scissors. "))

while a!=0 or a!=1 or 1!=2:
    
  if a==0 or a==1 or a==2:
    break
  else:
    print("\nChoose number from given number")
    a = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for scissors. "))

if a == 0:
  print(rock)
elif a == 1:
  print(paper)
elif a == 2:
  print(scissors)


import random

b = random.randint(0,2)
print("Computer Chose:")
if b == 0:
  print(rock)
elif b == 1:
  print(paper)
elif b == 2:
  print(scissors)

if a==b:
  print("It's Draw")
elif a==0 and b==2:
  print("You win!")
elif a==1 and b==0:
  print("You win!")
elif a==2 and b==1:
  print("You win!")
else:
  print('you lose!')