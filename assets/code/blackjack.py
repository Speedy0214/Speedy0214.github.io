# Copyright (C) 2019 Pepper(speedy0214.github.io). All Rights Reserved
# Learning and communication only.


# define a MDP
# S, A, P, R, r
# model-free
# evaluate Value Function V(s)
# every-visit mc
# policy: stick if sum of cards>=20, otherwise hit
# action:stick or hit


import pandas as pd
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Player(object):
    def __init__(self):
        self.cards = []

    def take_action(self):
        pass

    def get_card_sum(self):
        card_sum = sum(self.cards)
        if 1 in self.cards and card_sum + 10 <= 21:
            card_sum += 10
        return card_sum

    def player_policy(self, player_sum): return 'stick' if player_sum >= 20 else 'hit'


class Dealer(object):
    def __init__(self):
        self.cards = []
        self.card_show = None

    def dealer_policy(self, dealer_sum):
        return 'stick' if dealer_sum >= 17 else 'hit'

    def get_card_sum(self):
        card_sum = sum(self.cards)
        if 1 in self.cards and card_sum + 10 <= 21:
            card_sum += 10
        return card_sum

class Game(object):
    def __init__(self):
        pass

    def deal_card(self):
        card = np.random.randint(1, 14)
        card = min(card, 10)
        return card

    def play(self):
        # initialize
        player = Player()
        dealer = Dealer()
        ## two cards
        player.cards.append(self.deal_card())
        player.cards.append(self.deal_card())

        dealer.cards.append(self.deal_card())
        dealer.cards.append(self.deal_card())
        dealer.card_show = dealer.cards[-1]

        ## hit if sum of cards 11 or less
        while(player.get_card_sum()<=11):
            player.cards.append(self.deal_card())


        # game start

        # player turn
        player_episode = []
        rewards = [0]
        pr = None
        while(True):
            player_useable_ace = 1 if 1 in player.cards else 0
            player_sum = player.get_card_sum()
            #print("player_sum",player_sum)

            state = (player_useable_ace, player_sum - 12, dealer.card_show-1)

            player_action = player.player_policy(player_sum)

            player_episode.append((state, player_action))

            if  player_action == 'hit':
                # 加一张牌
                new_card = self.deal_card()
                if player_sum + new_card > 21:
                    #print("player > 21")
                    pr = -1
                    rewards.append(-1)
                    break
                else:
                    player.cards.append(new_card)
                    rewards.append(0)
            else:
                break



        if not pr:
            # dealer turn
            dr = None
            while(True):
                dealer_useable_ace = 1 if 1 in player.cards else 0
                dealer_sum = dealer.get_card_sum()
                #print("dealer_sum",dealer_sum)
                dealer_action = dealer.dealer_policy(dealer_sum)
                if dealer_action == 'hit':
                    new_card = self.deal_card()
                    if dealer_sum + new_card > 21:


                        #print("dealer > 21")
                        dr = -1
                        rewards.append(1)
                        break
                    else:
                        dealer.cards.append(new_card)
                else:
                    break

            # win?

            if not dr:
                if dealer_sum > player_sum:
                    rewards.append(-1)
                elif dealer_sum < player_sum:
                    rewards.append(1)
                elif dealer_sum == player_sum:
                    rewards.append(0)
        #print('player.cards:', player.cards)
        #print('dealer.cards:', dealer.cards)
        #print(player_episode, rewards)
        return player_episode, rewards

def MC(num=10000):
    VALUES = np.zeros([2,10,10])
    REWARDS = np.zeros([2,10,10])
    COUNTS = np.ones([2,10,10])
    for i in tqdm(range(num)):
        # time.sleep(0.01)
        episode, reward = Game().play()
        if sum(reward)>1:
            raise Exception('rewards sum:%s'%sum(reward))
        # if reward[-1] == 1:

            #print('episode',episode)
            #print( 'reward',reward)
        G = 0
        for j in range(len(episode)):
            state = episode[len(episode)-j-1][0]
            action = episode[len(episode)-j-1][1]
            G += reward[len(episode)-j]
            REWARDS[state] += G
            COUNTS[state] += 1
            VALUES[state] = REWARDS[state]/COUNTS[state]
    return VALUES



if __name__ == '__main__':
    import time
    s1 = time.time()

    V = MC(10000)
    V1 = MC(500000)
    X = np.arange(0, 10, 1)
    Y = np.arange(0, 10, 1)
    X, Y = np.meshgrid(X, Y)


    fig = plt.figure()
    ax = fig.add_subplot(221, projection='3d')
    ax.plot_wireframe(X, Y, V[0], rstride=1, cstride=1)

    ax = fig.add_subplot(222, projection='3d')
    ax.plot_wireframe(X, Y, V[1], rstride=1, cstride=1)

    ax = fig.add_subplot(223, projection='3d')
    ax.plot_wireframe(X, Y, V1[0], rstride=1, cstride=1)

    ax = fig.add_subplot(224, projection='3d')
    ax.plot_wireframe(X, Y, V1[1], rstride=1, cstride=1)


    plt.show()
    #print(time.time()-s1)
