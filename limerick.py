#!/usr/bin/env python
import argparse
import sys
import codecs
if sys.version_info[0] == 2:
  from itertools import izip
else:
  izip = zip
from collections import defaultdict as dd
import re
import os.path
import gzip
import tempfile
import shutil
import atexit
import string

# Use word_tokenize to split raw text into words
from string import punctuation

import nltk
#nltk.download()
from nltk.tokenize import word_tokenize
# from nltk.tokenize import

scriptdir = os.path.dirname(os.path.abspath(__file__))

reader = codecs.getreader('utf8')
writer = codecs.getwriter('utf8')

def prepfile(fh, code):
    if type(fh) is str:
        fh = open(fh, code)
    ret = gzip.open(fh.name, code if code.endswith("t") else code+"t") if fh.name.endswith(".gz") else fh
    if sys.version_info[0] == 2:
        if code.startswith('r'):
            ret = reader(fh)
        elif code.startswith('w'):
            ret = writer(fh)
        else:
            sys.stderr.write("I didn't understand code "+code+"\n")
            sys.exit(1)
    return ret

def addonoffarg(parser, arg, dest=None, default=True, help="TODO"):
    ''' add the switches --arg and --no-arg that set parser.arg to true/false, respectively'''
    group = parser.add_mutually_exclusive_group()
    dest = arg if dest is None else dest
    group.add_argument('--%s' % arg, dest=dest, action='store_true', default=default, help=help)
    group.add_argument('--no-%s' % arg, dest=dest, action='store_false', default=default, help="See --%s" % arg)


