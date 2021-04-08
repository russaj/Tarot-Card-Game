# Modules
import tarot_dictionary
# Module End

def full_deck():
    cards = tarot_dictionary.tarot_deck;
    list_cards = []
    for x in cards.items():
        list_cards.append(x)
    return list_cards

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
