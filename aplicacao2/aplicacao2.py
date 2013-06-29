#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Aplicação 2 - Notas musicais

import numpy as np
import scipy.io.wavfile

# Função para tocar um sinal senoidal de frequência f
# por um determinado tempo em segundos
def tocaseno(f, tempo, fa=44100):
    n = np.arange(np.floor(tempo*fa))
    sinal = 10000*np.sin(2*np.pi*f/fa*n)
    return sinal

# Frequências das notas musicais da oitava chamada de 0
fnotas = {'s': 0,      # silêncio
         'do': 261.63,
         'dos': 277.18,
         're': 293.66,
         'res': 311.13,
         'mi': 329.63,
         'fa': 349.23,
         'fas': 369.99,
         'sol': 391.99,
         'sols': 415.30,
         'la': 440.00,
         'las': 466.16,
         'si': 493.88,
         }

musicaclose = (('las', 0.4, 0),
               ('do', 0.4, 1),
               ('sols', 0.4, 0),
               ('s', 0.3, 0),
               ('sols', 0.5, -1),
               ('res', 0.5, 0),
               ('s', 0.3, 0),
               ('las', 0.4, 1),
               ('do', 0.4, 2),
               ('sols', 0.4, 1),
               ('s', 0.3, 1),
               ('sols', 0.5, 0),
               ('res', 0.5, 1),
               )


# Dada uma sequência de notas com o determinado tempo e oitava,
# retorna o sinal "tocando a música"
def tocamusica(musica):
    sinalmusica = np.array([0])
    for nota in musica:
        fnota = fnotas[nota[0]]
        tnota = nota[1]
        oitava = nota[2]
        sinalnota = tocaseno(fnota*(2**oitava), tnota)
        sinalmusica = np.concatenate((sinalmusica, sinalnota))
    return sinalmusica

close = tocamusica(musicaclose)
closeq = close.astype(np.int16)

# Grava arquivo wav
fa = 44100
scipy.io.wavfile.write('close.wav', fa, closeq)

# Sinais com 8 bits
closeq8 = (close/100).astype(np.int8)

# Grava arquivo wav 8 bits
fa = 44100
scipy.io.wavfile.write('close_8.wav', fa, closeq8)
