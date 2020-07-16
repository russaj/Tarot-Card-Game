# Setup Start
import tarot_dictionary
import random
# Setup End

# name = input("Hello. What is your name?")
# print("Hello " + name + ". Welcome to the tarot game!")

# ready = input(" Are you ready to have your fortune told? (Yes or No)")
# if ready == "Yes":
#     print("Great! Let's get started.")
# else:
#     print("It'll be fine - take a deep breath and let's get started.")

print("Please pick a number between 1 and 23.")
number = int(input())
number -= 1
print(number)

cards = tarot_dictionary.tarot_deck;
list_cards = []
for x in cards.items():
    list_cards.append(x)
print(type(list_cards))
#name of the card
print(list_cards[number][1]['Suit'])
print(list_cards[number][1]['Keywords'])
#print(list_cards[number][1])
#for y in list_cards[0]['keywords']:
#    print(y)
#print(type(y))

#for k,v in cards.items():
#    print(k)

#print(type(list_cards))
#print(list_cards[0][number])

#selection = random.choice(list(cards.values()))
#print(selection)
