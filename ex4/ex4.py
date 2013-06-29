#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 1000) # Mais pontos -> Maior resolução
senox = np.sin(x)

plt.figure()                      # Cria uma figura
plt.plot(x,senox)                 # Faz o gráfico de x por senox
plt.xlabel('x')                   # Label eixo X
plt.ylabel('seno(x)')             # Label eixo Y
plt.title('Exemplo Matplotlib')   # Título
plt.axis([0, 2*np.pi, -1.2, 1.2]) # Limites do gráfico
plt.grid()                        # Mostra grade
plt.show()                        # Mostra o gráfico
