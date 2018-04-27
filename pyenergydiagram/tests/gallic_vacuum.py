from energydiagram import ED
from matplotlib.backends.backend_pdf import PdfPages
 
diagram = ED()
diagram.add_level(-646.499346248,'Closed Shell Molecule')

diagram.add_level(-645.842343146,'C3 unrelaxed')
diagram.add_level(-645.852575856,'C4 unrelaxed','last')
diagram.add_level(-645.852440887,'C5 unrelaxed','last')

diagram.add_level(-645.866923481,'C3 relaxed',)
diagram.add_level(-645.868512298,'C4 relaxed','last')
diagram.add_level(-645.866256558,'C5 relaxed','last')

diagram.add_link(0,1)
diagram.add_link(0,2)
diagram.add_link(0,3)
diagram.add_link(1,4)
diagram.add_link(2,5)
diagram.add_link(3,6)
 
diagram.plot(show_IDs=True)    
my_fig = diagram.fig
 