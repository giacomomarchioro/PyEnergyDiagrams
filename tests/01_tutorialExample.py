from energydiagram import ED
import matplotlib.pyplot as plt
from pathlib import Path

a = ED()
a.round_energies_at_digit = 2
a.bottom_text_fontsize = 'small'
a.top_text_fontsize = 'small'
a.offset = 2
a.add_level(0, 'Separated\nReactants')
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
a.add_arrow(3, 4, position='left', color='blue')
a.add_arrow(6, 4, position='center')
a.add_arrow(5, 4, position='right', color='r')
a.plot(show_IDs=True)
output_path = Path("..") / "fixtures" / "Final.png"
plt.savefig(output_path,dpi=400)
