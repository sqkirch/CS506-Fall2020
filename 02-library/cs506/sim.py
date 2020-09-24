import math

def euclidean_dist(x, y):
    if (len(x)==0 or len(y)==0):
        return ValueError("Vector cannot be empty.")
    if (len(x)!=len(y)):
        return ValueError("Vectors must be the same dimension.")
    sum = 0.
    entrydist = 0.
    entrydistsq = 0.
    for i in range(len(x)):
        entrydist = abs(x[i]-y[i])
        entrydistsq = entrydist**2
        sum += entrydistsq
    return (sum**.5)

def manhattan_dist(x, y):
    if (len(x)==0 or len(y)==0):
        return ValueError("Vector cannot be empty.")
    if (len(x)!=len(y)):
        return ValueError("Vectors must be the same dimension.")
    sum = 0.
    entrydist = 0.
    for i in range(len(x)):
        entrydist = abs(x[i]-y[i])
        sum += entrydist
    return sum

def jaccard_dist(x, y):
    if (len(x)==0 or len(y)==0):
        return ValueError("Vector cannot be empty.")
    if (len(x)!=len(y)):
        return ValueError("Vectors must be the same dimension.")
    
    cap = set(x).intersection(set(y))
    cup = set(x).union(set(y))
    return 1-((abs(len(cap)))/(abs(len(cup))))


def cosine_sim(x, y):
    if (len(x)==0 or len(y)==0):
        return ValueError("Vector cannot be empty.")
    if (len(x)!=len(y)):
        return ValueError("Vectors must be the same dimension.")
    
    normsqx = 0.
    normx = 0.
    normsqy = 0.
    normy = 0.
    dotprod = 0.
    for i in range(len(x)):
        normsqx += x[i]**2
        normsqy += y[i]**2
        normx = normsqx**.5
        normy = normsqy**.5
        dotprod += x[i]*y[i]    
    return (dotprod/(normx*normy))


# Feel free to add more
