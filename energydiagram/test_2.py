#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 11:45:00 2018

@author: opdate
"""

from energydiagram import ED

diagram = ED()
diagram.add_level(0 + 0 + 1,'$n_x = 0$ \n $n_y = 0$',right_text='test' )
diagram.add_level(1 + 0 + 1,'$n_x = 1$ \n $n_y = 0$')
diagram.add_level(0 + 1 + 1,'$n_x = 0$ \n $n_y = 1$')
diagram.add_level(2 + 0 + 1,'$n_x = 2$ \n $n_y = 0$')
diagram.add_level(1 + 1 + 1,'$n_x = 1$ \n $n_y = 1$')
diagram.add_level(0 + 2 + 1,'$n_x = 0$ \n $n_y = 2$')
diagram.add_level(3 + 0 + 1,'$n_x = 3$ \n $n_y = 0$')
diagram.add_level(2 + 1 + 1,'$n_x = 2$ \n $n_y = 1$')
diagram.add_level(1 + 2 + 1,'$n_x = 1$ \n $n_y = 2$')
diagram.add_level(0 + 3 + 1,'$n_x = 0$ \n $n_y = 3$')
diagram.plot()

