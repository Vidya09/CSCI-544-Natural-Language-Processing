from fst import FST
import string, sys
from fsmutils import composechars, trace

def letters_to_numbers():
    """
    Returns an FST that converts letters to numbers as specified by
    the soundex algorithm
    """

    # Let's define our first FST
    f1 = FST('soundex-generate')

    # Add all states
    f1.add_state('0')
    f1.add_state('1')
    f1.add_state('2')
    f1.add_state('3')
    f1.add_state('4')
    f1.add_state('5')
    f1.add_state('6')
    f1.add_state('7')
    f1.add_state('2a')
    f1.add_state('3a')
    f1.add_state('4a')
    f1.add_state('5a')
    f1.add_state('6a')
    f1.add_state('7a')

    # Indicate that '0' is the initial state
    f1.initial_state = '0'

    # Set all the final states
    f1.set_final('1')
    f1.set_final('2')
    f1.set_final('3')
    f1.set_final('4')
    f1.set_final('5')
    f1.set_final('6')
    f1.set_final('7')
    f1.set_final('2a')
    f1.set_final('3a')
    f1.set_final('4a')
    f1.set_final('5a')
    f1.set_final('6a')
    f1.set_final('7a')

    # Define all lists
    remove_letters = ['a', 'e', 'h', 'i', 'o', 'u', 'w', 'y', 'A', 'E', 'H', 'I', 'O', 'U', 'W', 'Y']
    g1 = ['b', 'f', 'p', 'v', 'B', 'F', 'P', 'V']
    g2 = ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z', 'C', 'G', 'J', 'K', 'Q', 'S', 'X', 'Z']
    g3 = ['d', 't', 'D', 'T']
    g4 = ['l', 'L']
    g5 = ['m', 'n', 'M', 'N']
    g6 = ['r', 'R']

    # Add the rest of the arcs
    for letter in string.ascii_letters:
        # Retain the first character
        if letter in g1:
            f1.add_arc('0', '2a', (letter), (letter))
            f1.add_arc('2a', '2', (letter), ())
            f1.add_arc('3a', '2', (letter), ('1'))
            f1.add_arc('4a', '2', (letter), ('1'))
            f1.add_arc('5a', '2', (letter), ('1'))
            f1.add_arc('6a', '2', (letter), ('1'))
            f1.add_arc('7a', '2', (letter), ('1'))
            f1.add_arc('1', '2', (letter), ('1'))
            f1.add_arc('2', '2', (letter), ())
            f1.add_arc('3', '2', (letter), ('1'))
            f1.add_arc('4', '2', (letter), ('1'))
            f1.add_arc('5', '2', (letter), ('1'))
            f1.add_arc('6', '2', (letter), ('1'))
            f1.add_arc('7', '2', (letter), ('1'))

        if letter in g2:
            f1.add_arc('0', '3a', (letter), (letter))
            f1.add_arc('3a', '3', (letter), ())
            f1.add_arc('2a', '3', (letter), ('2'))
            f1.add_arc('4a', '3', (letter), ('2'))
            f1.add_arc('5a', '3', (letter), ('2'))
            f1.add_arc('6a', '3', (letter), ('2'))
            f1.add_arc('7a', '3', (letter), ('2'))
            f1.add_arc('1', '3', (letter), ('2'))
            f1.add_arc('3', '3', (letter), ())
            f1.add_arc('2', '3', (letter), ('2'))
            f1.add_arc('4', '3', (letter), ('2'))
            f1.add_arc('5', '3', (letter), ('2'))
            f1.add_arc('6', '3', (letter), ('2'))
            f1.add_arc('7', '3', (letter), ('2'))

        if letter in g3:
            f1.add_arc('0', '4a', (letter), (letter))
            f1.add_arc('4a', '4', (letter), ())
            f1.add_arc('2a', '4', (letter), ('3'))
            f1.add_arc('3a', '4', (letter), ('3'))
            f1.add_arc('5a', '4', (letter), ('3'))
            f1.add_arc('6a', '4', (letter), ('3'))
            f1.add_arc('7a', '4', (letter), ('3'))
            f1.add_arc('1', '4', (letter), ('3'))
            f1.add_arc('4', '4', (letter), ())
            f1.add_arc('2', '4', (letter), ('3'))
            f1.add_arc('3', '4', (letter), ('3'))
            f1.add_arc('5', '4', (letter), ('3'))
            f1.add_arc('6', '4', (letter), ('3'))
            f1.add_arc('7', '4', (letter), ('3'))

        if letter in g4:
            f1.add_arc('0', '5a', (letter), (letter))
            f1.add_arc('5a', '5', (letter), ())
            f1.add_arc('2a', '5', (letter), ('4'))
            f1.add_arc('3a', '5', (letter), ('4'))
            f1.add_arc('4a', '5', (letter), ('4'))
            f1.add_arc('6a', '5', (letter), ('4'))
            f1.add_arc('7a', '5', (letter), ('4'))
            f1.add_arc('1', '5', (letter), ('4'))
            f1.add_arc('5', '5', (letter), ())
            f1.add_arc('2', '5', (letter), ('4'))
            f1.add_arc('3', '5', (letter), ('4'))
            f1.add_arc('4', '5', (letter), ('4'))
            f1.add_arc('6', '5', (letter), ('4'))
            f1.add_arc('7', '5', (letter), ('4'))

        if letter in g5:
            f1.add_arc('0', '6a', (letter), (letter))
            f1.add_arc('6a', '6', (letter), ())
            f1.add_arc('2a', '6', (letter), ('5'))
            f1.add_arc('3a', '6', (letter), ('5'))
            f1.add_arc('4a', '6', (letter), ('5'))
            f1.add_arc('5a', '6', (letter), ('5'))
            f1.add_arc('7a', '6', (letter), ('5'))
            f1.add_arc('1', '6', (letter), ('5'))
            f1.add_arc('6', '6', (letter), ())
            f1.add_arc('2', '6', (letter), ('5'))
            f1.add_arc('3', '6', (letter), ('5'))
            f1.add_arc('4', '6', (letter), ('5'))
            f1.add_arc('5', '6', (letter), ('5'))
            f1.add_arc('7', '6', (letter), ('5'))

        if letter in g6:
            f1.add_arc('0', '7a', (letter), (letter))
            f1.add_arc('7a', '7', (letter), ())
            f1.add_arc('2a', '7', (letter), ('6'))
            f1.add_arc('3a', '7', (letter), ('6'))
            f1.add_arc('4a', '7', (letter), ('6'))
            f1.add_arc('5a', '7', (letter), ('6'))
            f1.add_arc('6a', '7', (letter), ('6'))
            f1.add_arc('1', '7', (letter), ('6'))
            f1.add_arc('7', '7', (letter), ())
            f1.add_arc('2', '7', (letter), ('6'))
            f1.add_arc('3', '7', (letter), ('6'))
            f1.add_arc('4', '7', (letter), ('6'))
            f1.add_arc('5', '7', (letter), ('6'))
            f1.add_arc('6', '7', (letter), ('6'))

        # Remove letters
        if letter in remove_letters:
            f1.add_arc('0', '1', (letter), (letter))
            f1.add_arc('1', '1', (letter), ())
            f1.add_arc('2a', '1', (letter), ())
            f1.add_arc('3a', '1', (letter), ())
            f1.add_arc('4a', '1', (letter), ())
            f1.add_arc('5a', '1', (letter), ())
            f1.add_arc('6a', '1', (letter), ())
            f1.add_arc('7a', '1', (letter), ())
            f1.add_arc('2', '1', (letter), ())
            f1.add_arc('3', '1', (letter), ())
            f1.add_arc('4', '1', (letter), ())
            f1.add_arc('5', '1', (letter), ())
            f1.add_arc('6', '1', (letter), ())
            f1.add_arc('7', '1', (letter), ())

    return f1
    # The stub code above converts all letters except the first into '0'.
    # How can you change it to do the right conversion?



