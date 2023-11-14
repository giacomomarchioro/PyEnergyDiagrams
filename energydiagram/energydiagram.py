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
from matplotlib.patches import PathPatch
from matplotlib.path import Path
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
        self.color_top_text = 'k'
        self.aspect = aspect
        self.round_energies_at_digit = "keep all digits"
        self.top_text_fontsize = "medium"
        self.bottom_text_fontsize = "medium"
        self.right_text_fontsize = "medium"
        self.left_text_fontsize = "medium"
        # data
        self.pos_number = 0
        self.energies = []
        self.positions = []
        self.top_texts = []
        self.bottom_texts = []
        self.left_texts = []
        self.right_texts = []
        self.links = []
        self.arrows = []
        self.electons_boxes = []
        self.level_kwargs = []
        # matplotlib fiugre handlers
        self.fig = None
        self.ax = None

    def add_level(self, energy, bottom_text='', position=None,
                  top_text=None, right_text='', left_text='', color='k', linewidth=2, **kwargs):
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
        right_text  : str
                Text at the right of the level. (default  '')
        left_text  : str
                Text at the left of the level. (default  '')
        linestyle  : str
                The linestyle of the level, one of the following values:
                'solid', 'dashed', 'dashdot', 'dotted' (default  'solid')




        Returns
        -------
        Append to the class data all the information regarding the level added
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
        if top_text is None:
            if self.round_energies_at_digit == "keep all digits":
                top_text = energy
            else:
                top_text = round(energy, self.round_energies_at_digit)

        self.energies.append(energy)
        self.positions.append(position)
        self.top_texts.append(top_text)
        self.bottom_texts.append(bottom_text)
        self.left_texts.append(left_text)
        self.right_texts.append(right_text)
        kwargs['color'] = color
        kwargs['linewidth'] = linewidth
        self.level_kwargs.append(kwargs)

        self.links.append([])
        self.arrows.append([])

    def add_arrow(self, start_level_id, end_level_id, position='center', text=None, **kwargs):
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
        self.arrows[start_level_id].append((end_level_id, position, text, kwargs))

    def add_link(self, start_level_id, end_level_id, line_order=1, color='k', ls='dashed', lw=1.0, **kwargs):
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
        kwargs['line_order'] = line_order
        kwargs['color'] = color
        kwargs['ls'] = ls
        kwargs['lw'] = lw
        self.links[start_level_id].append((end_level_id, kwargs))

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

    def plot_level(self, energy, pos, btext, ttext, rtext, ltext, **kwargs):
        start = pos * (self.dimension + self.space)
        self.ax.hlines(energy, start, start + self.dimension, **kwargs)
        # top text
        self.ax.text(start + 0.5 * self.dimension,  # X
                     energy + self.offset,  # Y
                     ttext,  # self.top_texts
                     horizontalalignment='center',
                     verticalalignment='bottom',
                     color=self.color_top_text,
                     fontsize=self.top_text_fontsize)
        # bottom text
        self.ax.text(start + self.dimension,  # X
                     energy,  # Y
                     rtext,  # self.right_text
                     horizontalalignment='left',
                     verticalalignment='center',
                     color=self.color_bottom_text,
                     fontsize=self.left_text_fontsize)
        # right text
        self.ax.text(start,  # X
                     energy,  # Y
                     ltext,  # self.left_text
                     horizontalalignment='right',
                     verticalalignment='center',
                     color=self.color_bottom_text,
                     fontsize=self.right_text_fontsize)
        # left text
        self.ax.text(start + 0.5 * self.dimension,  # X
                     energy - 2 * self.offset,  # Y
                     btext,  # self.bottom_text
                     horizontalalignment='center',
                     verticalalignment='top',
                     color=self.color_bottom_text,
                     fontsize=self.bottom_text_fontsize)

    def plot_link(self, idx, idy, **kwargs):
        # i is a tuple: (end_level_id,ls,linewidth,color)
        start = self.positions[idx] * (self.dimension + self.space)
        x1 = start + self.dimension
        x2 = self.positions[idy] * (self.dimension + self.space)
        y1 = self.energies[idx]
        y2 = self.energies[idy]
        # draw line
        line_order = kwargs.pop('line_order')
        if line_order == 1:
            # straight line
            line = Line2D([x1, x2], [y1, y2], **kwargs)
            self.ax.add_line(line)
        elif line_order == 2:
            # tapered at the top
            curve = PathPatch(Path([(x1, y1), ((x1 + x2)/2, max(y1, y2)), (x2, y2)],
                                   [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
                              fc="none",
                              **kwargs
                              )
            self.ax.add_patch(curve)
        elif line_order == 3:
            # tapered at bottom and top
            curve = PathPatch(Path([(x1, y1), ((x1 + x2)/2, y1), ((x1 + x2)/2, y2), (x2, y2)],
                                   [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]),
                              fc="none",
                              **kwargs
                              )
            self.ax.add_patch(curve)
        else:
            raise NotImplementedError

    def plot_arrow(self, idx, idy, position, text, **kwargs):
        start = self.positions[idx] * (self.dimension + self.space)
        x_arrow = start + 0.5 * self.dimension
        x_text = x_arrow
        y1 = self.energies[idx]
        y2 = self.energies[idy]
        gap = y1 - y2

        if text is None:
            if self.round_energies_at_digit == 'keep all digits':
                text = gap
            else:
                text = round(gap, self.round_energies_at_digit)

        middle = y1 - 0.5 * gap
        arrow_width = 20.0
        arrowprops = {'arrowstyle': '<->',
                      'shrinkA': 0,
                      'shrinkB': 0,
                      'linestyle': '--',
                      'mutation_scale': arrow_width,
                      'color': 'green',
                      }
        bbox = {'boxstyle': 'round',
                'fc': 'white',
                'color': 'green',
                }
        arrowprops.update({key: kwargs[key] for key in kwargs if key in arrowprops})
        bbox.update({key: kwargs[key] for key in kwargs if key in bbox})

        # determine arrow position
        if position == 'center':
            ha = 'center'
        elif position == 'right':
            arrowprops['arrowstyle'] = '|-|'
            arrowprops['mutation_scale'] *= 0.2
            x_arrow += 0.5 * self.dimension + 0.2 * self.space
            x_text += 0.5 * self.dimension + 0.5 * self.space
            ha = 'left'
        elif position == 'left':
            arrowprops['arrowstyle'] = '|-|'
            arrowprops['mutation_scale'] *= 0.2
            x_arrow -= 0.5 * self.dimension + 0.2 * self.space
            x_text -= 0.5 * self.dimension + 0.5 * self.space
            ha = 'right'
        else:
            raise ValueError

        # double arrow
        self.ax.annotate("", xy=(x_arrow, y1), xytext=(x_arrow, y2), arrowprops=arrowprops)
        # text
        self.ax.text(x_text, middle, text, bbox=bbox, va='center', ha=ha)

        # draw supporting line if levels are offset
        line_kwargs = {'color': 'green',
                       'linestyle': '--'}
        line_kwargs.update({key: kwargs[key] for key in kwargs if key in line_kwargs})
        p1 = self.positions[idx]
        p2 = self.positions[idy]
        if p1 > p2:
            x2 = p2 * (self.dimension + self.space) + self.dimension
            x1 = p1 * (self.dimension + self.space) + self.dimension
            line = Line2D([x1, x2], [y2, y2], **line_kwargs)
            self.ax.add_line(line)
        elif p2 > p1:
            x2 = p2 * (self.dimension + self.space)
            x1 = p1 * (self.dimension + self.space)
            line = Line2D([x1, x2], [y2, y2], **line_kwargs)
            self.ax.add_line(line)

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
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(111, aspect=self.aspect)
        # Otherwise register the axes and figure the user passed.
        else:
            self.ax = ax
            self.fig = ax.figure

            # Constrain the target axis to have the proper aspect ratio
            self.ax.set_aspect(self.aspect)

        self.ax.set_ylabel(ylabel)
        self.ax.axes.get_xaxis().set_visible(False)
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['bottom'].set_visible(False)

        self.__auto_adjust()

        data = zip(self.energies,  # 0
                   self.positions,  # 1
                   self.bottom_texts,  # 2
                   self.top_texts,  # 3
                   self.right_texts,  # 5
                   self.left_texts,  # 6
                   self.level_kwargs)  # 7

        for energy, pos, btext, ttext, rtext, ltext, kwargs in data:
            self.plot_level(energy, pos, btext, ttext, rtext, ltext, **kwargs)

        if show_IDs:
            # for showing the ID allowing the user to identify the level
            for ind, level in enumerate(data):
                start = level[1]*(self.dimension+self.space)
                self.ax.text(start, level[0]+self.offset, str(ind),
                             horizontalalignment='right', color='red')

        for idx, arrow in enumerate(self.arrows):
            # x1, x2   y1, y2
            for idy, position, text, kwargs in arrow:
                self.plot_arrow(idx, idy, position, text, **kwargs)

        for idx, link in enumerate(self.links):
            # here we connect the levels with the links
            # x1, x2   y1, y2
            for idy, kwargs in link:
                self.plot_link(idx, idy, **kwargs)

        for box in self.electons_boxes:
            # here we add the boxes
            # x,y,boxes,electrons,side,spacing_f
            x, y, boxes, electrons, side, spacing_f = box
            plot_orbital_boxes(self.ax, x, y, boxes, electrons, side, spacing_f)

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
            self.dimension = space_for_level * 0.5
            self.space = space_for_level * 0.5

        if self.offset == 'auto':
            self.offset = Energy_variation*self.offset_ratio


if __name__ == '__main__':
    a = ED()
    a.round_energies_at_digit = 2
    a.bottom_text_fontsize = 'xx-small'
    a.top_text_fontsize = 'xx-small'
    a.add_level(0, 'Separated Reactants')
    a.add_level(-5.4, 'mlC1')
    a.add_level(-15.6, 'mlC2', 'last',)
    a.add_level(28.5, 'mTS1', color='g')
    a.add_level(-9.7, 'mCARB1')
    a.add_level(-19.8, 'mCARB2', 'last')
    a.add_level(20, 'mCARBX', 'last')
    a.add_link(0, 1, color='r')
    a.add_link(0, 2)
    a.add_link(2, 3, color='b', line_order=2)
    a.add_link(1, 3, line_order=2)
    a.add_link(3, 4, color='g', line_order=2)
    a.add_link(3, 5, line_order=2)
    a.add_link(0, 6, line_order=3)
    a.add_electronbox(level_id=0, boxes=1, electrons=2, side=3, spacing_f=3)
    a.add_electronbox(3, 3, 1, 3, 3)
    a.add_electronbox(5, 3, 5, 3, 3)
    a.add_arrow(3, 4, position='center', color='blue')
    a.add_arrow(6, 4, position='center')
    a.add_arrow(5, 4, position='right', color='r')
    a.plot(show_IDs=True)
