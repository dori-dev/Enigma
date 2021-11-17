"""Generate the rotor for enigma machin
"""

from random import shuffle
from pickle import dump
from string import ascii_lowercase as ALPHABET
ALPHABET += ' '


def create_rotor() -> str:
    """make rotor

    Returns:
        str: rotor alphabet(random)
    """
    rotor = list(ALPHABET)
    shuffle(rotor)
    return ''.join(rotor)


ROTOR1 = create_rotor()

ROTOR2 = create_rotor()

ROTOR3 = create_rotor()

with open('./rotor_state.enigma', 'wb') as file:
    dump((ROTOR1, ROTOR2, ROTOR3), file)
