from __future__ import division
import sys,json,math
import os
import numpy as np

def load_word2vec(filename):
    # Returns a dict containing a {word: numpy array for a dense word vector} mapping.
    # It loads everything into memory.
    
    w2vec={}
    with open(filename,"r") as f_in:
        for line in f_in:
            line_split=line.replace("\n","").split()
            w=line_split[0]
            vec=np.array([float(x) for x in line_split[1:]])
            w2vec[w]=vec
    return w2vec

def load_contexts(filename):
    # Returns a dict containing a {word: contextcount} mapping.
    # It loads everything into memory.

    data = {}
    for word,ccdict in stream_contexts(filename):
        data[word] = ccdict
    print "file %s has contexts for %s words" % (filename, len(data))
    return data

def stream_contexts(filename):
    # Streams through (word, countextcount) pairs.
    # Does NOT load everything at once.
    # This is a Python generator, not a normal function.
    for line in open(filename):
        word, n, ccdict = line.split("\t")
        n = int(n)
        ccdict = json.loads(ccdict)
        yield word, ccdict
        
def jaccardsim_sparse(v1, v2):
    numerator = 0
    denominator = 0
    for key1, value1 in v1.iteritems():
        if key1 in v2.keys():
            print str(value1) + " " + str(v2[key1])
            numerator += min(value1, v2[key1])
            denominator += max(value1, v2[key1])
    jaccard_sim = float(numerator)/float(denominator)
    print jaccard_sim
    return jaccard_sim


def jaccardsim_dense(v1, v2):
    numerator = 0
    denominator = 0

    for x, y in np.nditer([v1, v2]):
        numerator += min(x, y)
        denominator += max(x, y)
    jaccard_sim = float(numerator)/float(denominator)
    return jaccard_sim


def dicesim_dense(v1, v2):
    numerator = 0
    denominator = 0

    for x, y in np.nditer([v1, v2]):
        numerator += min(float(x), float(y))
        denominator += (float(x) + float(y))
    dice_sim = (2 * numerator) / (denominator)
    # print dice_sim
    return dice_sim


def cossim_sparse(v1,v2):
    # Take two context-count dictionaries as input
    # and return the cosine similarity between the two vectors.
    # Should return a number beween 0 and 1

    ## TODO: delete this line and implement me
    product_sum = 0
    product_v1 = 0
    product_v2 = 0

    for key1, value1 in v1.iteritems():
        if key1 in v2.keys():
            product_sum += value1 * v2[key1]
            
    for key, value in v1.items():
        product_v1 += math.pow(value, 2)

    for key, value in v2.iteritems():
        product_v2 += math.pow(value, 2)
       
    return product_sum / (math.sqrt(product_v1) * math.sqrt(product_v2))
    pass

def cossim_dense(v1,v2):
    # v1 and v2 are numpy arrays
    # Compute the cosine simlarity between them.
    # Should return a number between -1 and 1
    
    ## TODO: delete this line and implement me
    product_sum = np.sum(np.multiply(v1, v2))
    product_v1 = np.sqrt(np.sum(np.square(v1)))
    product_v2 = np.sqrt(np.sum(np.square(v2)))
    sum_product = np.multiply(product_v1, product_v2)
    cosine_result = np.divide(product_sum, sum_product)
   
    return cosine_result
    pass

def show_nearest(word_2_vec, w_vec, exclude_w, sim_metric):
    #word_2_vec: a dictionary of word-context vectors. The vector could be a sparse (dictionary) or dense (numpy array).
    #w_vec: the context vector of a particular query word `w`. It could be a sparse vector (dictionary) or dense vector (numpy array).
    #exclude_w: the words you want to exclude in the responses. It is a set in python.
    #sim_metric: the similarity metric you want to use. It is a python function
    # which takes two word vectors as arguments.

    # return: an iterable (e.g. a list) of up to 10 tuples of the form (word, score) where the nth tuple indicates the nth most similar word to the input word and the similarity score of that word and the input word
    # if fewer than 10 words are available the function should return a shorter iterable
    #
    # example:
    #[(cat, 0.827517295965), (university, -0.190753135501)]
    
    ## TODO: delete this line and implement me
    functions = { 'cossim_sparse' : cossim_sparse,
                 'cossim_dense': cossim_dense }

    similarity_dict = {}
    for key, val in word_2_vec.items():
        if key not in exclude_w:
            similarity_dict[key] = functions[sim_metric.func_name](w_vec, val)

    similarity_list = []
    count = 0
    for v in sorted(similarity_dict, key = similarity_dict.get, reverse = True):
        if count == 10:
            break
        similarity_list.append((v, similarity_dict[v]))
        count += 1

    return similarity_list
    pass
