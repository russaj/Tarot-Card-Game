# Modules
import tarot_dictionary
import random
# Module End

# name = input("Hello. What is your name?")
# print("Hello " + name + ". Welcome to the tarot game!")

# ready = input(" Are you ready to have your fortune told? (Yes or No)")
# if ready == "Yes":
#     print("Great! Let's get started.")
# else:
#     print("It'll be fine - take a deep breath and let's get started.")

#print("Please pick a number between 1 and 23.")
#number = int(input())
#number -= 1
#print(number)
print("Are you interested in a One Card Oracle reading (A) or a Three Card Oracle Reading (B)")
card_spread = input().upper()
if card_spread == "A":
    #oracle_one_reading()
    v1 = random.sample(range(0,21),1)
    print(v1)
elif card_spread == "B":
    #oracle_three_reading()
    v1,v2,v3 = random.sample(range(0,21),3)
    print(v1,v2,v3)
else:
    print("Stop wasting my time! Pick one!")
cards = tarot_dictionary.tarot_deck;
list_cards = []
for x in cards.items():
    list_cards.append(x)
#print(type(list_cards))
#choose random card
#random_card1 = random.randint(0, 21)
v1,v2,v3 = random.sample(range(0,21),3)
print(v1,v2,v3)

# determine upright or reverse card
random_number = random.random()
print(random_number)
if random_number >= .5:
    print(list_cards[v1][1]['face'])
    print(list_cards[v1][1]['Keywords'])
else:
    print(list_cards[v1][1]['face'])
    print(list_cards[v1][1]['Reverse Keywords'])

random_number = random.random()
print(random_number)
if random_number >= .5:
    print(list_cards[v2][1]['face'])
    print(list_cards[v2][1]['Keywords'])
else:
    print(list_cards[v2][1]['face'])
    print(list_cards[v2][1]['Reverse Keywords'])

random_number = random.random()
print(random_number)
if random_number >= .5:
    print(list_cards[v3][1]['face'])
    print(list_cards[v3][1]['Keywords'])
else:
    print(list_cards[v3][1]['face'])
    print(list_cards[v3][1]['Reverse Keywords'])
#name of the card
#print(list_cards[number][1]['Suit'])
#print(list_cards[number][1]['Keywords'])
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
