# Copyright (C) 2019 Pepper(speedy0214.github.io). All Rights Reserved
# Learning and communication only.
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
from tqdm import tqdm
import tkinter as tk
import time
from random import random
from sklearn.metrics import mean_squared_error

class RandomWalk(tk.Tk, object):
    def __init__(self):
        # super(RandomWalk, self).__init__()


        self.GRID_H = 1
        self.GRID_W = 7

        self.UNIT = 200

        self.actions = [-1, 1]
        self.r = np.array([[0. ],
                           [0. ],
                           [0. ],
                           [0. ],
                           [0. ],
                           [0.5],
                           [0. ]])
        self.P = np.array([[1. , 0. , 0. , 0. , 0. , 0. , 0. ],
                           [0.5, 0. , 0.5, 0. , 0. , 0. , 0. ],
                           [0. , 0.5, 0. , 0.5, 0. , 0. , 0. ],
                           [0. , 0. , 0.5, 0. , 0.5, 0. , 0. ],
                           [0. , 0. , 0. , 0.5, 0. , 0.5, 0. ],
                           [0. , 0. , 0. , 0. , 0.5, 0. , 0.5],
                           [0. , 0. , 0. , 0. , 0. , 0. , 1. ]])
        self.states_names = np.array(['0', 'A', 'B', 'C', 'D', 'E', '1'])

        self.size = len(self.states_names)
        self.values = np.ones([self.size, 1])*0.5
        self.values[0, 0] = 0
        self.values[-1, 0] = 0

        self.true_values = np.array([[0],[1/6],[2/6],[3/6],[4/6],[5/6],[0]])

        self.episodes = []
        self.episodes_name = []

        # self.title('Gridworld')
        # self.geometry('{0}x{1}'.format(self.GRID_W * self.UNIT, self.GRID_H * self.UNIT))
        # self.CanvasItems = []
        #
        # self._build_grid()


    def _build_grid(self):
        self.canvas = tk.Canvas(self, bg='white',
                           height=self.GRID_H * self.UNIT,
                           width=self.GRID_W * self.UNIT)

        self.canvas.create_text(self.UNIT*(self.size/2), self.UNIT/2+66, text='start', font=("", 56))

        for i in range(self.size):
            j = i+1
            self.canvas.create_text(self.UNIT*(j-0.5), self.UNIT/2, text=str(self.states_names[i]), font=("", 36))
            self.canvas.create_oval(self.UNIT*(j-0.5-0.25), self.UNIT*(0.25), self.UNIT*(j-0.25), self.UNIT*(0.75),width=2, fill='grey' if self.states_names[i] in ('0','1') else '')
            if 1 < j < self.size-1:
                self.canvas.create_line(self.UNIT*(j-0.25), self.UNIT/2, self.UNIT*(j+0.25), self.UNIT/2, arrow='both', width=2, arrowshape = "26 26 5")

                self.canvas.create_text(self.UNIT*(j), self.UNIT/2-16,
                    text=1 if self.states_names[i+1] == '1' else 0 , fill='blue',font=("", 26))
            elif j == 1 or j == self.size-1:
                self.canvas.create_line(self.UNIT*(j-0.25), self.UNIT/2,
                            self.UNIT*(j+0.25), self.UNIT/2,arrow='first' if j==1 else 'last', width=2, arrowshape = "26 26 5")

                self.canvas.create_text(self.UNIT*(j), self.UNIT/2-16,
                    text=1 if self.states_names[i+1] == '1' else 0 , fill='blue',font=("", 26))
            else:
                pass

            self.CanvasItems.append(self.canvas.create_text(self.UNIT*(j-0.5), self.UNIT/2-26, text='(%s)'%self.values[i, 0], font=("", 16)))

        self.canvas.pack()

    def update_value_text(self):
        [self.canvas.delete(t) for t in self.CanvasItems]
        self._value_upate()
        print(self.values)
        for i in range(self.size):
            j = i+1
            self.CanvasItems.append(self.canvas.create_text(self.UNIT*(j-0.5), self.UNIT/2-26, text='(%s)'%round(self.values[i, 0],2), font=("", 16)))

        self._render()

    def _value_upate(self):
        print(self.P)
        print(self.values)
        self.values = self.r + np.dot(self.P, self.values)


    def _render(self):
        time.sleep(0.1)
        self.update()


    def MC(self,num = 100, alpha=0.01):

        totalRewards = np.zeros([self.size, 1])
        totalCounts = np.ones([self.size, 1])
        RMSE1 = []
        RMSE2 = []
        for i in tqdm(range(num)):
            # time.sleep(0.1)
            s = 3
            episode_rewords = [0]
            episode = []
            episode_state_name = []
            while True:
                episode.append(s)
                episode_state_name.append(self.states_names[s])
                if random() >=0.5:
                    if s == 5:
                        episode_rewords.append(1)
                    else:
                        episode_rewords.append(0)
                    s += 1
                else:
                    episode_rewords.append(0)
                    s += -1
                if s in (0, self.size-1):
                    break

            # first-visit
            G = 0
            T = len(episode)

            for t in range(T):
                s = episode[T-t-1]
                G += episode_rewords[T-t]
                if s not in episode[0:T-t-1]:
                    self.values[s, 0] += alpha*(G - self.values[s, 0])
            RMSE1.append(np.sqrt(np.mean(abs((self.values - self.true_values)*(self.values - self.true_values)))))
            RMSE2.append(np.sqrt(mean_squared_error(self.values, self.true_values)))
        # print([(RMSE1[i],RMSE2[i]) for i in range(len(RMSE1))])
        return RMSE1





    def TD(self, num=100, alpha=0.01):
        RMSE1 = [np.sqrt(np.mean(abs((self.values - self.true_values)*(self.values - self.true_values))))]
        RMSE2 = [np.sqrt(mean_squared_error(self.values, self.true_values))]
        for i in tqdm(range(num)):
            # time.sleep(0.1)
            s = 3
            episode_rewords = [0]
            episode = []
            episode_state_name = []
            while True:
                episode.append(s)
                episode_state_name.append(self.states_names[s])
                if random() >=0.5:
                    if s == 5:
                        episode_rewords.append(1)
                    else:
                        episode_rewords.append(0)
                    s += 1
                else:
                    episode_rewords.append(0)
                    s += -1
                if s in (0, self.size-1):
                    break

            # TD(0)
            T = len(episode)

            for t in range(T):
                s = episode[t]
                s_next = episode[t+1] if t != T-1 else int(1.5*(s-1))
                r = episode_rewords[t+1]
                self.values[s, 0] += alpha*(r + self.values[s_next, 0] - self.values[s, 0])
            RMSE1.append(np.sqrt(np.mean(abs((self.values - self.true_values)*(self.values - self.true_values)))))
            RMSE2.append(np.sqrt(mean_squared_error(self.values, self.true_values)))
        return RMSE1


