#! /usr/bin/env python
# -*- coding: utf-8 -*-

from scipy.io.wavfile import read

amostras = read('audio.wav') # Lê um arquivo de áudio wav
                             # retorna uma tupla com 2 elementos:
                             # a frequência de amostragem do sinal
                             # e um array com os valores de cada amostra
print "amostras"
print amostras
