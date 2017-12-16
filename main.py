from indexer import generator
from ranker import search

option = ""
while option != "3":
    print "\n"
    print "RESUME MATCHER\n"
    print "Enter your choice"
    print "1. Create Inverted Index"
    print "2. Match Resume"
    print "3. Quit"

    option = raw_input(":: ")

    if option == "1":
        generator("documents")
    elif option == "2":
        print "Enter search query"
        keywords = raw_input("::")
        search(keywords)

