"""
Our group's purpose is to implement Monte Carlo Simulation for the model of "Wechat lucky money relay", which rule
is that In one Wechat group, one person send an electronic red envelope first with random money amount and packet
numbers, then everyone started to grab. The person who grab the largest amount of money continued to send a new round
of red envelopes and then continued to reciprocate. Through the simulation results and analysis to research how different
relay methods and game environments affect the redistribution of wealth among members of the Wechat group.

The numpy version we used in this project is 1.14.2.

Group member: Tongyang Yan, Weihao Li, Yixin Zhou

"""

import numpy as np

# Read the dataset
dataset = np.genfromtxt("total amount.csv", delimiter=",")

# For each person, calculate the total amount of envelope
# And then calculate mean and standard deviation of these people's total amount of envelope
total_amount = np.nansum(dataset, axis=0)
total_amount_mean = np.mean(total_amount)
total_amount_std = np.std(total_amount)


class Player:
    def __init__(self, player_id, initial_money):
        self.player_id = player_id
        self.initial_money = initial_money
        self.money_remained = initial_money

    def send_out_envelope(self, total_amount_mean, total_amount_std):
        """Decide how much money a person will stuff in his/her envelope.
           Assume the amount of money in an envelope subjects to normal distribution

           Args:
               total_amount_mean
               total_amount_std
               Then the_amount_of_money_in_an_envelope ~ N (total_amount_mean, total_amount_std)

           Return:
               total_envolope_amount: An estimate/simulation of the amount of money in this player's envelope
        """
        total_envelope_amount = -1
        # According to Wechat envolope rule:
        #  Player should at least send out envelope with 0.01 RMB and should not send out money more than initial money
        while total_envelope_amount <= 0.01 or total_envelope_amount > self.money_remained:
            total_envelope_amount = np.random.normal(loc=total_amount_mean,
                                                     scale=total_amount_std,
                                                     size=1)

        return total_envelope_amount

    def split_out_envelope(self, player_num):
        """Decide how many small envelopes a player will choose to split his/her original envelope.
           A player will send out at least 1 envelope, and at most player_num envelopes

           Args:
               player_num: int

           Return:
               envelope_num: int
        """
        envelope_num = int(np.random.randint(low=1, high=player_num + 1, size=1))

        return envelope_num

    def send_out_small_envelopes(self, envelope_num, total_envelope_amount):
        """Decide how much money will be stuffed in each small envelope.
           small_envelopes_array = total_amount_of_money_in_original envelope * weights_array.
           weights_array subjects to dirichlet distribution.

           Args:
               envelope_num: int, number of small envelopes
               total_envelope_amount: float, amount of money in the original envelope

           Return:
               small_envelope_array: A numpy array including amount of money in each small envelope.

        """
        # Create a numpy array with shape (1, small_envelope_num)
        alpha = [(num + 1) for num in range(envelope_num)]
        weights = np.random.dirichlet(alpha, size=1)
        # Stuff money into each small envelopes
        small_envelopes_array = weights * total_envelope_amount

        return small_envelopes_array



