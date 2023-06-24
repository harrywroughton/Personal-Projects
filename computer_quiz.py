print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

# user starts game and exits if statement
if playing.lower() != "yes":
    quit()

# score determined from start
print("OK, let's play!")
score = 0

# add point to score for all questions correct, otherwise score remains the same and moves to next Q
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Sorry, your answer is incorrect!")

answer = input("What is the most universal coding language? ")
if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Sorry, your answer is incorrect!")

answer = input("What does RAM stand for ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Sorry, your answer is incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Sorry, your answer is incorrect!")

# convert score to string to give output of score and percentage
print("You got " + str(score) + " question correct!")
print("You got " + str((score / 4) * 100) + "%.")
