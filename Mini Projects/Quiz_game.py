print("Welcome to my CODING QUIZ!")

playing = input("Do you want to play the quiz? ")  
score = 0

if playing.lower() != "yes" :
  quit()
else :
  print("okay, Let's go")
  name = input("What can I call you ? : ")

# Q1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit" :
  print("Congratulation!")
  score += 1
else :
  print("Wrong")

# Q2
answer = input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit" :
  print("Congratulation!")
  score += 1
else :
  print("Wrong")

# Q3
answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory" :
  print("Congratulation!")
  score += 1
else :
  print("Wrong")  

# Q4
answer = input("what does PSU stand for? ")
if answer.lower() == "power supply" :
  print("Congratulation!")
  score += 1 
else :
  print("Wrong")

# Q5
answer = input("What does NPU stand for? ")
if answer.lower() == "neural processing unit" :
  print("Congratulation!")
  score += 1
else :
  print("Wrong")


print("score of {} : {}".format(name, score))
print("This is {}% of the answer".format(score / 5 * 100))