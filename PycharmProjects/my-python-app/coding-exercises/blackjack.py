from numpy import random

dealerHand = []
playerHand = []
deck = []
for x in range(0, 52):
    deck.append(x)

def card(picked):
    cardSuit = 52
    cardName = 52
    if picked / 13 < 1:
        cardSuit = "Diamond"
    elif 1 <= picked / 13 and picked / 13 < 2:
        cardSuit = "Heart"
    elif 2 <= picked / 13 and picked / 13 < 3:
        cardSuit = "Club"
    elif 3 <= picked / 13 and picked / 13 < 4:
        cardSuit = "Spade"
    if picked % 13 in range(1,10):
        cardName = str(picked % 13)
    elif picked % 13 == 0:
        cardName = "Ace"
    elif picked % 13 == 10:
        cardName = "Jack"
    elif picked % 13 == 11:
        cardName = "Queen"
    elif picked % 13 == 12:
        cardName = "King"
    return f"{cardName} of {cardSuit}s"

def startGame():

    picked1 = random.randint(0, len(deck))
    dealerHand.append(picked1)
    deck.pop(picked1)

    picked2 = random.randint(0, len(deck))
    playerHand.append(picked2)
    deck.pop(picked2)

    picked3 = random.randint(0, len(deck))
    dealerHand.append(picked3)
    deck.pop(picked3)

    picked4 = random.randint(0, len(deck))
    playerHand.append(picked4)
    deck.pop(picked4)

    print("The dealer deals you each two cards, placing the second face up on each. "
          f"The dealer has the {card(dealerHand[1])}. You have the {card(playerHand[0])} "
          f"and the {card(playerHand[1])}")

def playerCounter():
    handValue = 0
    for x in playerHand:
        if x % 13 in range(1, 10):
            handValue += (x % 13)
        elif x % 13 in range (10, 13):
            handValue += 10
        else:
            handValue += 1
    return handValue

def playerAceCount():
    aceCount = 0
    for x in playerHand:
        if x % 13 == 0:
            aceCount += 1
    return aceCount

def dealerAceCount():
    aceCount = 0
    for x in dealerHand:
        if x % 13 == 0:
            aceCount += 1
    return aceCount

def dealerCounter():
    handValue = 0
    for x in dealerHand:
        if x % 13 in range(1, 10):
            handValue += (x % 13)
        elif x % 13 in range (10, 13):
            handValue += 10
        else:
            handValue += 1
    return handValue

startGame()