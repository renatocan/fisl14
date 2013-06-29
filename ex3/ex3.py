#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 10)
senox = np.sin(x)

plt.figure()       # Cria uma figura
plt.plot(x,senox)  # Faz o gráfico de x por senox
plt.show()         # Mostra o gráfico

plt.savefig('figPlotEx3.eps', bbox_inches='tight') # salva um arquivo com o gráfico




