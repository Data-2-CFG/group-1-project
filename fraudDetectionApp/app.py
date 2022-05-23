from config import *
from preprocessing_pipeline import *
from model_pipeline import *
from crime_pipeline import *
from covid_pipeline import *
from covid_plots import *
from exploratory_plots import *

with st.sidebar:
    choose = option_menu("The Fraud Detection Project", ["About", "Fraud Detection", "Fraud and Crime", "Fraud and COVID", "Conclusion"],
                         menu_icon="bank")

dataset_name = "Creditcard Fraud Detection"
display_df = load_dataset(dataset_name)

if choose == "About":
    
        st.write("""
        # About
        Credit card fraud is as prevalent as ever, with online transactions becoming more common. The aim of our project is to be able to detect whether new transactions are fraudulent or not through the use of different machine learning techniques, as well as to identify patterns in credit card fraud using data visualisations. The project uses a dataset containing 26 features and other external data was also added, such as information on COVID restrictions and crime rates 
                 """)
                 
        with st.expander("Guiding Questions", expanded=False):
             st.write(
                 """    
                 - How to predict if new transactions are fraudulent or not? - Focus Question
                 - What is the relationship between crime rates and  fraud rates?
                 - Did the effects of COVID restrictions result in more creditcard fraud than different periods of time throughout the year?

             """)

        st.markdown("A project by Ilaria Alessandrelli, Joey Chan, Juliana Novaes, Nicol Saccardi and Rumaanah Ellahi")


if choose == "Fraud Detection":
    st.write("""
    # Explore machine learning models for fraud detection
    Learn how different classification models perform on creditcard fraud detection       
             """)
             
    dataset_name = st.selectbox("Select Dataset",
                                ("Creditcard Fraud Detection",
                                     "")
                                )
    
    st.subheader("{} Dataset".format(dataset_name))
    st.write(
    """    
        Open access dataset containing creditcard transactions in the USA and their label as fraud or not .
        
    """)
    st.write(display_df.head(5))
    st.write("Shape of the Dataset", display_df.shape)
    st.write("Number of Classes", len(display_df["is_fraud"].unique()))
    
    st.subheader("Data Preparation")
    
    with st.expander("Preprocessing Pipeline", expanded=False):
            st.write(
                """    
                - Choosing a labelled dataset
                - Importing data
                - Identifying missing data
                - Dropping variables that could lead to biases or overfit
                - Adding new variables from existing data
                - Encoding categorical variables
                - Dividing dataset into train and test
                - Applying machine learning algorithm
                - Evaluating results

            """)
            
    st.subheader("Exploratory Analysis")
    
     
    exp_graph = st.selectbox("Select Chart", 
                            ("Fradulent Transactions vs. Legitimate Transactions",
                             "")
                           )
    
    st.subheader(exp_graph)
    
    col1, col2 = st.columns(2)
    

    with col1:

        if exp_graph == "Fradulent Transactions vs. Legitimate Transactions":
            plot_fraud_percentage(display_df)
    
    
    with col2: 
        st.write("It is visible that we have a very unbalanced dataset, with over 99% of transactions being legit and less than 1% fraudulent ones. This characteristic had to be taken into consideration when choosing a machine learning model that would suit our needs. For our evaluation, it was more important to have good precision and recall metrics, so that the model would be less likely to cause false positives or false negatives")
    
    clf_name = st.selectbox("Select Classifier", 
                            ("Decision Tree",
                             "Logistic Regression")
                           )
    
    st.subheader("{} Classifier".format(clf_name))
        
    y_test, y_pred = model_pipeline(dataset_name, clf_name)
    
    accuracy, precision, recall = print_results(y_test, y_pred)

        
    if clf_name == "Decision Tree":
            st.write("A model that builds itself as a pathway to a decision. It includes conditional ‘control’ statements to classify data, starting at a single point (or ‘node’) which then branches (or ‘splits’) in two or more directions. Each branch offers different possible outcomes, incorporating a variety of decisions and chance events until a final  outcome is achieved.")

    if clf_name == "Logistic Regression":
            st.write("A model that measures the probability of one event taking placeby having the log-odds - the logarithm of the odds - for the event be a linear combination of one or more independent variables")

    col1, col2 = st.columns(2)
    
    with col1:
      
        st.subheader("Confusion Matrix")
        plot_matrix(y_test, y_pred)

    with col2:
        
        st.write("Accuracy: ",accuracy)
        st.write("Precision: ", precision)
        st.write("Recall: ", recall)
       
    
