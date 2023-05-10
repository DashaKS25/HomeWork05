#https://www.codewars.com/kata/5a360620f28b82a711000047/train/python
def define_suit(card):
    suit_dict = {'S': 'spades', 'D': 'diamonds', 'H': 'hearts', 'C': 'clubs'}
    return suit_dict[card[-1].upper()]