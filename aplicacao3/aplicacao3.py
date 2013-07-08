#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Aplicação 3 - Filtragem

import numpy as np
import scipy.io.wavfile
import scipy.signal

# Lê um arquivo wav
audio = scipy.io.wavfile.read('audio60.wav')
fa = audio[0] # frequência de amostragem
audio_orig = audio[1] # amostras

# Lê um arquivo numpy com parâmetros A e B do filtro
npzfile = np.load('H.npz')
A = npzfile['A']
B = npzfile['B']
print "A"
print A
print "B"
print B

# Filtra o sinal de áudio usando um filtro linear
# com parâmetros A e B
audio_filt = scipy.signal.lfilter(B, A, audio_orig)

# Quantização
audio_filt_q = audio_filt.astype('int16')

# Grava um arquivo wav
scipy.io.wavfile.write('audiofilt.wav', fa, audio_filt_q)
