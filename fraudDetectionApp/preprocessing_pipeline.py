# -*- coding: utf-8 -*-
"""
Created on Sun May 22 16:30:27 2022

@author: intern7
"""

from config import *

@st.cache(allow_output_mutation=True)
def load_dataset(dataset_name):
    
    if dataset_name == "Creditcard Fraud Detection":
        
        #Importing train and test dataset
        transactions_train_df = pd.read_csv("C:/Users/intern7/Documents/fraudDetectionApp/data/fraudTrain.csv", parse_dates=["trans_date_trans_time"])
        transactions_test_df = pd.read_csv("C:/Users/intern7/Documents/fraudDetectionApp/data/fraudTest.csv", parse_dates=["trans_date_trans_time"])
        
        #Appending both datasets
        df = transactions_train_df.append(transactions_test_df, ignore_index=True)
        
    return df

def create_variables(df):
    
    ##1 - Business hours / Non business hours
    
    ### Creating a column for business_hour with zero as default
    df["business_hour"] = int(0)
    
    ###Considering business hours between 8:00-19:00
    start = dt.datetime.strptime("08:00:00", "%H:%M:%S").time()
    end = dt.datetime.strptime("19:00:00", "%H:%M:%S").time()
    
    ###Defining a mask for the query that catches data within the defined range
    businessHour_mask = df["trans_date_trans_time"].dt.time.between(start, end)
    
    ###Setting numbers that fit into encoding to 1
    df["business_hour"][businessHour_mask] = 1
    
    ##2 - Weekdays / Weekends
    
    ### Defining weekdays bin, being weekdays from Monday to Friday (0-4) and weekends Saturday and Sunday (5-6). Weekdays will be labelled as 1 and weekends as 0
    weekDay_list = [0,1,2,3,4]
    weekEnd_list = [5,6]
    
    ###Creating a new column is_weekday
    
    df["is_weekday"] = int(0)
    
    ###Applying the weekday rule into the dataset
    df["is_weekday"][df["trans_date_trans_time"].dt.weekday.isin(weekDay_list)] = 1
    df["is_weekday"][df["trans_date_trans_time"].dt.weekday.isin(weekEnd_list)] = 0
      
    ##3 - Months
    
    ###Extracting the month
    df["month"] = df["trans_date_trans_time"].dt.strftime("%m")
      
    ###Transforming month into an integer
    df["month"] = df["month"].astype(int)
    
    ##4 - Time since las transaction in the same card
    
    ###Creating a function to parse time difference between rows
    
    def time_difference(df):
      df["time_diff"] = df["unix_time"] - df["unix_time"].shift()
      return df
    
    ###Applying the function to dataset grouped by creditcard number
    
    df = df.groupby("cc_num").apply(time_difference)
    
    ###Replacing NaN with zeroes
    df['time_diff'] = df['time_diff'].fillna(0)
    
    ##5 - Frequency of transacations in the same card in time intervals of 1 and 7 days
    
    ###Creating functions to extract frequency of transactions in the time intervals
    def last_day(df):
        temp = pd.Series(df.index, index = df["trans_date_trans_time"], name='count_1_day').sort_index()
        count_1_day = temp.rolling('1d').count() - 1
        count_1_day.index = temp.values
        df['count_1_day'] = count_1_day.reindex(df.index)
        return df
    
    def last_week(df):
        temp = pd.Series(df.index, index = df["trans_date_trans_time"], name='count_7_days').sort_index()
        count_7_days = temp.rolling('7d').count() - 1
        count_7_days.index = temp.values
        df['count_7_days'] = count_7_days.reindex(df.index)
        return df
    
    ###Applying functions to dataframe
    
    df = df.groupby('cc_num').apply(last_day)
    df = df.groupby('cc_num').apply(last_week)
    
    ##6 - Numeric age
    
    ###Transforming date of birth into numeric age
    yearCharacters = 4
    currentYear = int(dt.datetime.now().strftime("%Y"))
    
    df["age"] = currentYear - df["dob"].str[:yearCharacters].astype(int)
    
    ###Dropping the original column "dob"
    df.drop(['dob'], axis=1, inplace=True)
        
    return df

def drop_columns(df):
    
    #Removing irrelevant variables

    irrelevantVar_list = ["first",
                      "last", 
                      "street", 
                      "zip",
                      "lat",
                      "job",
                      "long",
                      "cc_num", 
                      "unix_time",
                      "trans_date_trans_time",
                      "trans_num", 
                      "merch_lat",
                      "merch_long"]

    df.drop(irrelevantVar_list, axis=1, inplace=True)
    
    return df

def encode_dataset(df):
    
        #Encoding variables
    
    ##1 - Target Encoding merchant categories
    
    ###Getting the means for each category
    merchantMeans_dict = df.groupby('category')['is_fraud'].mean().to_dict()
    
    ###Replacing the categorical labels with the means
    df['category'] = df['category'].map(merchantMeans_dict)
    
    ##2 - Target Encoding states
    
    ###Getting the means for each state
    statetMeans_dict = df.groupby('state')['is_fraud'].mean().to_dict()
    
    ###Replacing the categorical labels with the means
    df['state'] = df['state'].map(statetMeans_dict)
    
    
    ##3 - Target Encoding cities
    
    cityMeans_dict = df.groupby('city')['is_fraud'].mean().to_dict()
    
    
    df["city"] =  df["city"].map(cityMeans_dict)
    
    ##4 - Target Encoding the merchant
    
    merchantMeans_dict = df.groupby("merchant")['is_fraud'].mean().to_dict()
    
    df["merchant"] = df['merchant'].map(merchantMeans_dict)
    
    ##5 - Label encoding Male / Female
    
    ###Defining 1 as male and 2 as female and replacing values
    df["gender"].replace('F', 0, inplace=True)
    df["gender"].replace('M', 1, inplace=True)
    
    return df

@st.cache    
def preprocessing_pipeline(dataset_name):
    
    df = load_dataset(dataset_name)
    df = create_variables(df)
    df = drop_columns(df)
    df = encode_dataset(df)
    
    return df
