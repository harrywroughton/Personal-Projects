print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("OK, let's play!")
score = 0

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

print("You got " + str(score) + " question correct!")
print("You got " + str((score / 4) * 100) + "%.")
