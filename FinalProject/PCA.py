# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVC

DEBUG = False

# div function: to divide data by "num" column
def debug(s):
    if DEBUG:
        print(s)

def div(a, ratio):
    print("Running seg{0} ... ".format(a))

    df = pd.read_csv("./data/segData/df_seg%s.csv"%a)
    df.drop(["Unnamed: 0", "MemberId"], axis=1, inplace=True)
    debug("Sum of data(for this seg): {0} ".format(len(df)))

    msk = np.random.rand(len(df)) < ratio
    train = df[msk]
    test = df[~msk]
    debug(train["SalesOrderSlaveTotalPayment"].max())
    debug(train["SalesOrderSlaveTotalPayment"].min())

    train["SalesOrderSlaveTotalPayment"] = norm(train["SalesOrderSlaveTotalPayment"])
    # debug: max should = 1, min should = 0
    debug(train["SalesOrderSlaveTotalPayment"].max())
    debug(train["SalesOrderSlaveTotalPayment"].min())

    test["SalesOrderSlaveTotalPayment"] = norm(test["SalesOrderSlaveTotalPayment"])

    print("Sum of training data(for this seg): {0}".format(len(train)))
    print("Sum of testing data(for this seg): {0}".format(len(test)))
    print("---")
    return train, test

# norm function: to normalize (pandas) series data
def norm(s):
    result = (s - s.min())/(s.max()-s.min())
    return(result)

# get_testing_labels function: PCA
def get_testing_labels(training_samples, training_labels, testing_samples):
    normalizer       = Normalizer().fit(training_samples)
    training_samples = normalizer.transform(training_samples)
    testing_samples  = normalizer.transform(testing_samples)

    pca              = PCA(n_components=0.8, whiten=True).fit(training_samples)
    training_samples = pca.transform(training_samples)
    testing_samples  = pca.transform(testing_samples)

    svm_classifier   = SVC(C=2.8).fit(training_samples, training_labels)
    return svm_classifier.predict(testing_samples)


# main function
def main():

    # --- Read argument ---
    ratio = float(sys.argv[1])

    # --- divided df_seg2~20 into training&testing data ---
    # choose df_seg2~20 and divide it
    trainingData, testingData = div(2,ratio)
    debug(len(trainingData))
    debug(len(testingData))

    for i in range(3,21):
        df0, df1 = div(i, ratio)
        # concat to pre dataframe, and ignore index
        trainingData = pd.concat([trainingData,df0],ignore_index=True)
        testingData = pd.concat([testingData,df1],ignore_index=True)
        debug(len(trainingData))
        debug(len(testingData))

    debug(len(trainingData))
    debug(len(testingData))

    # store "num" column at df_label before norm
    # to check error of every seg(mean "num" column)
    num = testingData["num"]

    # normalize the "num" column
    trainingData["num"] = norm(trainingData["num"])
    testingData["num"] = norm(testingData["num"])

    # change CostAbi to (1 - CostAbi)
    trainingData["1CostAbi"] = 1- trainingData["CostAbi"]
    testingData["1CostAbi"] = 1 - testingData["CostAbi"]

    # debug: check trainingData&testingData
    debug("Sum of training data: {0}".format(len(trainingData)))
    debug("Sum of testing data: {0}".format(len(testingData)))

    # check column
    trainingData.to_csv("./data/columncheck.csv")

    # --- PCA of training&testing data ---
    # Read training and testing data
    training_df  = trainingData.dropna()
    testing_df   = testingData.dropna()
    print("Training set has {0[0]} rows and {0[1]} columns".format(training_df.shape))
    print(" Testing set has {0[0]} rows and {0[1]} columns".format(testing_df.shape))

    # Get training samples and labels from training data
    training_labels     = training_df["label"].values
    training_samples    = training_df.drop(["label"], axis = 1).values
    # Get testing samples from testing data
    real_testing_label  = testing_df["label"]
    testing_samples     = testing_df.drop(["label"], axis = 1).values
    testing_labels      = get_testing_labels(training_samples, training_labels, testing_samples)

    # Writing testing labels to CSV
    df_label   = pd.DataFrame(testing_labels, columns=["label"])
    df_label.index     += 1
    df_label.index.name = "label"
    df_label["real_testing_label"] = real_testing_label
    df_label["num"] = num

    print('testingLabel finish!')

    # Accuracy
    # every seg accuracy
    df_label.dropna(inplace=True)
    df_label_int = df_label.astype("int")
    df_label_int['diff'] = df_label_int['real_testing_label']-df_label_int['label']
    len_df = len(df_label_int)
    accuracy = (len_df - df_label_int['diff'].abs().sum())/len_df*100
    print("all Accuracy: {0}%".format(accuracy))

    add_column_list = ["l1r1", "l1r0", "l0r1", "l0r0"]

    state1 = True
    state2 = True
    for column in add_column_list:
        df_label_int[column] = 0
        df_label_int[column][(df_label_int["label"]==state1)&(df_label_int["real_testing_label"]==state2)] = 1
        state1 = (state1^state2)^True
        state2 = state2^True

    data = df_label_int.groupby(by="num")["l1r1", "l1r0", "l0r1", "l0r0"].sum()
    data["oriRatio"] = (data["l1r1"]+data["l0r1"])/(data["l1r1"]+data["l1r0"]+data["l0r1"]+data["l0r0"])
    data["transRatio"] = data["l1r1"]/(data["l1r1"]+data["l1r0"])
    data.to_csv('./data/training&testingData/testing_labels_df_{0}.csv'.format(ratio), sep=',', index = False)
    print(data)

if __name__ == "__main__":
    main()
