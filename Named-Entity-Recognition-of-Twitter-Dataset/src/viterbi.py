import numpy as np
from numpy import random
from itertools import product
import math


def run_viterbi(emission_scores, trans_scores, start_scores, end_scores):
# def run_viterbi():
    """Run the Viterbi algorithm.

    N - number of tokens (length of sentence)
    L - number of labels

    As an input, you are given:
    - Emission scores, as an NxL array
    - Transition scores (Yp -> Yc), as an LxL array
    - Start transition scores (S -> Y), as an Lx1 array
    - End transition scores (Y -> E), as an Lx1 array

    You have to return a tuple (s,y), where:
    - s is the score of the best sequence
    - y is a size N array of integers representing the best sequence.
    """

    L = start_scores.shape[0]
    assert end_scores.shape[0] == L
    assert trans_scores.shape[0] == L
    assert trans_scores.shape[1] == L
    assert emission_scores.shape[1] == L
    N = emission_scores.shape[0]
    y = []

    """
    y = []
    N = 4
    L = 5

    print "Tokens (N): " + str(N)
    print "Labels (L): " + str(L)
    
    emission_scores = np.array([
                                [0, 0, 0.7, 0, 0],
                                [0.4, 0.1, 0, 0, 0],
                                [0.1, 0.9, 0, 0, 0],
                                [0, 0, 0, 1, 0.1]
                              ])
    trans_scores = np.array([
                             [0.2, 0.4, 0.01, 0.3, 0.04],
                             [0.3, 0.05, 0.3, 0.2, 0.1],
                             [0.9, 0.01, 0.01, 0.01, 0.7],
                             [0.4, 0.05, 0.4, 0.1, 0.05],
                             [0.1, 0.5, 0.1, 0.1, 0.1]
                            ])
    start_scores = np.array([0.3, 0.1, 0.3, 0.2, 0.1])
    end_scores = np.array([0.05, 0.05, 0, 0, 0.1])
    """

    viterbi_table = np.zeros(shape=(L, N))
    backpointer_table = np.zeros(shape=(L, N))

    # start probabilities * emission probabilities
    for i in xrange(L):
        viterbi_table[i][0] = start_scores[i] + emission_scores[0][i]

    # fill rest of table
    for j in range(1, N):
        for i in range(0, L):
            trans_em = np.array([(viterbi_table[x][j - 1] + trans_scores[x][i]) for x in range(L)])
            viterbi_table[i][j] = emission_scores[j][i] + max(trans_em)
            backpointer_table[i][j] = np.argmax(trans_em)

    # end probabilities
    end_prob = np.array([(viterbi_table[i][N - 1] + end_scores[i]) for i in range(L)])
    last_seq = np.argmax(end_prob)
    best_score = max(end_prob)

    # construct best sequence
    best_seq = [last_seq]
    best_index = last_seq
    for i in reversed(range(1, N)):
        best_index = backpointer_table[int(best_index)][i]
        best_seq.append(int(best_index))

    return best_score, best_seq[::-1]

if __name__ == "__main__":
    run_viterbi()
