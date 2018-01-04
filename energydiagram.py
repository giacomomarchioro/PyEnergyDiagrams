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


class ED:
    def __init__(self):
        #plot parameters
        self.dimension = 3
        self.space = 2
        self.offset = 1
        self.color_bottom_text = 'blue'
        #data 
        self.pos_number=0
        self.energies = []
        self.positions = []
        self.colors = []
        self.top_texts = []
        self.bottom_texts = []
        self.links = []
        self.arrows = []
        
        
    def add_level(self,energy, bottom_text ='', position = None, color = 'k', 
                  top_text = 'Energy',):
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
                 argument for adding the level to the last position used.  
                 (default  None)
         color  : str 
                 Color of the level  (default  'k')
         top_text  : str 
                 Text on the top of the level. By default it will print the 
                 energy of the level. (default  'Energy')

                 
        
        Returns
        -------
        Append to the calss data all the informations regarding the level added
        '''

        if position == None:
            position = self.pos_number + 1
            self.pos_number +=1


        elif position == 'last':
            position = self.pos_number
        if top_text == 'Energy':
            top_text = energy
       
        link = []       
        self.colors.append(color)
        self.energies.append(energy)
        self.positions.append(position)
        self.top_texts.append(top_text)
        self.bottom_texts.append(bottom_text)
        self.links.append(link)
     
    def add_arrow(self,start_level_id,end_level_id):
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
        
    def add_link(self,start_level_id,end_level_id):
        '''
        Method of ED class
        Add a link between two energy levels using IDs of the leve. Use
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
        self.links[start_level_id].append(end_level_id)
        
     
    def plot(self,show_IDs=False):
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
        
        Returns
        -------
        fig (plt.figure) and ax (fig.add_subplot()) 

        '''
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_ylabel( "Energy / $kcal$ $mol^{-1}$")
        ax.axes.get_xaxis().set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        data = zip(self.energies, # 0
                   self.positions, # 1
                   self.bottom_texts, # 2
                   self.top_texts, # 3
                   self.colors) # 4
        for level in data:
            start = level[1]*(self.dimension+self.space)
            ax.hlines(level[0],start,start+self.dimension, color = level[4])
            ax.text(start+self.dimension/2., #X
                    level[0]+self.offset,  #Y
                    level[3], # self.top_texts 
                    horizontalalignment='center')
            ax.text(start+self.dimension/2., # X
                    level[0]-self.offset*2, # Y
                    level[2], # self.bottom_text
                    horizontalalignment='center',
                    color= self.color_bottom_text)
        if show_IDs:           
            for ind,level in enumerate(data):
                start = level[1]*(self.dimension+self.space)
                ax.text(start, level[0]+self.offset, str(ind),
                        horizontalalignment='right',color='red')
        
        for idx, arrow in enumerate(self.arrows):
            # by Kalyan Jyoti Kalita
            # x1, x2   y1, y2
            for i in arrow:
                start = self.positions[idx]*(self.dimension+self.space)
                x1 = start + 0.5*self.dimension
                x2 = start + 0.5*self.dimension
                y1 = self.energies[idx]
                y2 = self.energies[i]
                gap = y1-y2
                gapnew = '{0:.2f}'.format(gap) 
                middle= y1-0.5*gap          #warning: this way works for negative HOMO/LUMO energies
                ax.annotate("", xy=(x1,y1), xytext=(x2,middle), arrowprops=dict(color='green', width=1.5, headwidth=5))
                ax.annotate(s= gapnew, xy=(x2, y2), xytext=(x1, middle), color='green', arrowprops=dict(width=1.5, headwidth=5, color='green'),
                        bbox=dict(boxstyle='round', fc='white'),
                        ha='center', va = 'center')
        
        
        for idx, link in enumerate(self.links):
            # x1, x2   y1, y2
            for i in link:
                start = self.positions[idx]*(self.dimension+self.space)
                x1 = start + self.dimension
                x2 = self.positions[i]*(self.dimension+self.space)
                y1 = self.energies[idx]
                y2 = self.energies[i]
                l = Line2D([x1,x2],[y1,y2], ls='--',linewidth = 0.5, color= 'k')                                    
                ax.add_line(l) 
        return fig, ax
 
if __name__ == '__main__':
        a = ED()
        print 'Created ED() instance called: a'
        a.add_level(0,'Separated Reactants')
        a.add_level(-5.4,'mlC1')
        a.add_level(-15.6,'mlC2','last',)
        a.add_level(28.5,'mTS1',color='g')
        a.add_level(-9.7,'mCARB1')
        a.add_level(-19.8,'mCARB2','last')
        a.add_level(20,'mCARBX','last')
        print 'Added levels using a.add_level()'
        a.add_link(0,1)
        a.add_link(0,2)
        a.add_link(2,3)
        a.add_link(1,3)
        a.add_link(3,4)
        a.add_link(3,5)
        a.add_link(0,6)
        print 'Added links using a.add_link()'
        a.plot(show_IDs=True)
