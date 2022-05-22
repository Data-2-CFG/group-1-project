Libraries required:
pandas
numpy
	In addition, from numpy:
	mean
	std
matplotlib.pyplot
seaborn
sklearn
	In addition, from sklearn:
	metrics
train_test_split
make_column_transformer 
make_pipeline
cross_val_score
OneHotEncoder
make_classification
KFold
RepeatedKFold
StratifiedKFold
RepeatedStratifiedKFold
LogisticRegression
resample
tree
datetime
	In addition, from datetime:
time
	timedelta 

Instructions to run modelling taskforce Jupyter notebooks
We recommend the following order of execution when consulting the Jupyter notebooks produced by the modelling (Ilaria, Juliana):
ILA_Notebook_1: This notebook contains the initial analysis performed to explore the structure and content of the synthetic fraud dataset. It introduces the challenges of selecting and pre-processing relevant data. It also contains the first attempt at using OneHotEncoder to transform the dataset’s categorical variables into numeric variables.
JULIANA NOTEBOOK, DESCRIPTION TO INCLUDE
ILA_Notebook_2: This notebook builds on Juliana’s encoding protocol and predictive model to print a visualisation of the decision tree with additional information about its maximum depth and node count. 
ILA_Notebook_3: This notebook contains a OneHotEncoder pre-processing pipeline. This pipeline is then first applied to a Logistic Regression model, the resulting metrics reveal overfitting issues. Then the same pre-processing pipeline is applied to a decision tree model, yielding good metrics in accuracy, recall and precision.
ILA_Notebook_4: This notebook continues testing the potential of Logistic Regression in conjunction with the OneHotEncoder pipeline to produce a solid predictive model. Upsampling and downsampling techniques are introduced to deal with overfitting. To run the results of upsampling please first comment out all cells labelled as related to downsampling. In order to run the results of downsampling, please first comment out all cells labelled as related to upsampling.
ILA_Notebook_5: This notebook continues testing the potential of Logistic Regression to generate a solid anti-fraud predictive model. Here Juliana’s encoding protocol is applied instead of the OneHotEncoder pipeline to evaluate results. The final model continues to show overfitting issues.
ILA_Notebook_6: This notebook continues testing the potential of Logistic Regression to generate a solid anti-fraud predictive model. Cross-validation technique and a cost-sensitive learning framework are applied to the model. Logistic Regression continues to show issues with overfitting. 