class LimerickDetector:
    def __init__(self):
        """
        Initializes the object to have a pronunciation dictionary available
        """
        self._pronunciations = dict(nltk.corpus.cmudict.dict())


    def apostrophe_tokenize(self, sentence):
        return re.split("[\.!,\?;: ]", sentence)

    def num_syllables(self, word):
        """
        Returns the number of syllables in a word.  If there's more than one
        pronunciation, take the shorter one.  If there is no entry in the
        dictionary, return 1.
        """
        if self._pronunciations.has_key(word):
            return min([len(list(y for y in x if y[-1].isdigit())) for x in self._pronunciations[word.lower()]])
        else:
            return 1


    def rhymes(self, a, b):
        """
        Returns True if two words (represented as lower-case strings) rhyme,
        False otherwise.
        """
        pronunciations_a = []
        for word, pron in self._pronunciations.items():
            if word == a:
                pronunciations_a = pron

        if pronunciations_a is None:
            return False

        pronunciations_b = []
        for word, pron in self._pronunciations.items():
            if word == b:
                pronunciations_b = pron

        if pronunciations_b is None:
            return False

        pronun_a = []
        for diff_pron in pronunciations_a:
            for pron in diff_pron:
                if (pron[-1]) in ['0', '1', '2']:
                    index = diff_pron.index(pron)
                    pron_str = ''.join(map(str, diff_pron[index:]))
                    pronun_a.append(pron_str)
                    break

        pronun_b = []
        for diff_pron in pronunciations_b:
            for pron in diff_pron:
                if (pron[-1]) in ['0', '1', '2']:
                    index = diff_pron.index(pron)
                    pron_str = ''.join(map(str, diff_pron[index:]))
                    pronun_b.append(pron_str)
                    break

        for pron_a in pronun_a:
            for pron_b in pronun_b:
                if len(pron_a) < len(pron_b):
                    if pron_b.endswith(pron_a):
                        return True
                elif len(pron_b) < len(pron_a):
                    if pron_a.endswith(pron_b):
                        return  True
                elif len(pron_a) == len(pron_b):
                    if pron_a == pron_b:
                        return True

        return False


    def is_limerick(self, text):
        """
        Takes text where lines are separated by newline characters.  Returns
        True if the text is a limerick, False otherwise.

        A limerick is defined as a poem with the form AABBA, where the A lines
        rhyme with each other, the B lines rhyme with each other, and the A lines do not
        rhyme with the B lines.

        Additionally, the following syllable constraints should be observed:
          * No two A lines should differ in their number of syllables by more than two.
          * The B lines should differ in their number of syllables by no more than two.
          * Each of the B lines should have fewer syllables than each of the A lines.
          * No line should have fewer than 4 syllables

        (English professors may disagree with this definition, but that's what
        we're using here.)
        """
        lines = text.strip().split("\n")

        if len(lines) is not 5:
            return False

        line_count = 1
        punctuations_to_delete = set(string.punctuation)
        dict = {}

        for line in lines:
            line_strip = line.strip()
            words = nltk.word_tokenize(line_strip)
            # words = self.apostrophe_tokenize(line_strip)

            words = [x for x in words if x and x not in punctuations_to_delete]
            last_word = words[-1].lower()

            if line_count == 1 or line_count == 2 or line_count == 5:
                line_group = 'A'
            else:
                line_group = 'B'

            syllables_in_line = 0;
            for word in words:
                syllables_in_token = self.num_syllables(word.lower())
                syllables_in_line = syllables_in_line + syllables_in_token

            dict[line_count] = [line_group, syllables_in_line, last_word]
            line_count = line_count + 1


        # Limerick Check
        groupA_word1 =  dict.get(1)[2]
        groupA_word2 = dict.get(2)[2]
        groupA_word3 =  dict.get(5)[2]
        groupB_word1 = dict.get(3)[2]
        groupB_word2 = dict.get(4)[2]

        syllables_line1 = dict.get(1)[1]
        syllables_line2 = dict.get(2)[1]
        syllables_line3 = dict.get(3)[1]
        syllables_line4 = dict.get(4)[1]
        syllables_line5 = dict.get(5)[1]

        # Check rhymming
        if self.rhymes(groupA_word1, groupA_word2) and self.rhymes(groupA_word2, groupA_word3) and self.rhymes(groupA_word1, groupA_word3) and self.rhymes(groupB_word1, groupB_word2):

            # Check if no of syllables of all line >=4
            if syllables_line1 >= 4 and syllables_line2 >=4 and syllables_line3 >= 4 and syllables_line4 >= 4 and syllables_line5 >= 4:

                # Check if syllables of group B is always less than each of the lines of group A
                if syllables_line3 < syllables_line1 and syllables_line3 < syllables_line2 and syllables_line3 < syllables_line5 and  syllables_line4 < syllables_line1 and syllables_line4 <syllables_line2 and syllables_line4 < syllables_line5:

                    # Check if group A syllables differ by less than 2
                    if syllables_line1 - syllables_line2 <= 2 and syllables_line2 - syllables_line5 <= 2 and syllables_line1 - syllables_line5 <= 2:

                        # Check if group B syllables differ by less than 2
                        if syllables_line3 - syllables_line4 <= 2:
                            return True
        return False


# The code below should not need to be modified
def main():
    parser = argparse.ArgumentParser(description="limerick detector. Given a file containing a poem, indicate whether that poem is a limerick or not",
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    addonoffarg(parser, 'debug', help="debug mode", default=False)
    parser.add_argument("--infile", "-i", nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="input file")
    parser.add_argument("--outfile", "-o", nargs='?', type=argparse.FileType('w'), default=sys.stdout, help="output file")

    try:
        args = parser.parse_args()
    except IOError as msg:
        parser.error(str(msg))

    infile = prepfile(args.infile, 'r')
    outfile = prepfile(args.outfile, 'w')

    ld = LimerickDetector()
    lines = ''.join(infile.readlines())

    #lines = """I wish I had thought of a rhyme
    #Before I ran all out of time!
    #I'll sit here instead
    #A cloud on my head
    #That rains 'til I'm covered with slime."""

    outfile.write("{}\n-----------\n{}\n".format(lines.strip(), ld.is_limerick(lines)))

if __name__ == '__main__':
    main()
