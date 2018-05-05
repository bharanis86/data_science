import sharedprocessor as sp
import hierarchical as harch
import decisiontree as dtree
import kmean as kmean
import fuzzyc as fuzzy


path = "C:\BITS\dm_asg\data\\"
opath = "C:\BITS\dm_asg\data\output\\"
# Percentage of data used has test, eg: 0.3 - 30% test and 70% training data
testPercent = 0.3

# normalize input, bugs >= 1 is 1 and rest 0
# store op in new input_normalized sheet
sp.normalizeInputFiles(path, opath)

# Perform K-Means algorithm
kmean.perform(opath, testPercent)

# Perform HCluster algorithm
harch.perform(opath, testPercent)

# Perform fuzzy algorithm
fuzzy.perform(opath, testPercent)

# Perform decision tree algorithm
dtree.perform(opath, testPercent)

# Consolidate results
sp.consolidateResults(opath)