def truncate_to_three_digits():
    """
    Create an FST that will truncate a soundex string to three digits
    """
    # Ok so now let's do the second FST, the one that will truncate
    # the number of digits to 3
    f2 = FST('soundex-truncate')

    # Indicate initial and final states
    f2.add_state('1')
    f2.add_state('2')
    f2.add_state('3')
    f2.add_state('4')

    f2.initial_state = '1'

    f2.set_final('1')
    f2.set_final('2')
    f2.set_final('3')
    f2.set_final('4')

    # Add the arcs
    for letter in string.letters:
        f2.add_arc('1', '1', (letter), (letter))

    for number in string.digits:
        f2.add_arc('1', '2', (number), (number))
        f2.add_arc('2', '3', (number), (number))
        f2.add_arc('3', '4', (number), (number))
        f2.add_arc('4', '4', (number), ())

    #for n in range(3):
    #    f2.add_arc('1', '1', str(n), str(n))

    return f2
    # The above stub code doesn't do any truncating at all -- it passes letter and number input through
    # what changes would make it truncate digits to 3?



def add_zero_padding():
    # Now, the third fst - the zero-padding fst
    f3 = FST('soundex-padzero')

    # Indicate initial and final states
    f3.add_state('1')
    f3.add_state('1a')
    f3.add_state('1b')
    f3.add_state('2')

    f3.initial_state = '1'
    f3.set_final('2')

    # Add the arcs
    for letter in string.letters:
        f3.add_arc('1', '1', (letter), (letter))

    for number in string.digits:
        f3.add_arc('1', '1a', (number), (number))
        f3.add_arc('1a', '1b', (number), (number))
        f3.add_arc('1b', '2', (number), (number))

    f3.add_arc('1', '2', (), ('000'))
    f3.add_arc('1a', '2', (), ('00'))
    f3.add_arc('1b', '2', (), ('0'))
    return f3

if __name__ == '__main__':
    f1 = letters_to_numbers()
    f2 = truncate_to_three_digits()
    f3 = add_zero_padding()

    user_input = raw_input().strip()

    if user_input:
        print("%s -> %s" % (user_input, composechars(tuple(user_input), f1, f2, f3)))

"""
f1 = letters_to_numbers()
S = ['a', 'i', 's', 'q', 'i', 't', 'h']
result_f1 = f1.transduce(S)
print ''.join(result_f1)
#trace(f1, S)

f2 = truncate_to_three_digits()
result_f2 = f2.transduce(result_f1)
print ''.join(result_f2)
print " "
#trace(f2, result_f1)

f3 = add_zero_padding()
result_f3 = f3.transduce(result_f2)
print ''.join(result_f3)
print " "
#trace(f3, result_f2)
"""