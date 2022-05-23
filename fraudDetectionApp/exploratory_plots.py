# -*- coding: utf-8 -*-
"""
Created on Mon May 23 18:56:53 2022

@author: intern7
"""

from config import *

def plot_fraud_percentage(transaction_df):    
        
    fig = plt.figure(figsize=(1,1))
    
    fraud_mask = transaction_df["is_fraud"] == 1
    not_fraud_mask = transaction_df["is_fraud"] == 0
    
    fraud_count = transaction_df["is_fraud"][fraud_mask].count()
    legit_count = transaction_df["is_fraud"][not_fraud_mask].count()
    
    
    labels = ["Fraud", "Not Fraud"]

    fig, ax = plt.subplots()
    ax.pie([fraud_count, legit_count], labels = labels, autopct="%0.2f%%", colors = ("yellow", "gray"))
    
    explode = (0, 1)

    return st.pyplot(fig)


    

    
