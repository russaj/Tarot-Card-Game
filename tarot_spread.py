# Modules
import tarot_dictionary
# Module End

def full_deck():
    cards = tarot_dictionary.tarot_deck;
    list_cards = []
    for x in cards.items():
        list_cards.append(x)
    return list_cards
## Maybe create a single dictionary around "tarot_spreads = {" and have all these dictionaries operating underneath it?
## Also add in "Description" and make sure it doesn't mess up the information pull from tarot2.py
starSpread = {
  'name': 'Star Spread',
  'totalCards' : 6,
  "lineOne" : "first line",
  "lineTwo" : "second line",
  "lineThree" : "third line",
  "lineFour" : "fourth line",
  "lineFive" : "fifth line",
  "lineSix" : "sixth line",
}

threeSpread = {
  'name': 'Three Spread',
  'totalCards' : 3,
  "lineOne" : "past",
  "lineTwo" : "present",
  "lineThree" : "future",
}

oracleSpread = {
  'name': 'Oracle Spread',
  'totalCards' : 1,
  "lineOne" : "oracle",
}

new_moon_cancerSpread = {
  "Name": "New Moon - Cancer Spread",
  "totalCards": 4,
  "Description": "Understanding the Roots of Your Emotional Changes During the Cancer New Moon",
}

new_moon_manifestationSpread = {
  "Name": "New Moon - Manifestation Spread",
  "totalCards": 6,
  "Description": "New Moon is a good period to cleans yourself of previous issues and set intentions going forward. It's about setting the user up for success with the goals they hope to manifest",
}
celtic_crossSpread = {
  "Name": "Celtic Cross Spread",
  "totalCards": 10,
  "Description": "Made up of the cross and the staff, the cross will show what is most important to you at the time of the reading and what is on your conscious mind whereas the staff represents your life in general and what lessons life has to teach you",
}
horseshoeSpread = {
  "Name": "Hoseshoe Spread",
  "totalCards": 7,
  "Description": "For answering specific questions",
}
fanSpread = {
  "Name": "Fan Spread",
  "totalCards": 22,
  "Description": "General life reading when you don't have a specific question or problem to address",
}
