#!/usr/bin/python

import codecs
f = codecs.open('xn_alkona_general_es-es.dsl', 'r', encoding='iso-8859-15')
sust = set() # for uniqueness
adj = set()
verb = set()
current_word = ""

for line in f:
  if line[0] != '\t':
    line = line.strip()
    if line and ' ' not in line:
      current_word = line
  elif line[1:8] == '[m2][p]':
    if 'sust.' in line:
      sust.add(current_word)
    if 'verbo' in line:
      if current_word.endswith('se'):
        current_word = current_word[:-2]
      verb.add(current_word)
    if 'adj.' in line:
      adj.add(current_word)

f.close()
      
sust_file = codecs.open('words.N.txt', 'wb', 'utf-8')
for w in sust:
  sust_file.write(w + '\n')
sust_file.close()
verb_file = codecs.open('words.V.txt', 'wb', 'utf-8')
for w in verb:
  verb_file.write(w + '\n')
verb_file.close()
adj_file = codecs.open('words.A.txt', 'wb', 'utf-8')
for w in adj:
  adj_file.write(w + '\n')
adj_file.close()
