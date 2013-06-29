#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Aplicação 1 - Síntese de áudio

import numpy as np
import scipy.io.wavfile

# Frequência de amostragem
fa = 44100

# Frequência do sinal senoidal
f = 440

# Índices n de 0 a 44100*2-1
n = np.arange(fa*2)

# Gera o sinal
sinal = 10000*np.sin(2*np.pi*f/fa*n)

# Converte para 16 bits por amostra
sinalq = sinal.astype(np.int16) 

# Grava arquivo wav
scipy.io.wavfile.write('som.wav', fa, sinalq)

