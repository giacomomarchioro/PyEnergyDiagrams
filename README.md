# PyEnergyDiagrams
This is a simple script to plot energy profile diagrams using Python and matplotlib.

![alt tag](https://github.com/giacomomarchioro/PyEnergyDiagrams/blob/master/md_images/Final.png)
## Requirments
  > [matplotlib](http://matplotlib.org/users/installing.html)
  
## How to use it?

Put your script in your Python path.

```python
from energydiagram import ED
diagram = ED()
diagram.add_level(0,'Separated Reactants')
diagram.add_level(-5.4,'mlC1')
diagram.add_level(-15.6,'mlC2','last',) #Using 'last' it will be together with the previous level
diagram.add_level(28.5,'mTS1',color='g')
diagram.add_level(-9.7,'mCARB1')
diagram.add_level(-19.8,'mCARB2','last')
diagram.add_level(20,'mCARBX','last')
```
Show the IDs (red numbers) for understanding how to link the levels:

```python
diagram.plot(show_IDs=True)
```
![alt tag](https://github.com/giacomomarchioro/PyEnergyDiagrams/blob/master/With_IDs.png)

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
diagram.plot()
```
The results is displayed above.
## Trouble shooting and fine tuning
Most of the times there could be a problem of test padding. There are some parameters that can be changed in this way.
```python
diagram.offset = 10
```
![alt tag](https://github.com/giacomomarchioro/PyEnergyDiagrams/blob/master/md_images/Explained.jpg)

If you dont' see anything try:
```python
import matplotlib.pyplot as plt
plt.show()
```
