import nltk
from nltk.corpus import conll2000
# cp = nltk.RegexpParser(r"NP: {<[CDJNP].*>+}")
# test_sents = conll2000.chunked_sents('train.txt', chunk_types = ['NP'])
# print(cp.evaluate(test_sents))

train_sents = conll2000.chunked_sents('train.txt', chunk_types = ['NP'])
