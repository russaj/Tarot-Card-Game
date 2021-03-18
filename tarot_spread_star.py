# Modules
import tarot_dictionary
import random
# Module End
print("The Star Spread is used to explore a specific question. Be sure that your question is clear and precise.")
print("")

def full_deck():
    cards = tarot_dictionary.tarot_deck;
    list_cards = []
    for x in cards.items():
        list_cards.append(x)
    return list_cards

card_face = []
card_meaning = []
#this is a variable to determine how many cards are being pulled.
totalPullcards = 6
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

#print(card_face[0])
#print(card_meaning[0])
print("For the first card I see "+card_face[0]+", it is in the position of your present situation, relating to "+card_meaning[0]+".The second card represents The cause of your issues, and you drew "+card_face[1]+", which signifies "+card_meaning[1]+". The third card represents changes needed to resolve your issue, here presented as "+card_face[2]+ ", which could be interpreted as "+card_meaning[2]+". The fourth card represents Your Own Needed Strength, you drew "+card_face[3]+" which means "+card_meaning[3]+". Next is Other challenges to overcome, seen here in the "+card_face[4]+", which means "+card_meaning[4]+". And finally, the sixth card is the likely solution. Seen here with the drawn "+card_face[5]+" meaning "+card_meaning[5]+". Thank you for coming in today, I hope you found the answers you were looking for.")
