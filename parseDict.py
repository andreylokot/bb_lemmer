import codecs
from sets import Set
f = codecs.open('xn_alkona_general_es-es.dsl', 'r', encoding='iso-8859-15')
sust = Set() # for uniqueness
adj = Set()
verb = Set()
current_word = ""

for line in f:
  if line[0] != '\t':
    current_word = line
  if line[1:8] == '[m2][p]':
    if 'sust.' in line:
      sust.add(current_word)
    if 'verbo' in line:
      verb.add(current_word)
    if 'adj.' in line:
      adj.add(current_word)

f.close()
      
sust_file = codecs.open('sust.txt', 'w', 'utf-8')
for w in sust:
  sust_file.write(w)
sust_file.close()
verb_file = codecs.open('verb.txt', 'w', 'utf-8')
for w in verb:
  verb_file.write(w)
verb_file.close()
adj_file = codecs.open('adj.txt', 'w', 'utf-8')
for w in adj:
  adj_file.write(w)
adj_file.close()
