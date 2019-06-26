import numpy as np
import time
import sys
from base import *




if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk


UNIT = 100   # pixels
MAZE_H = 4  # grid height
MAZE_W = 4  # grid width
rectsize = 36

class DP(tk.Tk, object):
    def __init__(self):
        super(DP, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.title('Gridworld')
        self.geometry('{0}x{1}'.format(3*MAZE_H * UNIT, MAZE_H * UNIT))
        self._build_maze()


    def _build_maze(self):
        self.canvas = tk.Canvas(self, bg='white',
                           height=MAZE_H * UNIT,
                           width=MAZE_W * UNIT)


        # create grids
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_W * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)

        self.Values = np.zeros([MAZE_H*MAZE_W, 1])
        self.Texts = []

        self._create_text()

        # create origin
        origin = np.array([50, 50])

        self.canvas1 = tk.Canvas(self, bg='white',
                           height=MAZE_H * UNIT,
                           width=MAZE_W * UNIT)



        # create grids
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            self.canvas1.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_W * UNIT, r
            self.canvas1.create_line(x0, y0, x1, y1)

        self.Arrows = []

        self._create_Arrows()

        self.canvas1.pack(cnf={'side':'right'})

        # # hell
        #
        # hell1_center = origin + np.array([UNIT * 2, UNIT])
        # self.hell1 = self.canvas.create_rectangle(
        #     hell1_center[0] - rectsize, hell1_center[1] - rectsize,
        #     hell1_center[0] + rectsize, hell1_center[1] + rectsize,
        #     fill='black')
        # # hell
        # hell2_center = origin + np.array([UNIT, UNIT * 2])
        # self.hell2 = self.canvas.create_rectangle(
        #     hell2_center[0] - rectsize, hell2_center[1] - rectsize,
        #     hell2_center[0] + rectsize, hell2_center[1] + rectsize,
        #     fill='black')

        # # create oval
        # oval_center = origin + UNIT * 2
        # self.oval = self.canvas.create_oval(
        #     oval_center[0] - rectsize, oval_center[1] - rectsize,
        #     oval_center[0] + rectsize, oval_center[1] + rectsize,
        #     fill='yellow')
        #
        # # create red rect
        # self.rect = self.canvas.create_rectangle(
        #     origin[0] - rectsize, origin[1] - rectsize,
        #     origin[0] + rectsize, origin[1] + rectsize,
        #     fill='red')



        # pack all
        self.canvas.pack(cnf={'side':'left'})

    def _create_text(self):
        i = 0
        for c in range(0, MAZE_W):
            for r in range(0, MAZE_H):

                # self.Texts.append(self.canvas.create_text([(c+0.5)*UNIT,(r+0.5)*UNIT],text=self.Values[r, c]))
                self.Texts.append(self.canvas.create_text([(c+0.5)*UNIT,(r+0.5)*UNIT],text=str(np.ceil(self.Values[i, 0]*10)/10)))

                i += 1

    def _create_Arrows(self):
        i = 0
        for c in range(0, MAZE_W):
            for r in range(0, MAZE_H):

                max_q = (-1 + self.Values[SURROUND.get(i)]).max()


                if (-1 + self.Values[SURROUND.get(i)])[0,0] == max_q: # max_q_action = 'top'
                    self.Arrows.append(self.canvas1.create_line([(c+0.5)*UNIT,(r+0.5)*UNIT, (c+0.5)*UNIT,(r)*UNIT], arrow = "last"))
                if (-1 + self.Values[SURROUND.get(i)])[2,0] == max_q: # max_q_action = 'bottom'
                    self.Arrows.append(self.canvas1.create_line([(c+0.5)*UNIT,(r+0.5)*UNIT, (c+0.5)*UNIT,(r+1)*UNIT], arrow = "last"))

                if (-1 + self.Values[SURROUND.get(i)])[1,0] == max_q: # max_q_action = 'left'
                    self.Arrows.append(self.canvas1.create_line([(c+0.5)*UNIT,(r+0.5)*UNIT, (c)*UNIT,(r+0.5)*UNIT], arrow = "last"))
                if (-1 + self.Values[SURROUND.get(i)])[3,0] == max_q: # max_q_action = 'right'
                    self.Arrows.append(self.canvas1.create_line([(c+0.5)*UNIT,(r+0.5)*UNIT, (c+1)*UNIT,(r+0.5)*UNIT], arrow = "last"))

                i += 1

    def reset(self):
        self.update()
        time.sleep(0.1)
        [self.canvas.delete(t) for t in self.Texts]
        self.Values[:,:] = 0
        self._create_text()
        # origin = np.array([50, 50])

        # return observation
        # return self.canvas.coords(self.rect)

    def iterate_value(self):
        self.Values = np.around(R + np.dot(P, self.Values), 2)
        print(self.Values)
        [self.canvas.delete(t) for t in self.Texts]
        self._create_text()

    def iterate_policy(self):

        [self.canvas1.delete(t) for t in self.Arrows]
        self._create_Arrows()


    def render(self):
        time.sleep(2)
        self.update()


def update():
    for t in range(10):
        print(1)
        s = env.reset()
        while True:
            env.render()
            env.iterate_value()
            env.iterate_policy()

if __name__ == '__main__':
    env = DP()
    env.after(1000, update)
    env.mainloop()
