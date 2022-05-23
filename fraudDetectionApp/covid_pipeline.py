# -*- coding: utf-8 -*-
"""
Created on Mon May 23 13:24:12 2022

@author: intern7
"""
from config import *
from preprocessing_pipeline import *

def load_covid_data():
    covid2020_data = pd.read_csv(COVID-2020-PATH)
    covid2021_data = pd.read_csv(COVID-2021-PATH)

    return covid2020_data, covid2021_data

def covid_pipeline(covid2020_data, covid2021_data):
    covid2020_data['date_value'] = pd.to_datetime(covid2020_data['date_value'])
    covid2021_data['date_value'] = pd.to_datetime(covid2021_data['date_value'])

    USACovid2020_df = covid2020_data.loc[(covid2020_data['country_code'] == 'USA') & (covid2020_data['stringency_actual'] != 0)]
    USACovid2021_df = covid2021_data.loc[(covid2021_data['country_code'] == 'USA') & (covid2021_data['stringency_actual'] != 0)]
    
    USACovid2020_data = USACovid2020_df
    USACovid2021_data = USACovid2021_df
    
    USACovid2020_data['date_value'] = pd.to_datetime(USACovid2020_data['date_value'])
    USACovid2021_data['date_value'] = pd.to_datetime(USACovid2021_data['date_value'])

    USACovid2020_data.drop(['confirmed', 'deaths', 'stringency', 'stringency_legacy', 'stringency_legacy_disp'], axis=1, inplace=True)
    USACovid2021_data.drop(['confirmed', 'deaths', 'stringency', 'stringency_legacy', 'stringency_legacy_disp'], axis=1, inplace=True)
    
    Year=[]
    Month=[]
    Month_Year=[]
    Day_Month_Year=[]
    Day=[]
    Date=[]
    
    for i in range(len(USACovid2020_data['date_value'])):
        Y=USACovid2020_data['date_value'].iloc[i].year
        M=USACovid2020_data['date_value'].iloc[i].month
        D=USACovid2020_data['date_value'].iloc[i].day
        M_Y=f'{M}-{Y}'
        D_M_Y=f'{D}-{M}-{Y}'
        Year.append(Y)
        Month.append(M)
        Month_Year.append(M_Y)
        Day_Month_Year.append(D_M_Y)
        Day.append(D)
        Date.append(USACovid2020_data['date_value'].iloc[i])
    
    covidDate2020_df=pd.DataFrame([Date,Day,Month,Year,Day_Month_Year,Month_Year]).transpose()
    covidDate2020_df.rename(columns={0: "date_value",1: "Day", 2:"Month", 3: "Year", 4: "Day-Month-Year", 5:"Month-Year"},inplace=True)
    
    USACovid2020_data=covidDate2020_df.set_index('date_value').join(USACovid2020_data.set_index('date_value'))
    USACovid2020_data.reset_index(inplace=True)
    USACovid2020Monthly = USACovid2020_data[['Month', 'stringency_actual']].groupby(by='Month').mean()
    USACovid2020Monthly.reset_index(inplace=True)


    Year=[]
    Month=[]
    Month_Year=[]
    Day_Month_Year=[]
    Day=[]
    Date=[]
    
    for i in range(len(USACovid2021_data['date_value'])):
        Y=USACovid2021_data['date_value'].iloc[i].year
        M=USACovid2021_data['date_value'].iloc[i].month
        D=USACovid2021_data['date_value'].iloc[i].day
        M_Y=f'{M}-{Y}'
        D_M_Y=f'{D}-{M}-{Y}'
        Year.append(Y)
        Month.append(M)
        Month_Year.append(M_Y)
        Day_Month_Year.append(D_M_Y)
        Day.append(D)
        Date.append(USACovid2021_data['date_value'].iloc[i])
    
    covidDate2021_df=pd.DataFrame([Date,Day,Month,Year,Day_Month_Year,Month_Year]).transpose()
    
    covidDate2021_df.rename(columns={0: "date_value",1: "Day", 2:"Month", 3: "Year", 4: "Day-Month-Year", 5:"Month-Year"},inplace=True)
    
    USACovid2021_data=covidDate2021_df.set_index('date_value').join(USACovid2021_data.set_index('date_value'))

    USACovid2021_data.reset_index(inplace=True)

    USACovid2021Monthly = USACovid2021_data[['Month', 'stringency_actual']].groupby(by='Month').mean()

    USACovid2021Monthly.reset_index(inplace=True)
    
    
    transactions_train_df = pd.read_csv(TRANSACTIONS-TRAIN-PATH, parse_dates=["trans_date_trans_time"])
    transactions_test_df = pd.read_csv(TRANSACTIONS-TEST-PATH, parse_dates=["trans_date_trans_time"])
    
    #Appending both datasets
    transactions_df = transactions_train_df.append(transactions_test_df, ignore_index=True)
    
    
    transactions2020_df = transactions_df.loc[(transactions_df['trans_date_trans_time'] >= '2020-01-01')]
    transactions2019_df = transactions_df.loc[(transactions_df['trans_date_trans_time'] < '2020-01-01')]
    fraudTrans2019_df = transactions2019_df.loc[(transactions2019_df['is_fraud'] == 1)]
    fraudTrans2019_df.reset_index(inplace=True)
    
    #setting variables to store them in temporarily
    Year=[]
    Month=[]
    Month_Year=[]
    Day_Month_Year=[]
    Day=[]
    Date=[]
    
    #looping through the timestamps so we can separate them out
    for i in range(len(fraudTrans2019_df['trans_date_trans_time'])):
        Y=fraudTrans2019_df['trans_date_trans_time'].iloc[i].year
        M=fraudTrans2019_df['trans_date_trans_time'].iloc[i].month
        D=fraudTrans2019_df['trans_date_trans_time'].iloc[i].day
        M_Y=f'{M}-{Y}'
        D_M_Y=f'{D}-{M}-{Y}'
        Year.append(Y)
        Month.append(M)
        Month_Year.append(M_Y)
        Day_Month_Year.append(D_M_Y)
        Day.append(D)
        Date.append(fraudTrans2019_df['trans_date_trans_time'].iloc[i])
    
    #saving it to a new DF to use
    Date2019_df=pd.DataFrame([Date,Day,Month,Year,Day_Month_Year,Month_Year]).transpose()
    Date2019_df.rename(columns={0: "trans_date_trans_time",1: "Day", 2:"Month", 3: "Year", 4: "Day-Month-Year", 5:"Month-Year"},inplace=True)
    fraudTrans2019_df=Date2019_df.set_index('trans_date_trans_time').join(fraudTrans2019_df.set_index('trans_date_trans_time'))
    fraudTrans2019_df.reset_index(inplace=True)
    
    fraudTrans2019_df.drop(['index'], axis=1, inplace=True)
    fraudTrans2019Monthly = fraudTrans2019_df[['Month', 'is_fraud']].groupby(by='Month').count()

    fraudTrans2020_df = transactions2020_df.loc[(transactions2020_df['is_fraud'] == 1)]
    fraudTrans2020_df.reset_index(inplace=True)
    
    Year=[]
    Month=[]
    Month_Year=[]
    Day_Month_Year=[]
    Day=[]
    Date=[]
    
    for i in range(len(fraudTrans2020_df['trans_date_trans_time'])):
        Y=fraudTrans2020_df['trans_date_trans_time'].iloc[i].year
        M=fraudTrans2020_df['trans_date_trans_time'].iloc[i].month
        D=fraudTrans2020_df['trans_date_trans_time'].iloc[i].day
        M_Y=f'{M}-{Y}'
        D_M_Y=f'{D}-{M}-{Y}'
        Year.append(Y)
        Month.append(M)
        Month_Year.append(M_Y)
        Day_Month_Year.append(D_M_Y)
        Day.append(D)
        Date.append(fraudTrans2020_df['trans_date_trans_time'].iloc[i])

    Date2020_df=pd.DataFrame([Date,Day,Month,Year,Day_Month_Year,Month_Year]).transpose()
    Date2020_df.rename(columns={0: "trans_date_trans_time",1: "Day", 2:"Month", 3: "Year", 4: "Day-Month-Year", 5:"Month-Year"},inplace=True)

    fraudTrans2020_df=Date2020_df.set_index('trans_date_trans_time').join(fraudTrans2020_df.set_index('trans_date_trans_time'))
    fraudTrans2020_df.reset_index(inplace=True)
    
    fraudTrans2020_df.drop(['index'], axis=1, inplace=True)

    USACovid2020Monthly = USACovid2020Monthly.set_index('Month')
    stringeActualPctChange = USACovid2020Monthly.pct_change()
    stringeActualPctChange.reset_index(inplace=True)

    USACovid2021Monthly = USACovid2021Monthly.set_index('Month')
    stringeActualPctChange2021 = USACovid2021Monthly.pct_change()
    stringeActualPctChange2021.reset_index(inplace=True)
    
    fraudTrans2020Monthly = fraudTrans2020_df[['Month', 'is_fraud']].groupby(by='Month').count()
    fraudTransPctChange2020 = fraudTrans2020Monthly.pct_change()
    fraudTransPctChange2020.reset_index(inplace=True)
    fraudTransPctChange2020.rename(columns={'is_fraud': "is_fraud_2020"},inplace=True)
    fraudTransPctChange2019 = fraudTrans2019Monthly.pct_change()
    fraudTransPctChange2019.reset_index(inplace=True)
    fraudTransPctChange2019.rename(columns={'is_fraud': "is_fraud_2019"},inplace=True)
    covidVtransGraphDF = stringeActualPctChange.set_index('Month').join(fraudTransPctChange2020.set_index('Month'))
    covidVtransGraphDF.reset_index(inplace=True)
    covidVtransGraphDF2 = covidVtransGraphDF.set_index('Month').join(fraudTransPctChange2019.set_index('Month'))
    covidVtransGraphDF2.reset_index(inplace=True)
    covidVtransGraphDF2.fillna(0, inplace=True)
    
    return USACovid2020_data, USACovid2021_data, covidVtransGraphDF2