if choose == "Fraud and Crime":
    st.write("""
    # Understand how credit card fraud relates to crime rates
    
    What are crime rates in comparison to the credit card fraud rate?
            """)
    
        
    st.subheader("Data Gathering")
    
    with st.expander("FBI Crime Data API ", expanded=False):
        st.write(
        """    
            The API returns JSON or CSV data. We chose this endpoint as it provided data about offences divided by type of offence, one of which was “credit-card-automated-teller-machine-fraud”. The response we got was a nested dictionary, and our data was the value of the key ‘results’.
        """)
        
        US_Population, CCATM_Fraud_df = load_crime_data()
            
        st.write(CCATM_Fraud_df.head(4))
        st.write("Shape of the Dataset", CCATM_Fraud_df.shape)
        
        
    with st.expander("US Population: World Bank ", expanded=False):
         st.write(
         """    
             Open access dataset containing the total population of the United States over time.
         """)
         
             
         st.write(US_Population.head(4))
         st.write("Shape of the Dataset", US_Population.shape)
         
    with st.expander("Creditcard Fraud Detection ", expanded=False):
        
         st.write(
         """    
             Open access dataset containing credit card transactions in the USA and their label as fraud or not .
             
         """)
         
         st.write(display_df.head(4))
         st.write("Shape of the Dataset", display_df.shape)
         
         
    st.subheader("Data Preparation")
    
    with st.expander("Preprocessing Pipeline", expanded=False):
        st.write(
        """    
        - Importing datasets and adjusting data types
        - Dropping irrelevant columns and renaming other columns
        - Merging datasets
        - Building missing data (Year extraction from date)
        - Calculating Crime Rates and Percentage Change
        - Building graphs

        """)
        
    
    st.subheader("""
     Exploratory Analysis
     """)

    crime_graph = st.selectbox("Select Chart", 
                        ("Crime Rate trends since 1991",
                         "Crime Rate vs. Population",
                         "Creditcard Fraud Rate vs. Population",
                         "Fraud Rates in the USA vs. Creditcard Fraud Rates in our dataset")
                       )
    
    if crime_graph == "Crime Rate trends since 1991":
        st.subheader('Crime Rate trend vs. Time')
    
    if crime_graph == "Crime Rate vs. Population":
        st.subheader('Crime Rate Change vs. Population Change')
    
    if crime_graph == "Creditcard Fraud Rate vs. Population":
        st.subheader('Creditcard Fraud vs. Population Change over the last 3 years')
        
    if crime_graph == "Fraud Rates in the USA vs. Creditcard Fraud Rates in our dataset":
        st.subheader("Fraud Rates in the USA vs. Creditcard Fraud Rates in our dataset")
    
    col1, col2 = st.columns(2)
    

    with col1:
        crime_pipeline(crime_graph)

    with col2:
        
        if crime_graph == "Crime Rate trends since 1991":
            st.write("From this graph we can see a steady incline in crime rates over the years, between 1991 to 2010, crime rose to 28% and in 2010 to 2020, crime increased from 28% to 43%, averaging crime rate at an approximate growth of 14% per decade.")
        
        if crime_graph == "Crime Rate vs. Population":
            st.write("From this line graph we see both crime rate and population. The population line remains at a constant with hardly any change over the almost three decade period, unlike the crime rate measurement. Although there was a continuous fluctuation in crime rate, with the highest point at 2000 and the lowest at 2012, the rate of population did not change. It is therefore safe to say the rate of population had no effect on the rate of crime.")
            
        if crime_graph == "Credit Card Fraud Rate vs. Population":
            st.write('This line graph focuses on a 3 year period between 2017 to 2020, again it depicts the percentage change of Crime Rate and Population Change. As previously seen, population change has remained at a constant level. It is evident to see the consistent change in crime rate however what is most interesting is the highest peak being at the end of  2019 which is then followed by a significant drop. As mentioned earlier this may suggest COVID19 lockdowns might have had an effect on crime rates however data does not surpass 2020 so it can not be said for sure.')
            
