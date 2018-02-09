#!/usr/bin/env python
import distsim
from collections import defaultdict

f = open('q8.txt', 'r')
word_to_vec_dict = distsim.load_word2vec("nyt_word2vec.4k")

analogy_dict = defaultdict(list)
analogy_percentage = defaultdict(list)
category_list = []

# f1 = open('notes3.txt', 'w')

for line in f:
    line = line.strip('\n')
    if line.startswith('//'):
        continue
    if line.startswith(":"):
        category = line.split(' ')[1]
        category_list.append(category)
    else:
        words = line.split()

        # f1.write(str(words) + '\n')

        word1_dict = word_to_vec_dict[words[0]]
        word2_dict = word_to_vec_dict[words[1]]
        word4_dict = word_to_vec_dict[words[3]]
        ret = distsim.show_nearest(word_to_vec_dict, word1_dict-word2_dict+word4_dict, set([words[0], words[1], words[3]]),
                                   distsim.cossim_dense)

        # f1.write(str(ret) + '\n')

        number = 0
        found = False
        for result in ret:
            number += 1
            if result[0] == words[2]:
                found = True
                break
        if not found:
            number = None
        analogy_dict[category].append([number])

        # f1.write(str(analogy_dict))
        # f1.write("\n\n")
# f1.write(str(analogy_dict))

for cat, value in analogy_dict.items():
    top1 = 0
    top5 = 0
    top10 = 0
    for pos in value:
        if pos[0] is not None:
            if pos[0] == 1:
                top1 += 1
            if pos[0] <= 5:
                top5 += 1
            if pos[0] <= 10:
                top10 += 1
    top1_percent = float(top1) / float(len(value))
    top5_percent = float(top5) / float(len(value))
    top10_percent = float(top10) / float(len(value))
    analogy_percentage[cat].append([top1_percent, top5_percent, top10_percent])

# Print table
print "relation-group" + " " + "best-1" + " " + "best-5" + " " + "best-10"
for cat in category_list:
    values = analogy_percentage[cat]
    rounded_values = []
    for val in values[0]:
        decimal = str(val).split(".")[1]
        if decimal.startswith('0'):
            rounded_values.append(round(float(val), 3))
        else:
            rounded_values.append(round(float(val), 2))
    print cat + " " + str(rounded_values[0]) + " " + str(rounded_values[1]) + " " + str(rounded_values[2])
