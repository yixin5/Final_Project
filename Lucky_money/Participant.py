import numpy as np
import random
from random import randint

class Participant:

    def __init__(self, participant_id, init_money):
        self.participant_id = participant_id
        self.init_money = init_money
        self.remain_money = self.cal_remain_money()

    def send_out_envolope(self, mean, var):
        """Given the mean and var of the amount of red envelop a participant would send out,
           predict how much money the participant will actually send out
           (Assume the normal distribution)"""
        total_amonut_of_envelope = np.random.normal(mean, var, 1)

        return total_amonut_of_envelope

    def split_envolope(self, total_amonut_of_envelope):
        """1. Split the envelop into n small envelops,
        where n ~ Uniform(min=1, max = total_amonut_of_envelope / 0.01)
        2. Use n to randomly assign weight to each small envelop
        Return: the amonut of money in each samll envelope """
        n = int(np.random.uniform(1, total_amonut_of_envelope / 0.01,1))
        random_num_list = []
        for i in range(n + 1):
            random_num_list.append(randint(1, 10))
        rate = np.random.dirichlet(random_num_list, 1)
        small_envolopes = total_amonut_of_envelope * rate

        return small_envolopes


    def cal_remain_money(self, money_get, money_send_out):
        """A function to calculate the remain money"""
        remain_money = self.init_money + money_get - money_send_out
        self.init_money = remain_money

        return remain_money
