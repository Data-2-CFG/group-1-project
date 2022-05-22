**Libraries required:**  
pandas  
numpy  
matplotlib.pyplot  
matplotlib  
seaborn  
pprint  
Datetime (and datetime from datetime)  

**API Keys required:**  
An API key is required for the FBI Crime database. To obtain one please go to → https://api.data.gov/signup/

**Getting data from the GitHub repository:**  
- The *[/raw_data](https://github.com/Data-2-CFG/group-1-project/tree/main/raw_data) folder in this repo contains recent exports from our personal databases. You are welcome to build applications that draw directly from this repository.  
- The CSV file *[/raw_data/fraudTest.csv](https://github.com/Data-2-CFG/group-1-project/blob/main/raw_data/fraudTest.csv), provides the initial simulated test dataset for the credit card transactions. This is not updated as we used this as our base dataset.    
- The CSV file *[/raw_data/fraudTrain.csv](https://github.com/Data-2-CFG/group-1-project/blob/main/raw_data/fraudTrain.csv), provides the initial simulated train dataset for the credit card transactions. This is not updated as we used this as our base dataset.    
- The CSV file *[/raw_data/COVID19API_2019-01-01_2020-12-31](https://github.com/Data-2-CFG/group-1-project/blob/main/raw_data/COVID19API_2019-01-01_2020-12-31.csv), provides the 2020 stringency data for the entire world: This will be useful for the COVID visualisations
- The CSV file *[/raw_data/COVID19API_2021-01-01_2021-12-31](https://github.com/Data-2-CFG/group-1-project/blob/main/raw_data/COVID19API_2021-01-01_2021-12-31.csv), provides the 2020 stringency data for the entire world: This will be useful for the COVID visualisations

**Order in which to run the Notebooks:**
- There is an order to run the notebooks to reach the visualisations as they encourage you to save datasets as a csv file onto your local server to run codes for future use.   
- The notebook *[COVIDdata_API.ipynb](https://github.com/Data-2-CFG/group-1-project/blob/main/Nicol_data_retrieval/COVIDdata_API.ipynb) , this is to retrieve COVID stringency data. For the COVID visualisations the date ranges input were 2019-01-01 to 2020-12-31 and 2021-01-01 to 2021-12-31. However, these data sets have also been added to the data repository as noted above.  
- The notebook *[CRIMEdata_API.ipynb](https://github.com/Data-2-CFG/group-1-project/blob/main/Joey_data_retrieval/CRIMEdata_API_Joey.ipynb) , this is to retrieve CRIME values of USA data. For the CRIME visualisations, please follow Niki’s instructions. Please ensure you have an API key for the code to be able to retrieve from the database. There is the option to save all 4 API datasets into csv files but for the purposes of our project we only used API_1.  
- The notebook *[Transaction dataset.ipynb](https://github.com/Data-2-CFG/group-1-project/tree/main/Nicol_data_retrieval) , this is to merge the fraudTest and fraudTrain datasets to obtain a more complete dataset to work with for the visualisations.  
- The notebook *[CovidVisualisations_Joey.ipynb](https://github.com/Data-2-CFG/group-1-project/blob/main/Joey_data_retrieval/CovidVisualisations_Joey.ipynb), this is to run the data cleansing and preparation aspect before finally coming to creating the visualisations. All the datasets here are either retrievable from the previous steps or will be created into dataframes which can then be exported into csv files. Comments and descriptions are provided throughout the notebook to guide you through the code. Feel free to use the graphs for your own perusal.   
- The notebook *[Data visualisation_Nicol_def.ipynb](https://github.com/Data-2-CFG/group-1-project/tree/main/Nicol_data_retrieval), this is to run the data cleansing and preparation aspect before finally coming to creating the visualisations.   
