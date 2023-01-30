from type import typewriter as write
import time

name = input("What is your name? :")
score = 0


def easy():
  global score
  global name
  write('\nYou choose Easy, Here is how it works :\nYou will be given 1 points per answer you get out of 5 questions\nGOODLUCK! :)')
  q1easy = input('\nWhat is my Fullname : ')
  if q1easy.lower().replace(' ','')== "anoziechibuikejoel":
    score+=1
    write('\nCorrect!\n\nScore : {}'.format(score))
  else:
    write('Incorrect! :(\nScore : {}'.format(score))
  q2easy = input('Am I tall or Short : ')
  if q2easy.lower().strip()== "tall":
    score+=1
    write('Correct!\nScore : {}'.format(score))
  else:
    write('Incorrect! :(\nScore : {}'.format(score))
  q3easy = input('What is my best Color : ')
  if q3easy.lower().strip() == "black":
    score+=1
    write('Correct!\nScore : {}'.format(score))
    if score == 3:
      write('Wow, 3 points streak! ')
  else:
    write('Incorrect!\nScore : {}'.format(score))
  q4easy = input('What state do I live in : ')
  if q4easy.lower().strip()== "lagos":
    score+=1
    write('Correct!\nScore : {}'.format(score))
    if score == 4:
      write('You are on fire!!!, 4 points streak')
  else:
    write('Incorrect!\nScore : {}'.format(score))
  q5easy = input("What's my state of Origin : ") 
  if q5easy.lower().replace(' ','')== "anambra" or q5easy.lower().strip() == 'anambrastate':
    score+=1
    write('Correct!\nScore : {}'.format(score))
  else:
    write('Incorrect!\nScore : {}'.format(score))
  write('Congratulaions!, You have sucessfully finished the Easy Level of "HowWellDoYouKnowJoel" Quiz\n\nYou ended up scoring {}/5 questions'.format(score))
  time.sleep(0.5)
  if score >= 4 :
     write('You scored 4 or 5 so therefore you know Joel but you should try a higher tier level to know if you know him very well, as the easy level are basic questions and are few')
  elif score == 3:
     write('You scored 3... sigh....you know Joel not too well')
  else:
    write('You scored 2 or 1 or 0......\nYOU DO NOT KNOW JOEL!\nIf you are his friend you should consider again or you start asking about him then get your ass back here to know if you passed')

    
def func():
  global name
  write("Welcome {}, Do you know Joel so well? \nHe created this program to put you through the test of how much you know him, try getting a perfect score if you dare 😈".format(name))
  write('\nPick a level :\n\nEasy\nMedium\nHard')
  level = input("\nInput : ")
  if level.upper().strip()== 'EASY':
    easy()
  elif level.upper().strip()== 'MEDIUM':
    wmedium()
  elif level.upper().strip() == 'HARD':
    hard()
  else:
    write('You need to pick a Level')
    func()

func()    
def again():
  while True:
    out = input("Type 'restart' to restart the program or 'exit' to stop : ")
    if out.lower().replace(" ",'')== 'restart':
      func()
    elif out.lower().replace(" ","")== 'exit':
      break
    else:
      write('Invalid Command mother fucker\n')
      again()
again()
    
