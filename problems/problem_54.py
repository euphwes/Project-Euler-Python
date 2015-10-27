"""
Poker hands
-----------

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest,
in the following way:

High Card:       Highest value card.
One Pair:        Two cards of the same value.
Two Pairs:       Two different pairs.
Three of a Kind: Three cards of the same value.
Straight:        All cards are consecutive values.
Flush:           All cards of the same suit.
Full House:      Three of a kind and a pair.
Four of a Kind:  Four cards of the same value.
Straight Flush:  All cards are consecutive values of same suit.
Royal Flush:     Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins;
for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie,
for example, both players have a pair of queens, then highest cards in each hand are compared;
if the highest cards tie then the next highest cards are compared, and so on.

[example skipped because the formatting didn't work well in plain text]

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the
file contains ten cards (separated by a single space): the first five are Player 1's cards and
the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters
or repeated cards), each player's hand is in no specific order, and in each hand there is a clear
winner.

How many hands does Player 1 win?
"""

from utils.timer import time_it
from utils.poker import PokerHand

#-------------------------------------------------------------------------------------------------

def poker_games():
    """ Reads the lines from the resource file, builds each line as a pair of poker hands, and
    yields each pair in turn. """

    with open('resources/problem_054_poker.txt') as f:
        for line in (line.strip() for line in f):
            cards = line.split()
            player1_cards = ' '.join(cards[:5])
            player2_cards = ' '.join(cards[5:])
            yield PokerHand(player1_cards), PokerHand(player2_cards)


@time_it
def problem_54():

    print(len([True for p1_hand, p2_hand in poker_games() if p1_hand > p2_hand]))


#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_54()
