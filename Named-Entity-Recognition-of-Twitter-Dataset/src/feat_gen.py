#!/bin/python

import string
import nltk
import re
# nltk.download()
import numpy
from nltk import cluster
from collections import defaultdict

def preprocess_corpus(train_sents):
    # Use the sentences to do whatever preprocessing you think is suitable,
    # such as counts, keeping track of rare features/words to remove, matches to lexicons,
    # loading files, and so on. Avoid doing any of this in token2features, since
    # that will be called on every token of every sentence.

    # Of course, this is an optional function.

    # Note that you can also call token2features here to aggregate feature counts, etc.


    global lexicon_dict
    lexicon_dict = defaultdict(list)

    str_person = 'PERSON'
    str_location = 'LOCATION'
    str_sports = 'SPORTS'
    str_tvshow = 'TVSHOW'
    str_product = 'PRODUCT'
    str_company = 'COMPANY'
    str_facility = 'FACILITY'
    str_musicartist = 'MUSICARTIST'

    # Stopwords
    global stopwords
    stopwords = {}
    stopwords_lexicon = open('data/lexicon/english.stop', 'r')
    for line in stopwords_lexicon:
        stopwords[line.strip()] = 'STOPWORD'


    # PERSON
    # people.person
    people_person = open('data/lexicon/people.person', 'r')
    for line in people_person:
        x = line.strip().lower().split()
        for w in x:
            if lexicon_dict.has_key(w) and str_person in lexicon_dict[w]:
                pass
            else:
                lexicon_dict[w].append(str_person)

    # people.person.lastnames
    people_person_lastnames = open('data/lexicon/people.person.lastnames', 'r')
    for line in people_person_lastnames:
        x = line.strip().lower()
        if lexicon_dict.has_key(x) and str_person in lexicon_dict[x]:
            pass
        else:
            lexicon_dict[x].append(str_person)

    # people.family_name
    people_family_name = open('data/lexicon/people.family_name', 'r')
    for line in people_family_name:
        x = line.strip().lower()
        if lexicon_dict.has_key(x) and str_person in lexicon_dict[x]:
            pass
        else:
            lexicon_dict[x].append(str_person)


    # firstname.1000
    # firstname_1000 = open('data/lexicon/firstname.1000', 'r')
    # for line in firstname_1000:
    #     x = line.strip().lower()
    #     if lexicon_dict.has_key(x) and str_person in lexicon_dict[x]:
    #         pass
    #     else:
    #         lexicon_dict[x].append(str_person)

    # lastname.5000
    # lastname_5000 = open('data/lexicon/lastname.5000', 'r')
    # for line in lastname_5000:
    #     x = line.strip().lower()
    #     if lexicon_dict.has_key(x) and str_person in lexicon_dict[x]:
    #         pass
    #     else:
    #         lexicon_dict[x].append(str_person)

    # LOCATION
    # location
    location = open('data/lexicon/location', 'r')
    for line in location:
        x = line.strip().lower()
        if lexicon_dict.has_key(x) and str_location in lexicon_dict[x]:
            pass
        else:
            lexicon_dict[x].append(str_location)

    # location.country
    location_country = open('data/lexicon/location.country', 'r')
    for line in location_country:
        x = line.strip().lower()
        if lexicon_dict.has_key(x) and str_location in lexicon_dict[x]:
            pass
        else:
            lexicon_dict[x].append(str_location)


    # SPORTS TEAM
    sports_team = open('data/lexicon/sports.sports_team', 'r')
    for line in sports_team:
        x = line.strip().lower().split()
        for w in x:
            if lexicon_dict.has_key(w) and str_sports in lexicon_dict[w]:
                pass
            else:
                lexicon_dict[w].append(str_sports)


    # TV SHOW
    tv_program = open('data/lexicon/tv.tv_program', 'r')
    for line in tv_program:
        x = line.strip().lower().split()
        for w in x:
            if lexicon_dict.has_key(w) and str_tvshow in lexicon_dict[w]:
                pass
            else:
                lexicon_dict[w].append(str_tvshow)

    # PRODUCT
    product = open('data/lexicon/product', 'r')
    for line in product:
        x = line.strip().lower().split()
        for w in x:
            if lexicon_dict.has_key(w) and str_product in lexicon_dict[w]:
                pass
            else:
                lexicon_dict[w].append(str_product)

    # COMPANY
    # business.consumer_product
    consumer_product = open('data/lexicon/business.consumer_product', 'r')
    for line in consumer_product:
        x = line.strip().lower().split()
        for w in x:
            if lexicon_dict.has_key(w) and str_company in lexicon_dict[w]:
                pass
            else:
                lexicon_dict[w].append(str_company)

    # business.consumer_company
    consumer_company = open('data/lexicon/business.consumer_company', 'r')
    for line in consumer_company:
        x = line.strip().lower().split()
        for w in x:
            if lexicon_dict.has_key(w) and str_company in lexicon_dict[w]:
                pass
            else:
                lexicon_dict[w].append(str_company)

    # automotive.make
    automotive_make = open('data/lexicon/automotive.make', 'r')
    for line in automotive_make:
        x = line.strip().lower().split()
        for w in x:
            if lexicon_dict.has_key(w) and str_company in lexicon_dict[w]:
                pass
            else:
                lexicon_dict[w].append(str_company)

    # FACILITY
    # venues
    venues = open('data/lexicon/venues', 'r')
    for line in venues:
        x = line.strip().lower().split()
        for w in x:
            if lexicon_dict.has_key(w) and str_facility in lexicon_dict[w]:
                pass
            else:
                lexicon_dict[w].append(str_facility)

    # MUSICARTIST
    lexicon_dict['DJ'.lower()].append(str_musicartist)
    lexicon_dict['Band'.lower()].append(str_musicartist)

    f = open('dict.txt', 'w')
    for key, val in lexicon_dict.items():
        if 'COMPANY' in val:
            f.write(str(key) + " : " + str(val) + '\n')

    # print " "

    pass


