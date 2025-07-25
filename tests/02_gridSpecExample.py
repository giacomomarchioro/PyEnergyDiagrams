import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
plt.rcParams.update({'font.size': 8})
fig = plt.figure(figsize=(7,7))
fig.suptitle("Example multiple Energy Diagrams using GridSpec")

gs = GridSpec(3, 1, height_ratios=[1,1,1], width_ratios=None, wspace=0)
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])
ax3 = fig.add_subplot(gs[2])


from energydiagram import ED
diagram = ED()
diagram.add_level(0,'Sep.')
diagram.add_level(-5.4,'mlC1')
diagram.add_level(-15.6,'mlC2','last',) #Using 'last'  or 'l' it will be together with the previous level
diagram.add_level(28.5,'mTS1',color='g')
diagram.add_level(-9.7,'mCARB1')
diagram.add_level(-19.8,'mCARB2','l')
diagram.add_level(20,'mCARBX','last')
diagram.plot(show_IDs=True,ax=ax1)

diagram2 = ED()
diagram2.add_level(0,'Sep.')
diagram2.add_level(-5.4,'mlC1')
diagram2.add_level(-15.6,'mlC2','last',) #Using 'last'  or 'l' it will be together with the previous level
diagram2.add_level(28.5,'mTS1',color='g')
diagram2.add_level(-9.7,'mCARB1')
diagram2.add_level(-19.8,'mCARB2','l')
diagram2.add_level(20,'mCARBX','last')
diagram2.plot(show_IDs=True,ax=ax2)

diagram3 = ED()
diagram3.add_level(0,'Sep.')
diagram3.add_level(-5.4,'mlC1')
diagram3.add_level(-15.6,'mlC2','last',) #Using 'last'  or 'l' it will be together with the previous level
diagram3.add_level(28.5,'mTS1',color='g')
diagram3.add_level(-9.7,'mCARB1')
diagram3.add_level(-19.8,'mCARB2','l')
diagram3.add_level(20,'mCARBX','last')
diagram3.plot(show_IDs=True,ax=ax3)

plt.show()