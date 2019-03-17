from pypokerengine.players import BasePokerPlayer
import pprint


class RaisedPlayer(BasePokerPlayer):
    card_rank = ['A', 'K', 'Q', 'J'] + [str(num) for num in range(10, 1, -1)]

    def __init__(self):
      self.value_map = {}
      self.suit_map = {}

    def add_to_map(self, map, key):
       if key in map:
         map[key] += 1
       else:
         map[key] = 1

    def group_by(self, cards, criteria):
      if criteria == "suit":
        for card in cards:
          self.add_to_map(self.suit_map, card[0])
      else:
        for card in cards:
          self.add_to_map(self.value_map, card[1:])

    def pairs(self):
        return len([self.value_map[key] == 2 for key in self.value_map])

    def pair(self):
        return self.same_kind(2) == 1

    def two_pairs(self):
        return self.same_kind(2) == 2

    def three_of_a_kind(self):
        return self.same_kind(3) == 1

    def straight(self):
        values = sorted(self.value_map.values(), c)

    def same_kind(self, n):
        return self.value_map.values().count(n)

    def three_of_a_kind(self, cards):
        return self.same_kind(cards, 3)

    def four_of_a_kind(self, cards):
        return self.same_kind(cards, 4)

    def evaluation_function(self):
        pass

    def declare_action(self, valid_actions, hole_card, round_state):
        for i in valid_actions:
            if i["action"] == "raise":
                action = i["action"]
                return action  # action returned here is sent to the poker engine
        action = valid_actions[1]["action"]
        return action # action returned here is sent to the poker engine

    def receive_game_start_message(self, game_info):
        pass

    def receive_round_start_message(self, round_count, hole_card, seats):
      pass

    def receive_street_start_message(self, street, round_state):
      pass

    def receive_game_update_message(self, action, round_state):
      pass

    def receive_round_result_message(self, winners, hand_info, round_state):
      pass


def setup_ai():
  return RaisedPlayer()
