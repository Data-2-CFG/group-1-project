# -*- coding: utf-8 -*-
"""
Created on Sun May 22 01:37:56 2022

@author: intern7
"""

import pandas as pd
import numpy as np
import streamlit as st
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import metrics 
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from streamlit_option_menu import option_menu