class Game:
    def __init__(self, players, turn_num):
        """
        Args:
            players: A dict. {player_id: player instance}
            turn_num: the number of turns of the game
                      A turn means: A person send out n small envelopes randomly to n players, the player who get the
                                    largest amount of envelope will be the one to send out small envelopes in the next
                                    turn
        """
        self.players = players
        self.turn_num = turn_num
        self.player_id_list = list(self.players.keys())
        self.player_num = len(self.player_id_list)
        # Choose a player to send out envelope
        # In the first turn, namely, at the beginning, the player is randomly chose
        # In the rest of turns, player who get the largest money amount in the last turn will send out an envelope
        self.player_send_out_id = np.random.choice(self.player_id_list)

    def single_turn(self, total_amount_mean, total_amount_std):
        """Run a single turn of the game, the meaning of one turn has described above.
           At the end of the turn, update self.player_send_out_id, namely, update player who will send out envelopes
           in the next turn.

           Args:
               total_amount_mean: float
               total_amount_std: float
        """
        # Find the player object who sends out envelope in this turn according to player_send_out_id
        player = self.players[self.player_send_out_id]

        # Player chooses the envelope amount
        envelope_amount = player.send_out_envelope(total_amount_mean, total_amount_std)
        player.money_remained -= envelope_amount

        # Randomly split the envelope into small envelopes
        envelope_num = player.split_out_envelope(self.player_num)
        small_envelopes_array = player.send_out_small_envelopes(envelope_num, envelope_amount)

        # Randomly choose "envelope_num_players" to get those small envelopes
        # And increase these players' amount of remained money
        player_get_envelope_id = list(np.random.choice(self.player_id_list, size=envelope_num))
        i = 0
        for player_id in player_get_envelope_id:
            player = self.players[player_id]
            player.money_remained += small_envelopes_array[0, i]
            i += 1

        # Find the player who gets the largest envolope amount
        # Choose this player to send out envolope in the next turn
        largest_envelope_index = np.argmax(small_envelopes_array)
        self.player_send_out_id = player_get_envelope_id[largest_envelope_index]

    def start_game(self, total_amount_mean, total_amount_std):
        """Start game.

           Args:
               total_amount_mean
               total_amount_std

        """
        # Run single turn for turn_num turns
        for turn in range(self.turn_num):
            self.single_turn(total_amount_mean, total_amount_std)


if __name__ == '__main__':

    def gini(wealths):
        """Given the list of people's wealths, Calculate gini of these people.

           Args:
               wealths: A list of remained money, each element is a float

           Return:
               G: Float, gini of this group.
        """

        cum_wealths = np.cumsum(sorted(np.append(wealths, 0)))
        sum_wealths = cum_wealths[-1]
        x_array = np.array(range(0, len(cum_wealths))) / np.float(len(cum_wealths) - 1)
        y_array = cum_wealths / sum_wealths
        B = np.trapz(y_array, x=x_array)
        A = 0.5 - B
        G = A / (A + B)

        return G

    # Monte Carlo Simulation
    #  Create player dict with formats: {player_id: player_object}
    # Here we create 10 players, set their initial money as 1000 RMB, and turn_num as 20
    players_num = 10
    initial_money = 1000
    turn_num = 80
    simulation_times = 1000

    players = {}
    for player_id in range(10):
        players[player_id] = Player(player_id, initial_money)

    # Simulate process for the setted simulation times and save result of gini in gini_list
    gini_list = []
    for i in range(simulation_times):
        game = Game(players, turn_num)
        game.start_game(total_amount_mean, total_amount_std)
        players_remained_money_list = [player.money_remained for player in list(players.values())]
        G = gini(players_remained_money_list)
        gini_list.append(G)

    gini_array = np.array(gini_list)

    # Create a dict whose key is group symbol, value is a numpy array containing the relevant gini
    gini_group_dict = {}
    gini_group1 = gini_array[gini_array < 0.2]
    gini_group_dict["gini < 0.2"] = gini_group1
    gini_group2 = gini_array[np.logical_and(gini_array >=0.2, gini_array < 0.3)]
    gini_group_dict["0.2<= gini <= 0.3"] = gini_group2
    gini_group3 = gini_array[np.logical_and(gini_array >=0.3, gini_array < 0.4)]
    gini_group_dict["0.3 <= gini < 0.4"] = gini_group3
    gini_group4 = gini_array[np.logical_and(gini_array >=0.4, gini_array < 0.5)]
    gini_group_dict["0.4 <= gini < 0.5"] = gini_group4
    gini_group5 = gini_array[gini_array >= 0.5]
    gini_group_dict["gini >= 0.5"] = gini_group5

    # Create a dict whose key is group symbol, value is the probability that a gini belongs to this symbol
    gini_group_prob_dict ={}
    for gini_group, gini_group_value in gini_group_dict.items():
        group_num = gini_group_value.shape[0]
        group_prob = group_num / simulation_times
        gini_group_prob_dict[gini_group] = group_prob


    # Print out the final result
    for gini_group, gini_group_prob in gini_group_prob_dict.items():
        print("The probability in group " + gini_group + " is %.2f."%(gini_group_prob))


