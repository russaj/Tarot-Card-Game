# Modules
import tarot_dictionary
import random
# Module End


#Step 1: Meet the guest
# name = input("Hello. What is your name?")
# print("Hello " + name + ". Welcome to the tarot game!")

# ready = input(" Are you ready to have your fortune told? (Yes or No)")
# if ready == "Yes":
#     print("Great! Let's get started.")
# else:
#     print("It'll be fine - take a deep breath and let's get started.")


#Step 2: Select type of reading > incorporate other file of readings?
print("Are you interested in a One Card Oracle reading (A) or a Three Card Oracle Reading (B)")
card_spread = input().upper()
if card_spread == "A":
    #oracle_one_reading
    v1 = random.sample(range(0,21),1)
    # print(v1)
elif card_spread == "B":
    #oracle_three_reading
    v1,v2,v3 = random.sample(range(0,21),3)
    # print(v1,v2,v3)
else:
    print("Stop wasting my time! Pick one!")

cards = tarot_dictionary.tarot_deck
list_cards = []
for x in cards.items():
    list_cards.append(x)

#Step 3: Choose random card(s)
v1,v2,v3 = random.sample(range(0,21),3)
# print(v1,v2,v3)

#Step 4: Determine upright or reverse card
random_number = random.random()
# print(random_number)
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
