# Modules
import tarot_dictionary
import random
# Module End

def full_deck():
    cards = tarot_dictionary.tarot_deck;
    list_cards = []
    for x in cards.items():
        list_cards.append(x)
    return list_cards

card_face = []
current_card = 4
card = random.sample(range(0,21),current_card)
for x in card:
    #Determine if Card is Upright or Reverse
    random_number = random.random()
    if random_number >= .5:
        #Up Right
        face = full_deck()[x][1]['face']
        meaning = full_deck()[x][1]['Keywords']
    else:
        #Reverse
        face = full_deck()[x][1]['face']
        meaning = full_deck()[x][1]['Keywords']
    card_face.append(face+" with the meaning "+meaning)
print(card_face)
