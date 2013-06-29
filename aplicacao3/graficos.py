#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Aplicação 4 - Filtragem

import numpy as np
import scipy.io.wavfile
import scipy.signal
import matplotlib.pyplot as plt

# Lê um arquivo wav
audio = scipy.io.wavfile.read('audio60.wav')
fa = audio[0] # frequência de amostragem
audio_orig = audio[1] # amostras

audio2 = scipy.io.wavfile.read('audiofilt.wav')
fa2 = audio2[0] # frequência de amostragem
audio_filt = audio2[1] # amostras

# Lê um arquivo numpy com parâmetros A e B do filtro
npzfile = np.load('H.npz')
A = npzfile['A']
B = npzfile['B']

# Plota resposta em frequência
(w,H) = scipy.signal.freqz(B,A,100000)

plt.figure()
f = (w/(2*np.pi))*fa
GdB = 20*np.log10(np.abs(H))
plt.plot(f,GdB)
plt.xlabel('f (Hz)')
plt.ylabel('Ganho (dB)')
plt.show()

# Plota sinais de áudio
plt.figure()
plt.subplot(2,1,1)
plt.plot(audio_orig)
plt.title('Original')
plt.subplot(2,1,2)
plt.plot(audio_filt)
plt.title('Filtrado')
plt.show()