def token2features(sent, i, add_neighs = True):
    # Compute the features of a token.

    # All the features are boolean, i.e. they appear or they do not. For the token,
    # you have to return a set of strings that represent the features that *fire*
    # for the token. See the code below.

    # The token is at position i, and the rest of the sentence is provided as well.
    # Try to make this efficient, since it is called on every token.

    # One thing to note is that it is only called once per token, i.e. we do not call
    # this function in the inner loops of training. So if your training is slow, it's
    # not because of how long it's taking to run this code. That said, if your number
    # of features is quite large, that will cause slowdowns for sure.

    # add_neighs is a parameter that allows us to use this function itself in order to
    # recursively add the same features, as computed for the neighbors. Of course, we do
    # not want to recurse on the neighbors again, and then it is set to False (see code).

    ftrs = []

    # print location
    # print " "
    # print stopwords
    # print " "
    # print firstname_1000

    # bias
    ftrs.append("BIAS")


    # THE WORD ITSELF
    word = unicode(sent[i])
    ftrs.append("WORD=" + word)
    ftrs.append("LCASE=" + word.lower())


    # CHARACTER BASED FEATURES
    # Initial Capital
    if word[0] in string.ascii_uppercase:
        ftrs.append("IS_FIRST_CHARACTER_UPPERCASE")

    # Uppercase
    if word.isupper():
        ftrs.append("IS_UPPER")

    # Check if word has both upper and lower case letters
    lowercase = re.compile(r'.*[a-z]+')
    uppercase = re.compile(r'.*[A-Z]+')
    if lowercase.match(word) and uppercase.match(word):
        ftrs.append("IS_MIXED")

    # Numeric
    if word.isnumeric():
        ftrs.append("IS_NUMERIC")
    elif word.isdigit():
        ftrs.append("IS_NUMERIC")
    else:
        word_split = word.split()
        for w_s in word_split:
            if w_s.isnumeric():
                ftrs.append("IS_NUMERIC")

    # Twitter Username
    if word[0] in ['@']:
        ftrs.append('IS_USERNAME')

    # Word without prefix
    ftrs.append("PREFIX=" + word[2:])

    # Word without suffix
    ftrs.append("SUFFIX=" + word[:-2])


    # Lowercase
    # if word.islower():
    #     ftrs.append("IS_LOWER")

    # Inner Capital
    # word_split = word.split()
    # for w_s in word_split[1:-1]:
    #     if w_s.isupper():
    #         ftrs.append("IS_INNER_CAPITAL")

    # Word length
    # ftrs.append("WORD_LENGTH=" + str(len(word)))

    # Vowel Count
    # num_vowels = 0
    # for letter in word:
    #    if letter in "aeiouAEIOU":
    #        num_vowels = num_vowels + 1
    #ftrs.append("NUMBER_OF_VOWELS=" + str(num_vowels))


    # CONTEXT FEATURES
    # position features
    if i == 0:
        ftrs.append("SENT_BEGIN")
    if i == len(sent) - 1:
        ftrs.append("SENT_END")

    # POS Tag
    pos_tag = nltk.pos_tag(sent)
    tag = ''
    for p in pos_tag:
        if p[0] == word:
           tag = p[1]
    ftrs.append("IS_" + tag)

    # Stopwords
    if stopwords.has_key(word):
        ftrs.append('IS_STOPWORD')

    # Check if word is in lexicon
    if word[0] == '#':
        word_strip = word[1:].lower()
        if lexicon_dict.has_key(word_strip):
            for f in lexicon_dict[word_strip]:
                ftrs.append("IS_" + str(f))
        else:
            ftrs.append('IS_HASHTAG')
    else:
        if lexicon_dict.has_key(word.lower()):
            for f in lexicon_dict[word.lower()]:
                ftrs.append("IS_" + str(f))


    # previous/next word feats
    if add_neighs:
        if i > 0:
            for pf in token2features(sent, i-1, add_neighs = False):
                ftrs.append("PREV_" + pf)
        # if i > 1:
        #     for pf in token2features(sent, i-2, add_neighs = False):
        #         ftrs.append("PREV_PREV_" + pf)
        if i < len(sent)-1:
            for pf in token2features(sent, i+1, add_neighs = False):
                ftrs.append("NEXT_" + pf)
        # if i < len(sent)-2:
        #     for pf in token2features(sent, i + 2, add_neighs=False):
        #         ftrs.append("NEXT_NEXT_" + pf)





    # return it!
    return ftrs


if __name__ == "__main__":
    sents = [
    [ "I", "love", "food" ]
    ]

    preprocess_corpus(sents)
    for sent in sents:
        for i in xrange(len(sent)):
            print sent[i], ":", token2features(sent, i), '\n'
