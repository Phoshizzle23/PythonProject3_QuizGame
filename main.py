############################################
### Project #1 - PC Hardware - Quiz Game ###
############################################
print("Welcome to my Computer Quiz!!!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("OK!!! Let's Play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct! ;)")
    score += 1
else:
    print("Wrong!!! :P")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct! ;)")
    score += 1
else:
    print("Wrong!!! :P")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct! ;)")
    score += 1
else:
    print("Wrong!!! :P")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct! ;)")
    score += 1
else:
    print("Wrong!!! :P")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%!")
