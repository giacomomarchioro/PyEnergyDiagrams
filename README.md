# PyEnergyDiagrams
This is a simple module to plot energy profile diagrams using Python and matplotlib.

![alt tag](https://github.com/giacomomarchioro/PyEnergyDiagrams/blob/master/md_images/Final.png)
## Installation 
If you are new to Python the easiest way to get started is to use a distribution like [Anaconda](https://www.anaconda.com/). Then you can use the terminal to install the module using pip:

    pip install git+https://github.com/giacomomarchioro/PyEnergyDiagrams

The only requirments is [matplotlib](http://matplotlib.org/users/installing.html) which is installed by defult using Anaconda.
  
## How to use it?


```python
from energydiagram import ED
diagram = ED()
diagram.add_level(0,'Separated Reactants')
diagram.add_level(-5.4,'mlC1')
diagram.add_level(-15.6,'mlC2','last',) #Using 'last'  or 'l' it will be together with the previous level
diagram.add_level(28.5,'mTS1',color='g')
diagram.add_level(-9.7,'mCARB1')
diagram.add_level(-19.8,'mCARB2','l')
diagram.add_level(20,'mCARBX','last')
```
Show the IDs (red numbers) for understanding how to link the levels:

```python
diagram.plot(show_IDs=True)
```
![alt tag](https://github.com/giacomomarchioro/PyEnergyDiagrams/blob/master//md_images/With_IDs.png)

Add the links using `diagram.add_link(starting_level_ID,ending_level_ID)`:
```python
diagram.add_link(0,1)
diagram.add_link(0,2)
diagram.add_link(2,3)
diagram.add_link(1,3)
diagram.add_link(3,4)
diagram.add_link(3,5)
diagram.add_link(0,6)
```
For plotting the final result:
```python
diagram.plot(ylabel="Energy / $kcal$ $mol^{-1}$") # this is the default ylabel
```
To show it:
```python
import matplotlib.pyplot as plt
plt.show()
```
The results is displayed above.

## Electron boxes 
Also electron boxes can be added, the electron spin is automatically changed following the aufbau principle.

![alt tag](https://github.com/giacomomarchioro/PyEnergyDiagrams/blob/master/md_images/boxplot.png)

```python
from energydiagram import ED
a = ED()
a.add_level(0,'2pxy',top_text='')
a.add_level(10,'$\sigma*$',top_text='')
a.add_level(5,'$\pi*$','last',top_text='')
a.add_level(-5,'$\pi$','last',color='g',top_text='')
a.add_level(-10,'$\sigma$',top_text='',position='l')
a.add_level(0,'2pxy',top_text='')
for i in range(1,5):
    a.add_link(0,i,color='g')
    a.add_link(i,5,color='b')
a.add_electronbox(level_id=0, boxes=1, electrons=2, side=1.5, spacing_f=2.5)
a.add_electronbox(1,2,0,1.5,3)
a.add_electronbox(2,5,10,1.5,3)
a.add_electronbox(3,3,4,1.5,3)
a.add_electronbox(4,3,2,1.5,3)
a.add_electronbox(5,3,5,1.5,3)
a.offset *= 1.5
a.plot(show_IDs=True)
plt.show()
```
## Trouble shooting and fine tuning
Most of the times there could be a problem of test padding. There are some parameters that can be changed in this way.
```python
diagram.offset = 10
```
![alt tag](https://github.com/giacomomarchioro/PyEnergyDiagrams/blob/master/md_images/Explained.jpg)

To make the change effective you have to use the command `diagram.plot()` again. Remember that once you have done a first attempt for plotting. You can adjust the plot as every matplotlib plot. For convenience you can access `ax` and `fig` from the instance of the class.  

```python
# we adjust some parameters
diagram.ax.set_ylabel('My label')
diagram.fig.set_figwidth(10)
# don't want tikcs on the y label
diagram.ax.set_yticks([])
# I want to show on the x axis instead
diagram.ax.axes.get_xaxis().set_visible(True)
diagram.ax.spines['bottom'].set_visible(True)
diagram.ax.set_xlabel("My x label")
# we replot the figure (sometimes we have to resize with the mouse the figure so we force to refresh)
diagram.fig.show()

```
If you use the command `diagram.plot()` now all the changes will be overwritten, so these minor adjustment must be done after.

### Contributors
Thanks to Kalyan Jyoti Kalita for the arrow functionality and O2-AC, agrass15268 for bug fixing.
