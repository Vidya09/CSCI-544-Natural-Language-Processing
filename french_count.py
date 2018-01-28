import sys
from fst import FST
import string
from fsmutils import composewords, trace

kFRENCH_TRANS = {0: "zero", 1: "un", 2: "deux", 3: "trois", 4:
                 "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit",
                 9: "neuf", 10: "dix", 11: "onze", 12: "douze", 13:
                 "treize", 14: "quatorze", 15: "quinze", 16: "seize",
                 20: "vingt", 30: "trente", 40: "quarante", 50:
                 "cinquante", 60: "soixante", 100: "cent"}

kFRENCH_AND = 'et'

def prepare_input(integer):
    assert isinstance(integer, int) and integer < 1000 and integer >= 0, \
      "Integer out of bounds"
    list_digits = list("%03i" % integer)
    number = str(''.join(map(str, list_digits)))
    return number
    #return list("%03i" % integer)

def french_count():
    f = FST('french')

    # Add states
    f.add_state('0')
    f.add_state('1')
    f.add_state('2')
    f.add_state('3')
    f.add_state('4')
    f.add_state('5')
    f.add_state('6')
    f.add_state('7')
    f.add_state('8')
    f.add_state('9')
    f.add_state('10')

    # Initial State
    f.initial_state = '0'

    # Final State
    f.set_final('3')

    # Number groups
    zero = ['0']
    zero_to_nine = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    one = ['1']
    one_to_six = ['1', '2', '3', '4', '5', '6']
    one_to_nine = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    two_to_six = ['2', '3', '4', '5', '6']
    two_to_nine = ['2', '3', '4', '5', '6', '7', '8', '9']
    seven = ['7']
    seven_to_nine = ['7', '8', '9']
    eight = ['8']
    nine = ['9']

    # Add the rest of the arcs
    for digit in string.digits:
        if digit in zero:
            f.add_arc('0', '1', (digit), ())
            f.add_arc('1', '2', (digit), ())
            f.add_arc('4', '3', (digit), [kFRENCH_TRANS[10]])
            f.add_arc('5', '3', (digit), ())
            f.add_arc('4', '3', (digit), [kFRENCH_TRANS[10]])
            f.add_arc('6', '3', (digit), [kFRENCH_TRANS[10]])
            f.add_arc('7', '3', (digit), ())
            f.add_arc('8', '3', (digit), [kFRENCH_TRANS[10]])
            #f.add_arc('9', '10', (digit), ())
            f.add_arc('10', '3', (digit), ())

        if digit in zero_to_nine:
            f.add_arc('2', '3', (digit), [kFRENCH_TRANS[int(digit)]])

        if digit in one:
            f.add_arc('1', '4', (digit), ())
            f.add_arc('0', '9', (digit), [kFRENCH_TRANS[int(100)]])
            f.add_arc('5', '3', (digit), [kFRENCH_AND + " " + kFRENCH_TRANS[int(digit)]])
            f.add_arc('6', '3', (digit), [kFRENCH_AND + " " + kFRENCH_TRANS[int("1" + digit)]])

        if digit in one_to_six:
            f.add_arc('4', '3', (digit), [kFRENCH_TRANS[int("1" + digit)]])
            f.add_arc('8', '3', (digit), [kFRENCH_TRANS[int("1" + digit)]])

        if digit in one_to_nine:
            f.add_arc('7', '3', (digit), [kFRENCH_TRANS[int(digit)]])
            f.add_arc('9', '1', (), ())

        if digit in two_to_six:
            f.add_arc('1', '5', (digit), [kFRENCH_TRANS[int(digit + "0")]])
            f.add_arc('6', '3', (digit), [kFRENCH_TRANS[int("1" + digit)]])

        if digit in two_to_nine:
            f.add_arc('0', '9', (digit), [kFRENCH_TRANS[int(digit)] + " " + kFRENCH_TRANS[100]])
            f.add_arc('5', '3', (digit), [kFRENCH_TRANS[int(digit)]])

        if digit in seven_to_nine:
            f.add_arc('4', '3', (digit), [kFRENCH_TRANS[10] + " " + kFRENCH_TRANS[int(digit)]])
            f.add_arc('6', '3', (digit), [kFRENCH_TRANS[10] + " " + kFRENCH_TRANS[int(digit)]])
            f.add_arc('8', '3', (digit), [kFRENCH_TRANS[10] + " " + kFRENCH_TRANS[int(digit)]])

        if digit in seven:
            f.add_arc('1', '6', (digit), [kFRENCH_TRANS[60]])

        if digit in eight:
            f.add_arc('1', '7', (digit), [kFRENCH_TRANS[4] + " " + kFRENCH_TRANS[20]])

        if digit in nine:
            f.add_arc('1', '8', (digit), [kFRENCH_TRANS[4] + " " + kFRENCH_TRANS[20]])

    f.add_arc('9', '10', ('0'), ())
    return f

if __name__ == '__main__':
    string_input = raw_input()
    user_input = int(string_input)
    f = french_count()
    if string_input:
        print user_input, '-->',
        print " ".join(f.transduce(prepare_input(user_input)))