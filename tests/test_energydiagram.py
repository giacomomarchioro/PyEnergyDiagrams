import unittest
from energydiagram import ED

class TestED(unittest.TestCase):
    def setUp(self):
        self.ed = ED()
    
    def test_add_level(self):
        self.ed.add_level(0, 'Reactant')
        self.assertEqual(len(self.ed.energies), 1)
        self.assertEqual(self.ed.energies[0], 0)
        self.assertEqual(self.ed.bottom_texts[0], 'Reactant')
    
    def test_add_arrow(self):
        self.ed.add_level(0)
        self.ed.add_level(10)
        self.ed.add_arrow(0, 1)
        self.assertEqual(len(self.ed.arrows[0]), 1)
        self.assertEqual(self.ed.arrows[0][0][0], 1)
    
    def test_add_link(self):
        self.ed.add_level(0)
        self.ed.add_level(10)
        self.ed.add_link(0, 1)
        self.assertEqual(len(self.ed.links[0]), 1)
        self.assertEqual(self.ed.links[0][0][0], 1)
    
    def test_plot(self):
        self.ed.add_level(0)
        self.ed.add_level(10)
        try:
            self.ed.plot()
        except Exception as e:
            self.fail(f"plot() raised {e}")

if __name__ == '__main__':
    unittest.main()