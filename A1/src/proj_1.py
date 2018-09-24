# Assignment 1
# File contains:
# Apriori algorithm to find frequent sets (& support function)
# Simple rule building algorithm (& confidence function)
# (Commented out) Test on simple example data set

import csv

#Computes the support of the given set in the given database.
#c: A set of items
#D: A list of sets of items (Database)
#return: The number of sets in the database which itemset is a subset of. 
def support(c,D):
    count = 0
    for d in D:
        if c.issubset(d):
            count = count+1; 
    return count


#Finds all itemsets in database that have at least minSupport.
#D: A list of sets of items (Database)
#I: A list of all items that occur in the database
#minSupp: an integer > 1
#return: A list of sets of items, such that 
#   s in return --> support(s,database) >= minSupport.
def aPriori(I, D, minSupp):
    FS = set()
    cands = []
    for i in I:
        cands.append(frozenset({i}))
        #print(cands)
    while len(cands) > 0:
        H = set()
        for c in cands:
            if support(c,D) >= minSupp:
                H = H.union({c})
                #print(H)
        cands = set()
        #print(H)
        for h in H:
            for i in H.difference({h}):
                cands = cands.union({h.union(i)})
                #print(cands)
        #FS.append(H)
        FS = FS.union(H)
        #print(FS) 
    return FS


#Computes the confidence of a given rule.
#The rule takes the form precedent --> antecedent
#precedent: A set of items
#antecedent: A set of items that is a superset of precedent
#database: a list of sets of items.
#return: The confidence in precedent --> antecedent.
def conf(s,t,D):
    confidence = support(s.union(t),D)/support(s,D) 
    return confidence


#Given a set of frequently occuring Itemsets, returns
# a list of pairs of the form (precedent, antecedent)
# such that for every returned pair, the rule 
# precedent --> antecedent has confidence >= minConfidence
# in the database.
#FS: a set of frequently occurring sets of items. 
#D: A list of sets of items (Database)
#minConf: A real value between 0.0 and 1.0. 
#return: A list of pairs of sets of items.
def simpleRuleBuilding(FS, D, minConf):
    rules = []
    for s in FS:
        for t in FS.difference(s):
            if conf(s,t,D) >= minConf
                rules.append((s,t))
    return rules


# Test a simple set 
"""
# A priori frequent sets
D = [{1,2}, {1,2,3}, {1,4}, {4,6}, {1,4,6}]
I = [1, 2, 3, 4, 5, 6]
minSupp = 2
FS = aPriori(I,D,minSupp)
print(FS)
# Rule building
minConf = 0.90
rules = simpleRuleBuilding(FS, D, minConf)
print(rules)
"""

# read in the csv file and use it to create dataset and itemset
with open('../data/proj1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    D = []
    I = []

    rowentries = set()

    # generate D (whole dataset) and I (itemset)
    # D should be a list of sets, where each set is a row
    # I should be a list of items
    for row in readCSV:
        for i in range(len(row)):
            rowentries.add(row[i])
            if row[i] not in I:
                I.append(row[i]) 
        D.append(rowentries)
        rowentries = set()

    del D[0] # this just has a list of column headers

    

minSupp = 1000
minConf = 0.75
FS = aPriori(I,D,minSupp)
rules = simpleRuleBuilding(FS, D, minConf)

print('Frequent sets')
print(FS)
print('Frequent rules')
print(rules)



    
