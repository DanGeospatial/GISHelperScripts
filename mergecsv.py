# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 11:37:28 2022
@author: Daniel Nelson
"""

#########################
#Imports
#########################
import os
import pandas as pd

#########################
#Parameters
#########################

#set your directory and workspace
os.chdir(r'C:\Near\Total')

path = r'C:\Near\Total'

#########################
#Get CSV Files
#########################

#make sure folder only contains csv files
#or use glob.glob to only get csv
all_files = os.listdir(path)

listcsv = []

#########################
#Append Files
#########################

for csvfile in all_files:
    dataf = pd.read_csv(csvfile)
    listcsv.append(dataf)
    
bigcsv = pd.concat(listcsv)

#########################
#Export New CSV
#########################

#set your export filename
bigcsv.to_csv(path + r'\Near.csv')
