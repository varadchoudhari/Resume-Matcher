from math import log

k1 = 1.2
b = 0.75
k2 = 100
R = 0 

def retrieval(dl, avdl, n, N, f, q, r):
    p1 = ((k2 + 1) * q) / (k2 + q)
    p2 = ((k1 + 1) * f) / (scoreK(dl, avdl) + f)
    p3 = log((r + 0.5) * (N - n - R + r + 0.5)) / ((n - r + 0.5) * (R - r + 0.5))
    return p1 * p2 * p3

def scoreK(dl, avdl):
    return k1 * ((1 - b) + b * (float(dl) / float(avdl)))