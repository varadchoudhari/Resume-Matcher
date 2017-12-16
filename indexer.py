from collections import defaultdict
import glob
import tokenizer
import json


def get_file_names(path):
    files = []
    for file in glob.glob(str(path)+"/*.pdf"):
        files.append(file)
    return files


def make_index(tokens, document_name, index, length):
    for term in set(tokens):
        index[term].append([document_name,tokens.count(term)])
        length[document_name] = len(set(tokens))


def generator(path):
    resume_files = get_file_names(path)
    inverted_index = defaultdict(list)
    length_index = defaultdict(list)
    for file in resume_files:
        make_index(tokenizer.tokenize(file), file, inverted_index, length_index)
    write(inverted_index,length_index)
    print "Indexes generated"


def write(inverted_index,length_index):
    inv_index_file = open("inverted_index.json","w")
    json.dump(inverted_index,inv_index_file)

    length_index_file = open("length_index.json","w")
    json.dump(length_index,length_index_file)



