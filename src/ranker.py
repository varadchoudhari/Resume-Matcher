import json
import operator
from collections import defaultdict
from retrieval import BM25

# get average document length
def get_avdl(length_index):
    corpus_length = 0
    for document in length_index:
        corpus_length += length_index[document]
    return float(corpus_length) / float(len(length_index))

def search(query):
    inv_index_file = open("../dependency/indexes/inverted_index.json","r")
    inverted_index = json.load(inv_index_file)

    length_index_file = open("../dependency/indexes/length_index.json","r")
    length_index = json.load(length_index_file)

    scores = defaultdict(list)
    query_tokens = query.split()
    for token in query_tokens:
        for entry in inverted_index[token]:
            scores[entry[0]] = BM25(length_index[entry[0]],get_avdl(length_index),len(inverted_index[token]),len(length_index),entry[1],1,0)
    return sorted(scores.items(),key=operator.itemgetter(1))

