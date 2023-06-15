print("Welcome to the Nature Quiz Game!")

playing = input("Are you ready to test your nature knowledge? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Giraffes have the highest blood pressure of all land animals. True or false? ")
if answer.lower() == "true":
    print("Correct! Lucky guess, perhaps...")
    score += 1
else:
    print("Incorrect! Giraffes actually need high blood pressure to pump blood all the way up their necks to their brains.")

answer = input("Hipppotamous calves are sometimes born underwater. True or false? ")
if answer.lower() == "true":
    print("Correct! Hippos can give birth under water. After the birth, the mother gently lifts the newborn up to the surface to breathe in air.")
    score += 1
else:
    print("It's actually true! Time to fire up the nature documentaries.")

answer = input("Orangutans hold leaves over their heads when it rains. True or false? ")
if answer.lower() == "true":
    print("Correct! They don’t like water in general - it’s just too wet! The animals can swim but only do it if it can’t be avoided.")
    score += 1
else:
    print("Actually Orangutans do hold leaves above their heads when it rains. They don’t like water in general - it’s just too wet! The animals can swim but only do it if it can’t be avoided.")

print("You got " + str(score) + " questions correct!")
