#!/usr/bin/env python
import distsim

# you may have to replace this line if it is too slow 
word_to_ccdict = distsim.load_contexts("nytcounts.4k")

### provide your answer below
# print 'jack ' + str(distsim.show_nearest(word_to_ccdict, word_to_ccdict['jack'], set(['jack']), distsim.cossim_sparse))
# print 'people ' + str(distsim.show_nearest(word_to_ccdict, word_to_ccdict['people'], set(['people']), distsim.cossim_sparse))
# print 'beautiful ' + str(distsim.show_nearest(word_to_ccdict, word_to_ccdict['beautiful'], set(['beautiful']), distsim.cossim_sparse))
# print 'walk ' + str(distsim.show_nearest(word_to_ccdict, word_to_ccdict['walk'], set(['walk']), distsim.cossim_sparse))
# print 'california ' + str(distsim.show_nearest(word_to_ccdict, word_to_ccdict['california'], set(['california']), distsim.cossim_sparse))
# print 'million ' + str(distsim.show_nearest(word_to_ccdict, word_to_ccdict['million'], set(['million']), distsim.cossim_sparse))


print 'jack'
result_jack = distsim.show_nearest(word_to_ccdict, word_to_ccdict['jack'], set(['jack']), distsim.cossim_sparse)
for i, (word, score) in enumerate(result_jack):
    print("{}: {} ({})".format(i+1, word, score))

print '\n' + result_jack[0][0]
result_adam = (distsim.show_nearest(word_to_ccdict, word_to_ccdict[result_jack[0][0]], set([result_jack[0][0]]), distsim.cossim_sparse))
for i, (word, score) in enumerate(result_adam):
    print("{}: {} ({})".format(i+1, word, score))

print '\n' + result_adam[0][0]
result_susan = (distsim.show_nearest(word_to_ccdict, word_to_ccdict[result_adam[0][0]], set([result_adam[0][0]]), distsim.cossim_sparse))
for i, (word, score) in enumerate(result_susan):
    print("{}: {} ({})".format(i+1, word, score))


print '\n' + 'people'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['people'], set(['people']), distsim.cossim_sparse)):
    print("{}: {} ({})".format(i+1, word, score))

print '\n' + 'beautiful'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['beautiful'], set(['beautiful']), distsim.cossim_sparse)):
    print("{}: {} ({})".format(i+1, word, score))

print '\n' + 'walk'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['walk'], set(['walk']), distsim.cossim_sparse)):
    print("{}: {} ({})".format(i+1, word, score))

print '\n' + 'california'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['california'], set(['california']), distsim.cossim_sparse)):
    print("{}: {} ({})".format(i+1, word, score))

print '\n' + 'sister'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['sister'], set(['sister']), distsim.cossim_sparse)):
    print("{}: {} ({})".format(i+1, word, score))
    

"""
###Answer examples
# distsim.show_nearest(word_to_ccdict, word_to_ccdict['jack'],set(['jack']),distsim.cossim_sparse)
"""