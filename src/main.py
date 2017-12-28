from indexer import generator
from ranker import search

generator()
option = ""
while option != "q":
    print "\n"
    print "Enter search query"
    keywords = raw_input(":: ")
    results = search(keywords)
    print"\nThe Matching Resumes Are:"
    for result in results:
        print result[0]

