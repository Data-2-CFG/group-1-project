# -*- coding: utf-8 -*-
"""
Created on Mon May 23 01:12:11 2022

@author: intern7
"""

from preprocessing_pipeline import load_dataset
from config import*

def load_crime_data():
    
    US_Population=pd.read_csv(US_POPULATION-PATH, parse_dates=['DATE'])
    CCATM_Fraud_df= pd.read_csv(CCATM_FRAUD-PATH)
    
    return US_Population, CCATM_Fraud_df
    

def plot_crime_rate_year(CCATM_Fraud_withCR):

    fig = plt.figure(figsize=(4,3))

    Crime_Rate=CCATM_Fraud_withCR['Crime Rate']
    Year_CR=CCATM_Fraud_withCR['Year']

    plt.plot(Year_CR,Crime_Rate,color='blue')
    plt.grid(visible=True)
    plt.xlabel('Year')
    plt.ylabel('Crime Rate')
    
    return st.pyplot(fig)

def plot_crime_rate_population(CCATM_Fraud_withCR, Only_pop_CR_pctCH):

    fig,ax=plt.subplots(figsize=(4,3))

    x=Only_pop_CR_pctCH['Year']
    y1=Only_pop_CR_pctCH['Crime Rate']
    y2=Only_pop_CR_pctCH['Population']
    
    ax.set_xlabel("Year")
    ax.set_ylabel("Pct_Change")
    ax.grid(visible=True)
    
    ax.plot(x,y1,color='dodgerblue',label="Crime Rate")
    ax.plot(x,y2,color='blue',label="Population")
    
    plt.legend()
    
    return st.pyplot(fig)
 
def plot_credit_card_fraud_population_time(CR_pct_change_3YRS):
    
    fig,ax=plt.subplots(figsize=(4,3))

    x=CR_pct_change_3YRS['Year']
    y1=CR_pct_change_3YRS['Crime Rate']
    y2=CR_pct_change_3YRS['Population']

    ax.set_xlabel("Year",loc='center')
    ax.set_ylabel("Pct_Change")
    
    ax.plot(x,y1,color='dodgerblue',label="Crime Rate")
    ax.plot(x,y2,color='blue',label="Population")
    plt.xticks(x)
    
    plt.legend()
    
    return st.pyplot(fig)

def crime_pipeline(crime_graph):
    
    US_Population, CCATM_Fraud_df = load_crime_data()
    CCATM_Fraud_df.drop('incident_count',axis=1,inplace=True)
    CCATM_Fraud_df.rename(columns={"offense_count": "Offense Count", "data_year": "Year"},inplace=True)
    US_Population.rename(columns={"DATE": "Date", "POPTOTUSA647NWDB": "Population"},inplace=True)

    Year=[]
    Date=[]
    
    #for each date add the date to the list "Date", get the Year and add it to the list "Year"
    for i in range(len(US_Population['Date'])):
        Y=US_Population['Date'].iloc[i].year
        Year.append(Y)
        Date.append(US_Population['Date'].iloc[i])
    
    #create a dataframe with the 2 lists and transpose it to have dates and years in columns
    Pop_Date_df=pd.DataFrame([Date,Year]).transpose()
    Pop_Date_df.rename(columns={0: "Date",1: "Year"},inplace=True)
    US_Population=Pop_Date_df.set_index('Date').join(US_Population.set_index('Date'))
    US_Population.reset_index(inplace=True)
    US_Population.drop('Date',axis=1, inplace=True)
    CCATM_Fraud_withPOP_df=US_Population.set_index('Year').join(CCATM_Fraud_df.set_index('Year'))
    CCATM_Fraud_withPOP_df.dropna(axis=0, how='any', subset=['Offense Count'], inplace=True)
    CCATM_Fraud_withPOP_df.reset_index(inplace=True)
    
    crime_rate_by_year=[]
    Year_cr=[]

    # for each record get the offense, divide for the population and multiply by 100.000, store the ith Year and Crime rata 
    # in the lists "crime_rate_by_year" and "Year_cr"
    for i in range(len(CCATM_Fraud_withPOP_df['Offense Count'])):
        CR=100000*CCATM_Fraud_withPOP_df['Offense Count'].iloc[i]/CCATM_Fraud_withPOP_df['Population'].iloc[i]
        Y=CCATM_Fraud_withPOP_df['Year'].iloc[i]
        crime_rate_by_year.append(CR)
        Year_cr.append(Y)
    
    #Create a new dataframe with the new lists and transpose it to have Year and Crime rate as columns    
    CCATM_Fraud_CrimeR=pd.DataFrame([Year_cr,crime_rate_by_year]).transpose()
    CCATM_Fraud_CrimeR.rename(columns={0: "Year",1: "Crime Rate"},inplace=True)
    CCATM_Fraud_CrimeR['Year']=CCATM_Fraud_CrimeR['Year'].astype(int)
    CCATM_Fraud_withCR=CCATM_Fraud_CrimeR.set_index('Year').join(CCATM_Fraud_withPOP_df.set_index('Year'))
    CCATM_Fraud_withCR.reset_index(inplace=True)
    Only_pop_CR_df=CCATM_Fraud_withCR.drop(['Offense Count'],axis=1)
    Only_pop_CR_df=Only_pop_CR_df.set_index('Year')
    Only_pop_CR_pctCH=Only_pop_CR_df.pct_change()
    Only_pop_CR_pctCH.reset_index(inplace=True)
    CR_pct_change_3YRS=Only_pop_CR_pctCH[Only_pop_CR_pctCH['Year']>=2018]
    
    if crime_graph == "Crime Rate trends since 1991":
        return plot_crime_rate_year(CCATM_Fraud_withCR)

    if crime_graph == "Crime Rate vs. Population":
        return plot_crime_rate_population(CCATM_Fraud_withCR, Only_pop_CR_pctCH)
    
    if crime_graph == "Creditcard Fraud Rate vs. Population":
        return plot_credit_card_fraud_population_time(CR_pct_change_3YRS)
    
