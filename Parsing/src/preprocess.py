#!/usr/bin/env python

import sys, fileinput
import tree

#f = open('train.trees.pre', 'w')
#f1 = open('train.trees', 'r')

for line in fileinput.input():
    t = tree.Tree.from_str(line)

    # t = tree.Tree.from_str(line)
    # Binarize, inserting 'X*' nodes.
    t.binarize()

    # Remove unary nodes
    t.remove_unit()
    
    
    # t.annotate_parent(t.root)
    # t.annotate_grandparent(t.root)

    # The tree is now strictly binary branching, so that the CFG is in Chomsky normal form.
    # Make sure that all the roots still have the same label.
    assert t.root.label == 'TOP'
    
    print t

    #f.write(str(t) + '\n')