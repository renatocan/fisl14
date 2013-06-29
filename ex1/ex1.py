#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
vzeros = np.zeros(10) # cria um vetor com 10 zeros
print "vzeros"
print vzeros
x = np.linspace(0, 2*np.pi, 10) # cria um vetor com 10 elementos
                                # entre 0 e 2pi
                                # linearmente espaçados
print "x"
print x
senox = np.sin(x)               # cria um vetor senox com o mesmo
                                # número de elementos de x
                                # sendo cada elemento igual ao
                                # seno do respectivo elemento de x
print "senox"
print senox
