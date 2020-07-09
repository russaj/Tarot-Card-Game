# Setup Start
import tarot_dictionary
# Setup End

# name = input("Hello. What is your name?")
# print("Hello " + name + ". Welcome to the tarot game!")

# ready = input(" Are you ready to have your fortune told? (Yes or No)")
# if ready == "Yes":
#     print("Great! Let's get started.")
# else:
#     print("It'll be fine - take a deep breath and let's get started.")

print("Please pick a number between 1 and 22.")
number = int(input())
print(number)

card = tarot_dictionary.tarot_deck["fool"];
print(card)

#for x in tarot_deck:
#    print(tarot_deck["Keywords"])

