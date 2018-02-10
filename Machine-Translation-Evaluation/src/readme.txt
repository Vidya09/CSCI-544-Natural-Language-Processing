1. Install scikit
2. Install nltk. 
3. From nltk, download wordnet using command: 
      nltk.download('wordnet')
4. To generate eval.out, run the following command:
      python evaluate > eval.out
5. To get accuracy:
      python compare-with-human-evaluation < eval.out