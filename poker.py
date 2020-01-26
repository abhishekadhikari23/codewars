class PokerHand(object):

    RESULT = ["Loss", "Tie", "Win"]
    def __init__(self, hand):
        hand_list = hand.split(' ')
        straight = True
        for i in hand_list:
            if i[0] in ['K','Q','J','A']:
                straight = False
        pass
        
    def compare_with(self, other):
        pass