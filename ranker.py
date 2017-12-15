# -*- coding: utf-8 -*-

from math import log

'''
Using the following formula to calculate BM25
((k3 + 1)q)/((k3 + q)) * ((k1 + 1)f)/((K + f)) * log((r + 0.5)(N − n − R + r + 0.5))/((n − r + 0.5)(R − r + 0.5))
REFERENCE: https://xapian.org/docs/bm25.html
'''

