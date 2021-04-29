# Modules
import tarot_dictionary
import tarot_spread
import random
import zodiac
# Module End

# Full List of Tarot Cards
def full_deck():
    cards = tarot_dictionary.tarot_deck;
    list_cards = []
    for x in cards.items():
        list_cards.append(x)
    return list_cards

# Select the Spread you want
def spread_select():
    choiceSelected = False
    while choiceSelected == False:
        print("Are you interested in a One Card Oracle reading (A) or a Three Card Oracle Reading (B)")
        card_spread = input().upper()
        if card_spread == "A":
            #oracle_one_reading
            usedSpread = tarot_spread.oracleSpread
            choiceSelected = True
        elif card_spread == "B":
            #oracle_three_reading
            usedSpread = tarot_spread.threeSpread
            choiceSelected = True
        else:
            print("Stop wasting my time! Pick one!")
            print("")
    return usedSpread

card_face = []
card_meaning = []

#Step 1: Meet the guest
name = input("Hello. What is your name?")

print("Hello " + name + ". Welcome to the tarot game!")
birthDate = input("What month/day were you born (numerically mmdd)?")
if birthDate.isnumeric() == False:
    print("Please provide a valid birthday.")
else:
    if zodiac.zodiacSign(birthDate) == zodiac.currentZodiacSign(zodiac.currentDate):
        print("Wow, it's your birth season!")
    print("Looks like you're a", zodiac.zodiacSign(birthDate))
    ready = input(" Are you ready to have your fortune told? (Yes or No)")
    if ready == "Yes":
        print("Great! Let's get started.")
    else:
        #revise language here, not so forceful?
        print("It'll be fine - take a deep breath and let's get started.")

#Step 2: Select type of reading > incorporate other file of readings?
#Think about putting a While Loop Here to circle through if invalid answer given
dictionaryUsed = spread_select()

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
        meaning = full_deck()[x][1]['Reverse Keywords']
    card_face.append(face)
    card_meaning.append(meaning)

cardDescriptionValue = []
for key, value in dictionaryUsed.items():
    if key == 'name':
        pass
    elif key == 'totalCards':
        pass
    else:
        cardDescriptionValue.append(value)

x = 0
while x < totalPullcards:
    print("The number", (x+1) ,"card is", card_face[x])
    print(cardDescriptionValue[x],"is",card_meaning[x])
    print("")
    x += 1
