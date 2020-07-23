#creates the list version of the full deck of tarot cards
def full_deck():
    cards = tarot_dictionary.tarot_deck;
    list_cards = []
    for x in cards.items():
        list_cards.append(x)
    return list_cards
  
#one card oracle spread
def oracle_one():
  v1 = random.sample(range(0,21),1)
  random_number = random.random()
  if random_number >= .5:
    print(full_deck[v1][1]['face'])
    print(full_deck[v1][1]['Keywords'])
  else:
    print(full_deck[v1][1]['face'])
    print(full_deck[v1][1]['Reverse Keywords'])
