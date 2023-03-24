

Búið til af Arnóri Þorleifssyni aka. NoriThorleifs

usage: lykilord.py [-h] [-s SNIÐ]

Býr til ný lykilorð af handahófi

options:
  -h, --help            show this help message and exit
  -s SNIÐ, --snið SNIÐ  Ræður sniði og röðun lykilorðsins, 'o' býr til orð sem eru með stóran staf í fyrsta. 'n' býr
                        til tölustaf frá 0 til 9. '.' bætir við punkti. Sniðið verður 'oo.nn' ef ekkert er valið.

Dæmi um notkun:

python .\lykilord.py
FerdaflangsEggjasjoda.81

python .\lykilord.py -s o.o.n.n
Midfastan.Raftholtsmyrarsund.5.7

python .\lykilord.py -s nnnn
4570

Auk þess má flytja skjalið í þitt egið verkefni.

from lykilord import lykilorðaGerðin 
print(lykilorðaGerðin("ooo"))
