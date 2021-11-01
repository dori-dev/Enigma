"""generate the rotor for enigma machin
"""

from random import shuffle
from pickle import dump
from string import ascii_lowercase as ALPHABET
ALPHABET += ' '

r1 = list(ALPHABET)
shuffle(r1)
ROTOR1 = ''.join(r1)

r2 = list(ALPHABET)
shuffle(r2)
ROTOR2 = ''.join(r2)

r3 = list(ALPHABET)
shuffle(r3)
ROTOR3 = ''.join(r3)

with open('./rotor_state.enigma', 'wb') as file:
    dump((ROTOR1, ROTOR2, ROTOR3), file)
