"""Code and decode the message
"""
from pickle import load
from string import ascii_lowercase as ALPHABET
ALPHABET += ' '

with open('./rotor_state.enigma', 'rb') as file:
    ROTOR1, ROTOR2, ROTOR3 = load(file)


def reflector(character: str) -> str:
    """reflected the letter in alphabet, examples:
        inp: a
        out: z
        ------
        inp: c
        out: x
        ------

    Args:
        character (str): character will reflected

    Returns:
        str: reflected character
    """
    return ALPHABET[-ALPHABET.index(character)-1]


def front_rotors(char_list: list, char: str) -> str:
    """get front of rotors characters

    Args:
        char (str): character in front
        char_list (list): character list in back

    Returns:
        str: character in index of char_list from front character list(ALPHABET)
    """
    return char_list[ALPHABET.index(char)]


def back_rotors(char_list: list, char: str) -> str:
    """get back of rotors characters

    Args:
        char (str): character in back
        char_list (list): character list in back

    Returns:
        str: character in index of front character list(ALPHABET) from char_list
    """
    return ALPHABET[char_list.index(char)]


def enigma_one_char(character: str) -> str:
    """enigma machin, get character the got to rotor1, 2 and 3 then reflected character and
    got it from back in rotor3, 2 and 1

    Args:
        character (str): character input

    Returns:
        str: final character
    """
    char1 = front_rotors(ROTOR1, character)
    char2 = front_rotors(ROTOR2, char1)
    char3 = front_rotors(ROTOR3, char2)

    reflected = reflector(char3)

    char3 = back_rotors(ROTOR3, reflected)
    char2 = back_rotors(ROTOR2, char3)
    char1 = back_rotors(ROTOR1, char2)

    return char1


def rotate_rotors(rotors: tuple) -> tuple:
    """rotate the rotor1, 2 and 3

    Args:
        rotors (tuple): list of last rotors

    Returns:
        tuple: list of new rotors
    """
    last_rotor1, last_rotor2, last_rotor3 = rotors
    last_rotor1 = last_rotor1[1:] + last_rotor1[0]
    if state % 26:
        last_rotor2 = last_rotor2[1:] + last_rotor2[0]
    if state % (26*26):
        last_rotor3 = last_rotor3[1:] + last_rotor3[0]

    return last_rotor1, last_rotor2, last_rotor3


def set_rotors(my_state: int, rotors: tuple) -> tuple:
    """set the rotors with rotate_rotors function

    Args:
        my_state (int): state of rotors
        rotors (tuple): list of rotors

    Returns:
        tuple: new list of rotors
    """
    for _ in range(my_state):
        new_rotor = rotate_rotors(rotors)
    return new_rotor


def set_state(rotor1_number: int, rotor2_number: int, rotor3_number: int) -> int:
    """set state with rotors number

    Args:
        rotor1_number (int): number of rotor 1
        rotor2_number (int): number of rotor 2
        rotor3_number (int): number of rotor 3

    Returns:
        int: state number
    """
    return rotor1_number + (rotor2_number*26) + (rotor3_number*26*26)


def input_rotor_numbers() -> tuple:
    """input rotor numbers

    Returns:
        tuple: list of rotor numbers
    """
    rotor1 = int(input('rotor1: '))
    rotor2 = int(input('rotor2: '))
    rotor3 = int(input('rotor3: '))
    return rotor1, rotor2, rotor3


plain = input('enter text: ').lower()  # convert to lower character
plain = ''.join([letter for letter in plain if letter in ALPHABET])  # select valid character

if input('Do you want to set rotors(y/N)? ').lower() == 'y':
    state = set_state(*input_rotor_numbers())
    ROTOR1, ROTOR2, ROTOR3 = set_rotors(state, (ROTOR1, ROTOR2, ROTOR3))
else:
    state = 0

cipher = ''

for letter in plain:
    state += 1
    cipher += enigma_one_char(letter)
    ROTOR1, ROTOR2, ROTOR3 = rotate_rotors((ROTOR1, ROTOR2, ROTOR3))

print()
print(cipher)