if choose == "Fraud and COVID":
    
       st.write("""
       # Understand how credit card fraud relates to COVID restrictions
       
       Did COVID restrictions result in more Credit Card Fraud?
               """)
               
       st.subheader("Data Gathering")
       
       with st.expander("Oxford COVID-19 Government Response Tracker API", expanded=False):
           st.write(
           """    
               An API that allows tracking and comparing government responses to COVID 19 in over 180 countries. It contains data collected since January 2020 and a stringency index showing the measures in every country. 
               
           """)
           
           covid2020_data, covid2021_data = load_covid_data()
           covid_display = covid2020_data.append(covid2021_data, ignore_index=True)
               
           st.write(covid_display.head(4))
           st.write("Shape of the Dataset", covid_display.shape)
            
       with st.expander("Creditcard Fraud Detection ", expanded=False):
           
            st.write(
            """    
                Open access dataset containing credit card transactions in the USA and their label as fraud or not .
                
            """)
           
            
            st.write(display_df.head(4))
            st.write("Shape of the Dataset", display_df.shape)
            
         
       st.subheader("Data Preparation")
    
       with st.expander("Preprocessing Pipeline", expanded=False):
            st.write(
                """    
                - Importing data
                - Merging data sets
                - Rebuilding missing data
                - Standardisation
                - Normalisation
                - Deduplication
                - Verification and enrichment
                - Exporting data

            """)
               
       st.subheader("""
           Exploratory Analysis
           """)

       covid_graph = st.selectbox("Select Chart", 
                          ("COVID Restrictions in the USA over Time",
                           "COVID Restrictions vs. Fraud"))
                        
       USACovid2020_data, USACovid2021_data, covidVtransGraphDF2 = covid_pipeline(covid2020_data, covid2021_data)

       if covid_graph == "COVID Restrictions in the USA over Time":
           st.subheader('COVID Stringency vs. Time')
           covid_plot_stringency(USACovid2020_data, USACovid2021_data)
           st.write("The sharp rise in stringency values in 2020-03 indicates when COVID19 first impacted the USA government's policies. From these we are able to see the dips and rises according to what you can infer as seasonal changes. There is a slight increase of stringency in 2020-11 at the beginning of winter, then as winter draws to an end the stringency values slowly decrease. This is not to say they are gone completely. With COVID19 there was a lot of uncertainty and even though Summer came around 2021-05/06 with stringency being at the lowest levels for the past year, it sharply increased back to 63 possibly due to the increase in number of COVID19 cases.")
      
       if covid_graph == "COVID Restrictions vs. Fraud":
          st.subheader('Stringency Change Percentage vs. Fraud')
          covid_plot_stringency_fraud(covidVtransGraphDF2)
          st.write("A comparison of the distribution of stringency actual values between 2020 and 2021. This is to see how the USA changed their stringency as we got to understand COVID19 better. They share the same x and y axes so you can see the difference in values immediately.  With these graphs it is clear to see that consistently higher levels of stringency were present for the year of 2021. There is a spike for the year 2020 but there was more uncertainty and so that is why there are values towards the lower end of the spectrum. ")
     
if choose == "Conclusions":
    
       
       st.write("""
           # Conclusion
           - We were able to determine that fraud only counts as either 0.5% or 0.6% of all transactions in 2019 and 2020 in our dataset. 
           - We were able to determine that the best performing model to predict fraud in creditcard transactions in our case was Decision Tree
           - We were able to determine that the number of credit card frauds in our dataset remained stable between 2019 and 2020, as well as the general rates of fraud crimes in the USA.
           - We were able to identify that there was no correlation between credit card fraud and COVID 19 measures
         
                    """)
                    
      
                