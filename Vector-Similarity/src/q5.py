#!/usr/bin/env python
import distsim
word_to_vec_dict = distsim.load_word2vec("nyt_word2vec.4k")
###Provide your answer below

###Answer examples
# distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['jack'],set(['jack']),distsim.cossim_dense)

# print 'jack ' + str(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['jack'], set(['jack']), distsim.cossim_dense))
# print 'people ' + str(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['people'], set(['people']), distsim.cossim_dense))
# print 'beautiful ' + str(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['beautiful'], set(['beautiful']), distsim.cossim_dense))
# print 'walk ' + str(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['walk'], set(['walk']), distsim.cossim_dense))
# print 'california ' + str(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['california'], set(['california']), distsim.cossim_dense))
# print 'million ' + str(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['million'], set(['million']), distsim.cossim_dense))

print 'jack'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['jack'], set(['jack']), distsim.cossim_dense)):
    print("{}: {} ({})".format(i+1, word, score))
print " "
print 'people'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['people'], set(['people']), distsim.cossim_dense)):
    print("{}: {} ({})".format(i+1, word, score))
print " "
print 'beautiful'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['beautiful'], set(['beautiful']), distsim.cossim_dense)):
    print("{}: {} ({})".format(i+1, word, score))
print " "
print 'walk'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['walk'], set(['walk']), distsim.cossim_dense)):
    print("{}: {} ({})".format(i+1, word, score))
print " "
print 'california'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['california'], set(['california']), distsim.cossim_dense)):
    print("{}: {} ({})".format(i+1, word, score))
print " "
print 'sister'
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['sister'], set(['sister']), distsim.cossim_dense)):
    print("{}: {} ({})".format(i+1, word, score))
