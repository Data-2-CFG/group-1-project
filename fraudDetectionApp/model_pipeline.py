# -*- coding: utf-8 -*-
"""
Created on Sun May 22 21:33:45 2022

@author: intern7
"""

from config import *
from preprocessing_pipeline import *

def split_dataset(df):
    
    #Separating the data into train and test
    
    ##1 - Separating X and y
    X = df.drop(["is_fraud", "Unnamed: 0"], axis=1)
    y = df['is_fraud']
    
    return X, y
        
def train_apply(clf_name, X, y):
    
     
    ##2 - Splitting dataset into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, test_size=0.3, stratify=y)
    
    #Fitting the model into the data
    if clf_name == "Decision Tree":
        clf = DecisionTreeClassifier()
    elif clf_name == "Logistic Regression":
        clf = LogisticRegression()
    
    clf.fit(X_train, y_train)

    #Predicting fraudulent transactions 

    y_pred = clf.predict(X_test)
    
    return y_test, y_pred

@st.cache
def model_pipeline(dataset_name, clf_name):
    
    df = preprocessing_pipeline(dataset_name)
    X, y = split_dataset(df)
    y_test, y_pred = train_apply(clf_name, X, y)

    return y_test, y_pred

@st.cache    
def print_results(y_test, y_pred):
    
    accuracy = metrics.accuracy_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred)
    recall = metrics.recall_score(y_test, y_pred)
    
    return accuracy, precision, recall

def plot_matrix(y_test, y_pred):
    
    cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
    
    class_names=[0,1]
    fig, ax = plt.subplots()
    tick_marks = np.arange(len(class_names))
    plt.xticks(tick_marks, class_names)
    plt.yticks(tick_marks, class_names)
    # create heatmap
    sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="viridis" ,fmt='g')
    ax.xaxis.set_label_position("top")
    plt.tight_layout()
    plt.ylabel('Fraud label', fontsize=14)
    plt.xlabel('Predicted label', fontsize=14)
    
    return st.pyplot(fig)


    

    