README COVID API

This notebook is useful to retrieve data from Oxford COVID-19 Government Response Tracker
(https://covidtracker.bsg.ox.ac.uk/ ), an API to access the data collected from publicly available information by a cross-disciplinary Oxford University team of academics and students from every part of the world, led by the Blavatnik School of Government. The different policy responses are tracked since 1 January 2020, cover more than 180 countries.

To retrieve the data, open the “COVIDdata_API” notebook stored in the folder “API data retrieval”.
The user will be asked to provide a start date (from the 1st January 2020 on) and an end date.

After providing the time period the user will be supported by the instructions.

README TRANSACTION DATA

With this notebook we simply imported our 2 different transaction datasets (fraud_train.csv and fraud_test.csv) and merge them to have one unique dataset and save the into a csv file to proceed with our analysis.

Each step is made explicit in the title: after checking the path of the files “fraudTest.csv” and “fraudTrain.csv”, open the notebook “Transaction Data” and run the code following the instructions.

README DATA VISUALISATION_1

The function of this notebook provides information about the questions we are trying to answer to, and shows step by step the process we used to prepare, join and and analyse our Crime Rate, US Population and Transaction datasets, and to visualise the results in order to try to answer our questions. 

As with the other notebooks, each step is explained in the notes: before opening and running this notebook, make sure you’ve ran the ‘Transaction Data Notebook” to merge the “fraudTest.csv” and “fraudTrain.csv” file to generate the “Full_transaction_dataset.csv” file.

After checking the path of the files “Full_transaction_dataset.csv”, “CCATMFraudCrimeRate1991-2020.csv” and “US_total_population.csv”, open the notebook and run the code following the notes and the instructions.

