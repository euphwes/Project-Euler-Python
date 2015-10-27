from collections import Counter

#-------------------------------------------------------------------------------------------------

ACE   = 14
KING  = 13
QUEEN = 12
JACK  = 11

value_dict = dict(zip(
    ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'],
    list(range(2,11)) + [JACK, QUEEN, KING, ACE],
))

card_value = lambda x: value_dict[x[0]]
card_suit  = lambda x: x[1]

#-------------------------------------------------------------------------------------------------

class PokerHand(object):
    """ Represents a hand in standard 5-card poker, with no wild cards.

    In this scheme, the type of hands and their internal score as follows:

    High Card:        0
    One Pair:         1
    Two Pairs:        2
    Three of a Kind:  3
    Straight:         4
    Flush:            5
    Full House:       6
    Four of a Kind:   7
    Straight Flush:   8
    Royal Flush:      9

    By comparing the scores above against each other, we can quickly see if one hand beats another
    by their score. If the scores are identical (ie same hands), the high cards can be checked to
    determine the winning hand. """

    def __init__(self, cards):
        """ Expects a string describing the hand. The string must contain 5 pairs of alphanumerics
        separated by spaces, where each alphanumeric pair is of the form   <value><suit>

        <value> can be any character in the following list: [2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A]
        indicating card value in ascending order

        <suit> can be any character in the following list: [S, C, D, H]
        indicating card suit (spades, clubs, diamond, hearts)

        Example: "2H 4C 5S 5D JD".
        """
        self._input = cards
        self._parse_hand(cards)


    def __repr__(self):
        if hasattr(self, '_description'):
            return '{}: {}'.format(self._description, self._input)
        return self._input


    def __gt__(self, other):

        # Check if this hand is better than the other, or the other hand is better
        # than this one
        if self.hand_score > other.hand_score:
            return True
        elif self.hand_score < other.hand_score:
            return False

        # If both hands are the same type (ie. both hands are 2 pairs), compare each
        # high card, kicker, or whatever the appropriate comparator is until a winner
        # is determined
        for mine, theirs in zip(self.high_cards, other.high_cards):
            if mine == theirs:
                continue
            return mine > theirs


    def __lt__(self, other):
        return not self.__gt__(other)


    def _parse_hand(self, cards):

        cards = cards.split()

        self.card_suits        = list(card_suit(card) for card in cards)
        self.cards_high_to_low = list(reversed(sorted(card_value(card) for card in cards)))

        # Royal flush
        if self.is_flush and self.is_straight and self.highest_card == ACE:
            self._description = 'Royal Flush'
            self.hand_score = 9
            self.high_cards = self.cards_high_to_low
            return

        # Straight flush
        if self.is_flush and self.is_straight:
            self._description = 'Straight Flush'
            self.hand_score = 8
            self.high_cards = self.cards_high_to_low
            return

        # Four of a kind
        if self.has_four_of_kind:
            self._description = 'Four of a Kind'
            self.hand_score = 7
            # the value of the 4-of-a-kind match
            self.high_cards = [Counter(self.cards_high_to_low).most_common()[0][0]]
            return

        # Full house
        if self.has_three_of_kind and self.pair_count == 1:
            self._description = 'Full House'
            self.hand_score = 6
            # the value of the 3-of-a-kind match
            self.high_cards = [Counter(self.cards_high_to_low).most_common()[0][0]]
            return

        # Flush
        if self.is_flush:
            self._description = 'Flush'
            self.hand_score = 5
            self.high_cards = self.cards_high_to_low
            return

        # Straight
        if self.is_straight:
            self._description = 'Straight'
            self.hand_score = 4
            self.high_cards = self.cards_high_to_low
            return

        # Three of a kind
        if self.has_three_of_kind:
            self._description = 'Three of a Kind'
            self.hand_score = 3
            # the value of the 3-of-a-kind match
            self.high_cards = [Counter(self.cards_high_to_low).most_common()[0][0]]
            return

        # Two pairs
        if self.pair_count == 2:
            self._description = 'Two Pairs'
            self.hand_score = 2
            c = Counter(self.cards_high_to_low)
            pair1 = c.most_common()[0][0]
            pair2 = c.most_common()[1][0]
            kicker = [c.most_common()[2][0]]

            # highest pair first, then lower pair, then remaining card
            self.high_cards = list(reversed(sorted([pair1, pair2]))) + kicker
            return

        # One pair
        if self.pair_count == 1:
            self._description = 'One Pair'
            self.hand_score = 1
            c = Counter(self.cards_high_to_low)
            pair = [c.most_common()[0][0]]

            # highest pair first, then remaining cards in descending order
            kickers = list(reversed(sorted([c.most_common()[1][0], c.most_common()[2][0], c.most_common()[3][0]])))
            self.high_cards = pair + kickers
            return

        else:
            # High card
            self._description = 'High Card'
            self.hand_score = 0
            self.high_cards = self.cards_high_to_low


    @property
    def highest_card(self):
        """ Returns the value of the highest card. """
        return self.cards_high_to_low[0]


    @property
    def lowest_card(self):
        """ Returns the value of the lowest card. """
        return self.cards_high_to_low[-1]


    @property
    def is_flush(self):
        """ Determines if there is only one type of suit in the hand. """
        return len(set(self.card_suits)) == 1


    @property
    def is_straight(self):
        """ Determines if the hand is a straight. """
        return (self.highest_card - self.lowest_card == 4) and (len(set(self.cards_high_to_low)) == 5)


    @property
    def pair_count(self):
        """ Determines how many pairs are in the hand (0, 1, or 2). """
        return list(Counter(self.cards_high_to_low).values()).count(2)


    @property
    def has_three_of_kind(self):
        """ Determines if there is a three-of-a-kind in the hand. """
        return 3 in Counter(self.cards_high_to_low).values()


    @property
    def has_four_of_kind(self):
        """ Determines if there is a four-of-a-kind in the hand. """
        return 4 in Counter(self.cards_high_to_low).values()
