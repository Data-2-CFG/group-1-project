# -*- coding: utf-8 -*-
"""
Created on Mon May 23 14:09:34 2022

@author: intern7
"""

from config import *

def covid_plot_stringency(USACovid2020_data, USACovid2021_data):
    
    Covid2020Dates = USACovid2020_data['date_value']
    Covid2021Dates = USACovid2021_data['date_value']
    
    stringencyValue2020 = USACovid2020_data['stringency_actual']
    stringencyValue2021 = USACovid2021_data['stringency_actual']

    fig = plt.figure(figsize= [20, 12], linewidth = 2 ) 
    fig.supxlabel('Dates', fontsize = 20)
    fig.supylabel('Stringency Actual Values', fontsize = 20)

    graph1 = plt.subplot(121)
    plt.plot(Covid2020Dates, stringencyValue2020, linestyle = 'dashed', linewidth = 5, color = 'salmon')
    plt.title('02-02-2020 to 31-12-2020', fontsize = 20, pad = 10, fontweight = 'bold', color = 'salmon')
    plt.xlabel('Graph 1, Figure 1', fontsize = 15, fontweight = 'bold', color = 'salmon', loc= 'right')
    
    graph2 = plt.subplot(122, sharey=graph1)
    plt.plot(Covid2021Dates, stringencyValue2021, linestyle = 'dashed', linewidth = 5, color = 'orangered')
    plt.title('01-01-2021 to 31-12-2021', fontsize = 20, pad = 10, fontweight = 'bold', color = 'orangered')
    plt.xlabel('Graph 2, Figure 1', fontsize = 15, fontweight = 'bold', color = 'orangered', loc = 'right')
    
    return st.pyplot(fig)

def covid_plot_stringency_fraud(covidVtransGraphDF2):
    
    #Setting the y values
    stringeActualGraph = covidVtransGraphDF2['stringency_actual']
    isFraud2019Graph = covidVtransGraphDF2['is_fraud_2019']
    isFraud2020Graph = covidVtransGraphDF2['is_fraud_2020']
    
    #setting the x values
    pcDates = covidVtransGraphDF2['Month']
    
    #figure settings
    fig = plt.figure(figsize= [30, 20], linewidth = 2) 
    
    #plotting the lines
    plt.plot(pcDates, 
             isFraud2019Graph, 
             linestyle = 'dashed', 
             linewidth = 5,
             color = 'dodgerblue', 
             label = 'Fraudulent Trans 2019')
    plt.plot(pcDates, 
             isFraud2020Graph, 
             linestyle = 'dashed', 
             linewidth = 5,
             color = 'skyblue', 
             label = 'Fraudulent Trans 2020')
    plt.plot(pcDates, 
             stringeActualGraph, 
             linestyle = 'dashed', 
             linewidth = 5,
             color = 'orangered', 
             label = 'Stringency Actual 2020')
    
    #labels, titles and texts
    plt.title('Figure 4', loc = 'right', fontsize = 20, fontweight='bold', pad = 30)
    plt.xlabel('Months', fontsize = 20, fontweight='bold', labelpad = 30)
    plt.ylabel('Percentage Change', fontsize = 20, fontweight='bold', labelpad = 30)
    plt.xticks([2,3,4,5,6,7,8,9,10, 11, 12], 
               ['Jan-Feb', 'Feb-Mar', 'Mar-Apr', 'Apr-May', 'May-Jun', 'Jun-Jul', 'Jul-Aug','Aug-Sept', 'Sept-Oct', 'Oct-Nov','Nov-Dec'],
               fontsize = 15, fontweight='bold')
    plt.yticks(fontsize = 15, fontweight='bold')
    
    plt.legend(fontsize = 20)
    
    return st.pyplot(fig)