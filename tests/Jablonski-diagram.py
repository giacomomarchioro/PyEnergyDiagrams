"""
 @author Le Nhan Pham
 @website https://lenhanpham.github.io/
 @create date 2023-01-30 21:38:25
 @modify date 2023-01-30 21:38:25
"""


import os, sys 
file_path = 'E:\Projects\Martin-reaction\SET\SET\Ir-complex\def2tzvpd\energydiagram'
sys.path.append(os.path.dirname(file_path))

import matplotlib.pyplot as plt
from energydiagram import ED, extracttddft 

output="Ir-complex-Jablonski-diagram"
singletLog ='Ir-complex-singlet-trans-tddft-singlet'
tripletLog ='Ir-complex-singlet-trans-tddft-triplets'
        
singlets = extracttddft.extractData2files(singletLog+".log")
triplets = extracttddft.extractData2files(tripletLog+".log") 


diagram = ED(aspect='auto')
diagram.right_text_fontsize='xx-small'
diagram.bottom_text_fontsize='xx-small'
diagram.top_text_fontsize='xx-small'
diagram.left_text_fontsize='xx-small'

diagram.add_level(0,bottom_text='',top_text='0.00', right_text='S0',position=0, color = 'k')   #'S0'
diagram.add_level(singlets[1],bottom_text=str(round(singlets[1],2)),top_text='', right_text='S1',position=0, color = 'k')   #'S0'
diagram.add_level(triplets[1],bottom_text=str(round(triplets[1],2)),top_text='', right_text='T1',position=1, color = 'g')   #'T0'

singlets.pop(1)
for singlet in singlets:
   diagram.add_level(singlets[singlet],bottom_text='',top_text='',right_text='',position=0, color = 'k')   #'S1' 

triplets.pop(1) 
for triplet in triplets:
    diagram.add_level(triplets[triplet],bottom_text='',top_text='',right_text='',position=1, color = 'g')   #'T1'

diagram.offset = 0.03





diagram.plot() # this is the default ylabel

diagram.ax.set_ylabel("Energy / eV")
diagram.ax.set_xlabel("Electronic state")


#diagram.fig.set_figwidth(10)
diagram.ax.axes.get_xaxis().set_visible(True)
diagram.ax.axes.xaxis.set_ticklabels([])
diagram.ax.axes.set_xticks([], minor=False)
diagram.ax.spines['bottom'].set_visible(True)
plt.savefig(output + '.pdf')
plt.savefig(output + '.svg')