# -*- coding: utf-8 -*-
"""
Created on Mon May 23 01:12:11 2022

@author: intern7
"""

from preprocessing_pipeline import load_dataset
from config import*

def load_crime_data():
    
    US_Population=pd.read_csv("C:/Users/intern7/Documents/fraudDetectionApp/data/US_total_population.csv", parse_dates=['DATE'])
    CCATM_Fraud_df= pd.read_csv("C:/Users/intern7/Documents/fraudDetectionApp/data/CCATMFraudCrimeRate1991-2020.csv")
    
    return US_Population, CCATM_Fraud_df

def plot_crime_rate_fraud(CCATM_Fraud_withCR):
    
    transactions_train_df = pd.read_csv("C:/Users/intern7/Documents/fraudDetectionApp/data/fraudTrain.csv")
    transactions_test_df = pd.read_csv("C:/Users/intern7/Documents/fraudDetectionApp/data/fraudTest.csv")
    
    #Appending both datasets
    transaction_df = transactions_train_df.append(transactions_test_df, ignore_index=True)
    transaction_df['trans_date_trans_time'] = pd.to_datetime(transaction_df['trans_date_trans_time'])
    transaction_df['dob'] = pd.to_datetime(transaction_df['dob'])
    
    transaction_df.drop(['Unnamed: 0', 'cc_num', 'merchant', 'category',
       'amt', 'first', 'last', 'gender', 'street', 'zip',
       'lat', 'long', 'job', 'dob', 'unix_time',
       'merch_lat', 'merch_long'],axis=1,inplace=True)

    transaction_df.rename(columns={"trans_date_trans_time": "Date","city": "City","state":"State","city_pop":"City_population","trans_num":"Transaction_number"},inplace=True)
    
    Year=[]
    Date=[]
    
    #for each record in the transaction dataset, get the year from the date and append date and year to 2 new lists
    for i in range(len(transaction_df['Date'])):
        Y=transaction_df['Date'].iloc[i].year
        Year.append(Y)
        Date.append(transaction_df['Date'].iloc[i])
    
    #Create a new dataframe with our 2 new lists and transpose it to have date and year as columns
    Date_df=pd.DataFrame([Date,Year]).transpose()
    Date_df.head()
    
    Date_df.rename(columns={0: "Date",1: "Year"},inplace=True)
    
    transaction_df=Date_df.set_index('Date').join(transaction_df.set_index('Date'))
    
    transaction_df.reset_index(inplace=True)
    
    Fraudulent_trans=transaction_df[transaction_df['is_fraud']==1]
    
    Legitimate_trans=transaction_df[transaction_df['is_fraud']==0]
    
    Fraudulent_trans2019=Fraudulent_trans[Fraudulent_trans['Year']==2019]
    FT2019_count=Fraudulent_trans2019['Transaction_number'].count()
    
    Fraudulent_trans2020=Fraudulent_trans[Fraudulent_trans['Year']==2020]
    FT2020_count=Fraudulent_trans2020['Transaction_number'].count()
    
    #filter and count 2019 legitimate transactions
    Legitimate_trans2019=Legitimate_trans[Legitimate_trans['Year']==2019]
    LT2019_count=Legitimate_trans2019['Transaction_number'].count()
    
    #filter and count 2020 legitimate transactions
    Legitimate_trans2020=Legitimate_trans[Legitimate_trans['Year']==2020]
    LT2020_count=Legitimate_trans2020['Transaction_number'].count()
    
    CCATM_Fraud_withCR_2019_2020=CCATM_Fraud_withCR[CCATM_Fraud_withCR['Year']>=2019]
    
    Fraudulent_trans_2019_2020=Fraudulent_trans[Fraudulent_trans['Year']<=2020]
    
    Frauds_Count_2019_2020=Fraudulent_trans_2019_2020.groupby(['Year'])['is_fraud'].count()
    Frauds_Count_2019_2020=pd.DataFrame(Frauds_Count_2019_2020)
    
    Frauds_Count_2019_2020.reset_index(inplace=True)
    
    CCATM_Fraud_withCR_2019_2020=Frauds_Count_2019_2020.set_index('Year').join(CCATM_Fraud_withCR_2019_2020.set_index('Year'))
    
    CCATM_Fraud_withCR_2019_2020.rename(columns={'is_fraud':'Fraudulent Transactions','Offense Count':'Overall US Offenses'},inplace=True)
    
    CCATM_Fraud_withCR_2019_2020.reset_index(inplace=True)
    
    FraudsRate=pd.DataFrame(100000*CCATM_Fraud_withCR_2019_2020['Fraudulent Transactions']/CCATM_Fraud_withCR_2019_2020['Population'])
    FraudsRate.rename(columns={0:'DF Frauds Rate'},inplace=True)
    CCATM_Fraud_withCR_2019_2020=CCATM_Fraud_withCR_2019_2020.join(FraudsRate)
    
    fig = plt.figure()
    
    y = CCATM_Fraud_withCR_2019_2020[['Crime Rate','DF Frauds Rate']]
    
    x = CCATM_Fraud_withCR_2019_2020["Year"] 

    plt.bar(x, y)
    
    
    plt.ylabel('Rate')
    plt.legend(loc='upper right')
    
        
    return st.pyplot(fig)
    
    st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

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
    
    if crime_graph == "Credit Card Fraud Rate vs. Population":
        return plot_credit_card_fraud_population_time(CR_pct_change_3YRS)
    
    if crime_graph == "Fraud Rates in the USA vs. Creditcard Fraud Rates in our dataset":
        return plot_crime_rate_fraud(CCATM_Fraud_withCR)