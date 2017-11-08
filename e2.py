import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
from e1 import *

#Blank array will hold the dataframes
dataframes = []


#Loop through the different files
for n in range(0,len(electionID)):
    filename = electionID[n][0]+".csv"

    #take first row of the file and transform it to a dictionary
    party_candidate = pd.read_csv(filename, nrows = 1).dropna(axis=1)
    party_candidate_dict = party_candidate.iloc[0].to_dict()

    #open the dataframe
    votes_df = pd.read_csv(filename, index_col = 0, thousands = ',', skiprows = [1])


    #Replace the first rows with names from dictionary
    votes_df.rename(inplace = True, columns = party_candidate_dict) # rename to democrat/republican
    votes_df.dropna(inplace = True, axis = 1)    # drop empty columns
    votes_df["Year"] = electionID[n][0]

    #Select only the Year, Republic, Democrat and Total Votes from the current
    #dataframe
    votes_df = votes_df[["Year","Democratic","Republican", "Total Votes Cast"]]
    votes = votes_df.head()

    #add to the dataframe array
    dataframes.append(votes)


#Concatenate the dataframes together
results = pd.concat(dataframes)

#Calculate Share of votes for each party as a share of all votes cast
results["Republican Share"] = results["Republican"]/results["Total Votes Cast"]
results["Democrat Share"] = results["Democratic"]/results["Total Votes Cast"]


print(results)
