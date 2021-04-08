# Modules
import tarot_dictionary
import tarot_spread
import random
# Module End

# Full List of Tarot Cards
def full_deck():
    cards = tarot_dictionary.tarot_deck;
    list_cards = []
    for x in cards.items():
        list_cards.append(x)
    return list_cards

card_face = []
card_meaning = []

#Step 1: Meet the guest
# name = input("Hello. What is your name?")
# print("Hello " + name + ". Welcome to the tarot game!")

# ready = input(" Are you ready to have your fortune told? (Yes or No)")
# if ready == "Yes":
#     print("Great! Let's get started.")
# else:
#     print("It'll be fine - take a deep breath and let's get started.")


#Step 2: Select type of reading from tarot_spread document
print("Are you interested in a One Card Oracle reading (A) or a Three Card Oracle Reading (B)")
card_spread = input().upper()
if card_spread == "A":
    #oracle_one_reading
    usedSpread = tarot_spread.oracleSpread
elif card_spread == "B":
    #oracle_three_reading
    usedSpread = tarot_spread.threeSpread
else:
    print("Stop wasting my time! Pick one!")
print(usedSpread)
dictionaryUsed = usedSpread

#Step 3: Selected card from tarot_deck and determining its orientation
totalPullcards = dictionaryUsed['totalCards']
card = random.sample(range(0,21),totalPullcards)
for x in card:
    #Determine if Card is Upright or Reverse
    random_number = random.random()
    if random_number >= .5:
        #Up Right
        face = full_deck()[x][1]['face']
        meaning = full_deck()[x][1]['Keywords']
    else:
        #Reverse
        face = full_deck()[x][1]['face']+" in Reverse"
        meaning = full_deck()[x][1]['Keywords']
    card_face.append(face)
    card_meaning.append(meaning)

#Step 4: Spitting back out the values
cardDescriptionValue = []
for key, value in dictionaryUsed.items():
    if key == 'name':
        pass
    elif key == 'totalCards':
        pass
    else:
        cardDescriptionValue.append(value)

x = 0
y = x+1
while x < totalPullcards:
    y = x+1
    print("The number", y ,"card is", card_face[x])
    print(cardDescriptionValue[x],"is",card_meaning[x])
    x += 1
