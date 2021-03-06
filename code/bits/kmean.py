import fileprocessor as filep
import pandas as pd
import sharedprocessor as sp
from numpy import hstack
from sklearn.cross_validation import train_test_split
from sklearn.cluster import KMeans


csvEXT = ".csv"
xlsEXT = ".xlsx"

def perform(opath, testPercent):
    # Loop through all files
    files = filep.getAllFiles(opath)
    for file in files:
        if file.endswith(xlsEXT):
            # perform algorithm
            # store result in output_<algorithm_name>
            df = filep.importExcel(opath + file, "input_normalized")
            column_size = df.shape[1]
            length = len(df)
            X = df.values[:, 0:(column_size - 1)]
            Y = df.values[:, column_size - 1]
            X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=testPercent, random_state=0,
                                                                 stratify=None)

            kmeans = KMeans(n_clusters=2)
            kmeans.fit(X_train)
            centroids = kmeans.cluster_centers_
            labels = kmeans.labels_
            y_pred = kmeans.fit_predict(X_test)
            #y_pred = sp.classifyVectors(X_test, centroids)
            odf = pd.DataFrame().reindex_like(df)
            odf["Predicted Bug"] = ""
            for i in range(len(X_test)):
                odf.loc[i] = hstack((X_test[i] , Y_test[i] , y_pred[i]))
            filep.createSheet(opath + file, "output_kmean", odf)

            # generate confusion matrix
            # store result in output_<algorithm_name>_confusion sheet
            tn, fp, fn, tp = sp.generateConfusionMatrix(Y_test, y_pred)
            a, p, r, fmeasure = sp.computePerformanceMetrics(tn, fp, fn, tp)
            d = {'File name': [file], 'Algorithm': ['kmeans'], 'tn': [tn], 'fp': [fp], 'fn': [fn], 'tp': [tp],
                 'Accuracy': [a], 'Precision': [p], 'Recall': [r], 'F-Measure': [fmeasure]}
            cdf = pd.DataFrame(data=d)
            cdf = cdf[['File name', 'Algorithm', 'tn', 'fp', 'fn', 'tp', 'Accuracy', 'Precision', 'Recall',
                       'F-Measure']]
            filep.createSheet(opath + file, "output_kmean_result", cdf)