print("Welcome to the Nature Quiz Game!")

playing = input("Are you ready to test your nature knowledge? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

answer = input("Giraffes have the highest blood pressure of all land animals. True or false? ")
if answer.lower() == "true":
    print("Correct! Lucky guess, perhaps...")
else:
    print("Incorrect! Giraffes actually need high blood pressure to pump blood all the way up their necks to their brains.")