# def update(env):

if __name__ == '__main__':

    for a in range(1,6):
        n =100
        MC_RMSE = np.zeros(n)
        TD_RMSE = np.zeros(n)
        print(TD_RMSE)
        for j in range(100):
            rw = RandomWalk()
            MC_RMSE += np.array(rw.MC(n, 0.01*a)[0:n])
            rw = RandomWalk()
            TD_RMSE += np.array(rw.TD(n,0.05*a)[0:n])
        MC_RMSE = MC_RMSE/100
        TD_RMSE = TD_RMSE/100
        X = [i for i in range(len(MC_RMSE))]
        plt.plot(X, MC_RMSE, label='MC:%s'%(round(0.01*a,2)),color='blue', alpha = 0.2)
        p = 66-8*a
        plt.annotate(r'$\alpha=%s$'%round(0.01*a,2) ,xy=(X[p],MC_RMSE[p]), color='blue', xytext=[-6,0.1], textcoords='offset points')
        plt.plot(X, TD_RMSE, label='TD:%s'%(round(0.05*a,2)), color='red',alpha = 0.2)
        p = 100-16*a
        plt.annotate(r'$\alpha=%s$'%round(0.01*a,2) ,xy=(X[p],TD_RMSE[p]), color='red', xytext=[-10,0.1], textcoords='offset points')
    plt.show()
    # plt.show()



    # R = RandomWalk()
    #
    # while True:
    #     R.update_value_text()
    #
    # R.mainloop()
    # print(time.time()-s1)
