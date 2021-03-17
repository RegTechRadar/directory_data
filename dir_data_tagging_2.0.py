# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:05:35 2020

@author: jackw

Tagging algo for directory data
"""

import pandas as pd
import csv

# function for list --> string
def listToString(s):
    str1 = " "
    return(str1.join(s))
    

# Read in tag data using pandas dataframe 

tags = pd.read_csv('.csv', squeeze='true')
tags = tags.tolist()

#Initilize tag data variable

tag_data = []

# Use csv module to open sample data file

with open('.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # Loop over rows in csv which correspond to products
    for row in csv_reader:
        row = listToString(row)
        # Change case as algo is case-sensitive
        row = row.lower()
        # Create variable for storing tags per row (product)
        x = []
        # Loop over each tag within the tags list
        for tag in tags:
            # If the tag is matched within the row, add tag to x variable
            if tag in row:
                x.append(tag)
        # Append matched tags to tag_data variable with index corresponding to the product row
        x = ', '.join(x)
        tag_data.append(x)
    
        
# Turn into dataframe for easy csv output
df = pd.DataFrame(tag_data)
df.to_csv('.csv')
        
        
        