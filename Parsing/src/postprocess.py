#!/usr/bin/env python

import sys, fileinput
import tree

#f = open('train.post', 'w')
for line in fileinput.input():
    t = tree.Tree.from_str(line)
    if t.root is None:
        print
        continue
    t.restore_unit()
    t.unbinarize()
    # t.unannotate_parent(t.root)
    # t.unannotate_grandparent(t.root)
    print t
    #f.write(str(t) + '\n')

#f1 = open('train.post')
#f2 = open('train.trees')
#data1 = f1.read().strip()
#data2 = f2.read().strip()

"""
if data1.strip() == data2.strip():
    print "Same!"
else:
    print "Not same"
"""
"""
# For postprocessing after getting parser output
#f1 = open('dev.parses', 'r')
#f = open('dev.parses.post', 'w')

for line in fileinput.input():
    if line in ['\n']:
        f.write('\n')
    else:
        t = tree.Tree.from_str(line)
        if t.root is None:
            print
            continue
        t.restore_unit()
        t.unbinarize()
        #f.write(str(t) + '\n')
#print ''.join(file('dev.parses.post'))
#with open('dev.parses.post', 'r') as fin:
#    print fin.read()



# Lowercase modification
# file = open('dev.trees', 'r')
# lines = [line.lower() for line in file]
# with open('dev2.trees', 'w') as out:
#      out.writelines(lines)
"""