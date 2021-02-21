# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 13:09:19 2017

--- Energy profile diagram---
This is a simple script to plot energy profile diagram using matplotlib.
E|          4__
n|   2__    /  \
e|1__/  \__/5   \
r|  3\__/       6\__
g|
y|
@author: Giacomo Marchioro giacomomarchioro@outlook.com

"""
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from .box_notation import plot_orbital_boxes


class ED:
    def __init__(self, aspect='equal'):
        # plot parameters
        self.ratio = 1.6181
        self.dimension = 'auto'
        self.space = 'auto'
        self.offset = 'auto'
        self.offset_ratio = 0.02
        self.color_bottom_text = 'blue'
        self.aspect = aspect
        # data
        self.pos_number = 0
        self.energies = []
        self.positions = []
        self.colors = []
        self.top_texts = []
        self.bottom_texts = []
        self.left_texts = []
        self.right_texts = []
        self.links = []
        self.arrows = []
        self.electons_boxes = []
        # matplotlib fiugre handlers
        self.fig = None
        self.ax = None

    def add_level(self, energy, bottom_text='', position=None, color='k',
                  top_text='Energy', right_text='', left_text=''):
        '''
        Method of ED class
        This method add a new energy level to the plot.

        Parameters
        ----------
        energy : int
                The energy of the level in Kcal mol-1
        bottom_text  : str
                The text on the bottom of the level (label of the level)
                (default '')
        right_text  : str
                The text on the right of the level (default '')
        left_text  : str
                The text on the left of the level (default '')
        position  : str
                The position of the level in the plot. Keep it empty to add
                the level on the right of the previous level use 'last' as
                argument for adding the level to the last position used
                for the level before.
                An integer can be used for adding the level to an arbitrary
                position.
                (default  None)
        color  : str
                Color of the level  (default  'k')
        top_text  : str
                Text on the top of the level. By default it will print the
                energy of the level. (default  'Energy')



        Returns
        -------
        Append to the class data all the informations regarding the level added
        '''

        if position is None:
            position = self.pos_number + 1
            self.pos_number += 1
        elif isinstance(position, (int, float)):
            pass
        elif position == 'last' or position == 'l':
            position = self.pos_number
        else:
            raise ValueError(
                "Position must be None or 'last' (abrv. 'l') or in case an integer or float specifing the position. It was: %s" % position)
        if top_text == 'Energy':
            top_text = energy

        link = []
        self.colors.append(color)
        self.energies.append(energy)
        self.positions.append(position)
        self.top_texts.append(top_text)
        self.bottom_texts.append(bottom_text)
        self.left_texts.append(left_text)
        self.right_texts.append(right_text)
        self.links.append(link)
        self.arrows.append([])

    def add_arrow(self, start_level_id, end_level_id):
        '''
        Method of ED class
        Add a arrow between two energy levels using IDs of the level. Use
        self.plot(show_index=True) to show the IDs of the levels.

        Parameters
        ----------
        start_level_id : int
                 Starting level ID
        end_level_id : int
                 Ending level ID

        Returns
        -------
        Append arrow to self.arrows

        '''
        self.arrows[start_level_id].append(end_level_id)

    def add_link(self, start_level_id, end_level_id,
                 color='k',
                 ls='--',
                 linewidth=1,
                 ):
        '''
        Method of ED class
        Add a link between two energy levels using IDs of the level. Use
        self.plot(show_index=True) to show the IDs of the levels.

        Parameters
        ----------
        start_level_id : int
                 Starting level ID
        end_level_id : int
                 Ending level ID
        color : str
                color of the line
        ls : str
                line styple e.g. -- , ..
        linewidth : int
                line width

        Returns
        -------
        Append link to self.links

        '''
        self.links[start_level_id].append((end_level_id, ls, linewidth, color))

    def add_electronbox(self,
                        level_id,
                        boxes,
                        electrons,
                        side=0.5,
                        spacing_f=5):
        '''
        Method of ED class
        Add a link between two energy levels using IDs of the level. Use
        self.plot(show_index=True) to show the IDs of the levels.

        Parameters
        ----------
        start_level_id : int
                 Starting level ID
        end_level_id : int
                 Ending level ID

        Returns
        -------
        Append link to self.links

        '''
        self.__auto_adjust()
        x = self.positions[level_id] * \
            (self.dimension+self.space)+self.dimension*0.5
        y = self.energies[level_id]
        self.electons_boxes.append((x, y, boxes, electrons, side, spacing_f))

    def plot(self, show_IDs=False, ylabel="Energy / $kcal$ $mol^{-1}$", ax: plt.Axes = None):
        '''
        Method of ED class
        Plot the energy diagram. Use show_IDs=True for showing the IDs of the
        energy levels and allowing an easy linking.
        E|          4__
        n|   2__    /  \
        e|1__/  \__/5   \
        r|  3\__/       6\__
        g|
        y|

        Parameters
        ----------
        show_IDs : bool
            show the IDs of the energy levels
        ylabel : str
            The label to use on the left-side axis. "Energy / $kcal$
            $mol^{-1}$" by default.
        ax : plt.Axes
            The axes to plot onto. If not specified, a Figure and Axes will be
            created for you.

        Returns
        -------
        fig (plt.figure) and ax (fig.add_subplot())

        '''

        # Create a figure and axis if the user didn't specify them.
        if not ax:
            fig = plt.figure()
            ax = fig.add_subplot(111, aspect=self.aspect)
        # Otherwise register the axes and figure the user passed.
        else:
            self.ax = ax
            self.fig = ax.figure

            # Constrain the target axis to have the proper aspect ratio
            self.ax.set_aspect(self.aspect)

        ax.set_ylabel(ylabel)
        ax.axes.get_xaxis().set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)

        self.__auto_adjust()

        data = list(zip(self.energies,  # 0
                        self.positions,  # 1
                        self.bottom_texts,  # 2
                        self.top_texts,  # 3
                        self.colors,  # 4
                        self.right_texts,  # 5
                        self.left_texts,))  # 6

        for level in data:
            start = level[1]*(self.dimension+self.space)
            ax.hlines(level[0], start, start + self.dimension, color=level[4])
            ax.text(start+self.dimension/2.,  # X
                    level[0]+self.offset,  # Y
                    level[3],  # self.top_texts
                    horizontalalignment='center',
                    verticalalignment='bottom')

            ax.text(start + self.dimension,  # X
                    level[0],  # Y
                    level[5],  # self.bottom_text
                    horizontalalignment='left',
                    verticalalignment='center',
                    color=self.color_bottom_text)

            ax.text(start,  # X
                    level[0],  # Y
                    level[6],  # self.bottom_text
                    horizontalalignment='right',
                    verticalalignment='center',
                    color=self.color_bottom_text)

            ax.text(start + self.dimension/2.,  # X
                    level[0] - self.offset*2,  # Y
                    level[2],  # self.bottom_text
                    horizontalalignment='center',
                    verticalalignment='top',
                    color=self.color_bottom_text)
        if show_IDs:
            # for showing the ID allowing the user to identify the level
            for ind, level in enumerate(data):
                start = level[1]*(self.dimension+self.space)
                ax.text(start, level[0]+self.offset, str(ind),
                        horizontalalignment='right', color='red')

        for idx, arrow in enumerate(self.arrows):
            # by Kalyan Jyoti Kalita: put arrows between to levels
            # x1, x2   y1, y2
            for i in arrow:
                start = self.positions[idx]*(self.dimension+self.space)
                x1 = start + 0.5*self.dimension
                x2 = start + 0.5*self.dimension
                y1 = self.energies[idx]
                y2 = self.energies[i]
                gap = y1-y2
                gapnew = '{0:.2f}'.format(gap)
                middle = y1-0.5*gap  # warning: this way works for negative HOMO/LUMO energies
                ax.annotate("", xy=(x1, y1), xytext=(x2, middle), arrowprops=dict(
                    color='green', width=2.5, headwidth=5))
                ax.annotate(s=gapnew, xy=(x2, y2), xytext=(x1, middle), color='green', arrowprops=dict(width=2.5, headwidth=5, color='green'),
                            bbox=dict(boxstyle='round', fc='white'),
                            ha='center', va='center')

        for idx, link in enumerate(self.links):
            # here we connect the levels with the links
            # x1, x2   y1, y2
            for i in link:
                # i is a tuple: (end_level_id,ls,linewidth,color)
                start = self.positions[idx]*(self.dimension+self.space)
                x1 = start + self.dimension
                x2 = self.positions[i[0]]*(self.dimension+self.space)
                y1 = self.energies[idx]
                y2 = self.energies[i[0]]
                line = Line2D([x1, x2], [y1, y2],
                              ls=i[1],
                              linewidth=i[2],
                              color=i[3])
                ax.add_line(line)

        for box in self.electons_boxes:
            # here we add the boxes
            # x,y,boxes,electrons,side,spacing_f
            x, y, boxes, electrons, side, spacing_f = box
            plot_orbital_boxes(ax, x, y, boxes, electrons, side, spacing_f)

    def __auto_adjust(self):
        '''
        Method of ED class
        This method use the ratio to set the best dimension and space between
        the levels.

        Affects
        -------
        self.dimension
        self.space
        self.offset

        '''
        # Max range between the energy
        Energy_variation = abs(max(self.energies) - min(self.energies))
        if self.dimension == 'auto' or self.space == 'auto':
            # Unique positions of the levels
            unique_positions = float(len(set(self.positions)))
            space_for_level = Energy_variation*self.ratio/unique_positions
            self.dimension = space_for_level*0.7
            self.space = space_for_level*0.3

        if self.offset == 'auto':
            self.offset = Energy_variation*self.offset_ratio


if __name__ == '__main__':
    a = ED()
    a.add_level(0, 'Separated Reactants')
    a.add_level(-5.4, 'mlC1')
    a.add_level(-15.6, 'mlC2', 'last',)
    a.add_level(28.5, 'mTS1', color='g')
    a.add_level(-9.7, 'mCARB1')
    a.add_level(-19.8, 'mCARB2', 'last')
    a.add_level(20, 'mCARBX', 'last')
    a.add_link(0, 1, color='r')
    a.add_link(0, 2)
    a.add_link(2, 3, color='b')
    a.add_link(1, 3)
    a.add_link(3, 4, color='g')
    a.add_link(3, 5)
    a.add_link(0, 6)
    a.add_electronbox(level_id=0, boxes=1, electrons=2, side=3, spacing_f=3)
    a.add_electronbox(3, 3, 1, 3, 3)
    a.add_electronbox(5, 3, 5, 3, 3)
    a.add_arrow(6, 4)
    a.offset *= 2
    a.plot(show_IDs=True)
