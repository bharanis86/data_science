from sklearn.metrics import confusion_matrix
from numpy import array
import pandas as pd
import fileprocessor as fp
import os
import shutil
from scipy.spatial import distance
from numpy import hstack


csvEXT = ".csv"
xlsEXT = ".xlsx"

def normalizeInputCSV(iPath, oPath, fileName):
    csvFilePath = iPath + fileName + csvEXT;
    xlsxFilePath = oPath + fileName + xlsEXT
    fp.convertToExcel(csvFilePath, xlsxFilePath, "input")
    df = fp.importCSV(csvFilePath)
    for index, row in df.iterrows():
        if row["bug"] > 0:
            df.set_value(index, 'bug', 1)
        else:
            df.set_value(index, 'bug', 0)

    df.drop(df.columns[[0, 1, 2]], axis=1, inplace=True)
    fp.createSheet(oPath + fileName + xlsEXT, "input_normalized", df)

def normalizeInputFiles(iPath, oPath):
    files = fp.getAllFiles(iPath)
    if os.path.exists(oPath):
        shutil.rmtree(oPath)
    os.makedirs(oPath)

    for file in files:
        if file.endswith(csvEXT):
            fileName = os.path.splitext(file)[0]
            normalizeInputCSV(iPath, oPath, fileName)

def generateConfusionMatrix(test_op, pred_op):
    tn, fp, fn, tp = confusion_matrix(test_op, pred_op).ravel()
    return tn, fp, fn, tp

def computePerformanceMetrics(tn, fp, fn, tp):
    a = (tp+tn)/(tp+tn+fp+fn)
    p = tp/(tp+fp)
    r = tp/(tp+fn)
    fmeasure = (2*tp)/(2*tp+fp+fn)
    return a, p, r, fmeasure

def computeDistance(d, c):
    return distance.euclidean(d, c)

def classifyVectors(xTest, centroids):
    yPred = array([])
    for tdata in xTest:
        d0 = computeDistance(tdata, centroids[0])
        d1 = computeDistance(tdata, centroids[1])
        if d0 < d1:
           yPred = hstack((yPred, [0]))
        else:
           yPred = hstack((yPred, [1]))
    return yPred

def consolidateResults(opath):
    files = fp.getAllFiles(opath)
    cdf = pd.DataFrame(columns=['File name', 'Algorithm', 'tn', 'fp', 'fn', 'tp', 'Accuracy',
                                'Precision', 'Recall', 'F-Measure'])
    cdf = cdf[['File name', 'Algorithm', 'tn', 'fp', 'fn', 'tp', 'Accuracy', 'Precision', 'Recall',
               'F-Measure']]
    for file in files:
        if file.endswith(xlsEXT):
            r_kmean = fp.importExcel(opath + file, "output_kmean_result")
            r_harch = fp.importExcel(opath + file, "output_hcluster_result")
            r_fuzzy = fp.importExcel(opath + file, "output_fuzzy_result")
            r_dtree = fp.importExcel(opath + file, "output_dtree_result")
            cdf = cdf.append(r_kmean)
            cdf = cdf.append(r_harch)
            cdf = cdf.append(r_fuzzy)
            cdf = cdf.append(r_dtree)

    fp.createExcel(opath + "consolidated_results" + xlsEXT, "output", cdf)