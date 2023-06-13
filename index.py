import streamlit as st


import pickle
import requests

#===========================================
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

import csv
import logging

import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

import time
import os

import boto3
import logging
import requests
from boto3 import resources

import requests
from io import StringIO
import logging





import streamlit_pandas as sp


st.cache(allow_output_mutation = True)


def load_data():
    
    
    d = os.getcwd()

    fname = os.path.join(d,'geckodriver.exe')

    # Load driver
    driver=webdriver.Firefox(executable_path=fname)

    driver.maximize_window()
    logging.info('Firefox webdriver loaded')

    driver.get('https://www.flipkart.com/') 
    #driver.get('http://www.censusindia.gov.in/')
    driver.implicitly_wait(5)

    # Click close add 
    driver.find_element(By.XPATH,"//button[contains(@class,'_2KpZ6l _2doB4z')]").click()
    driver.implicitly_wait(5)
    # Enter search item in search box
    driver.find_element(By.XPATH,"//input[contains(@class,'_3704LK')]").send_keys('samsung mobile phone ')
    driver.implicitly_wait(5)
    # Click search button
    driver.find_element(By.XPATH,"//button[contains(@class,'L0Z3Pu')]").click()
    driver.implicitly_wait(5)


    names = []
    prices = []

    name = driver.find_elements(By.XPATH,"//div[contains(@class,'_4rR01T')]")
    price = driver.find_elements(By.XPATH,"//div[contains(@class,'_30jeq3 _1_WHN1')]")
    time.sleep(3)
    for i in name:
        names.append(i.text)

    for i in price:
        prices.append(i.text)
    time.sleep(3)    
    print('Step_1 Complete')

    driver.quit()



    #--------------------------------------
    # Testing
    print('\n')
    print('len_names' , len(names))
    print('len_prices',len(prices))
    print('\n')
    #----------------------------------------
    
    
    a = []
    b = []
    for i in names:
        try:
            a.append(i.split('(')[0])
        except:
            a.append(i)

    for i in prices:
        try:
            j = i.split('₹')[1]
            j = j.replace(',','')
            j = int(j)
            print(j,type(j))
            b.append(j)  
        except:
            pass

    # Calling DataFrame constructor on list
    df = pd.DataFrame({'Phone_Name':a,'Price':b})

    return (df)

if st.button("Satrt") :

    df1 = load_data()
    st.write(df1)





    #1. We 1st create a function load_data() for seleniun to run
    #2. and WebScrap data for Flipkart and return a dataframe


# ===========================================
    







    
             
             
             
