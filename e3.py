import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver

#import data and structures from last two questions
from e1 import *
from e2 import *

#Create bar charts for Accomack County, Alexandria City, Alleghany County, Amelia County


################################################################################
#Accomack County Plot
################################################################################
accomack_county_df = results[results.index == "Accomack County"]
accomack_bar = accomack_county_df.plot.bar(x = "Year", y=["Republican Share", "Democrat Share"])
accomack_bar.set_ylabel("Percent of Votes")
accomack_bar.set_ylim([0,1])
accomack_bar.set_yticklabels(['{:3.2f}%'.format(x*100) for x in accomack_bar.get_yticks()] )
plt.title("Accomack County Share of Votes")
accomack_bar.figure.savefig("Accomack County.pdf")
plt.show()


################################################################################
#Alexandria City Plot
################################################################################
Alexandria_df = results[results.index == "Alexandria City"]
Alexandria_bar = Alexandria_df.plot.bar(x = "Year", y=["Republican Share", "Democrat Share"])
Alexandria_bar.set_ylabel("Percent of Votes")
Alexandria_bar.set_ylim([0,1])
Alexandria_bar.set_yticklabels(['{:3.2f}%'.format(x*100) for x in Alexandria_bar.get_yticks()])
plt.title("Alexandria City Share of Votes")
Alexandria_bar.figure.savefig("Alexandria City.pdf")
plt.show()



################################################################################
#Alleghany County Plot
################################################################################
Alleghany = results[results.index == "Alleghany County"]
Alleghany_bar = Alleghany.plot.bar(x = "Year", y=["Republican Share", "Democrat Share"])
Alleghany_bar.set_ylabel("Percent of Votes")
Alleghany_bar.set_ylim([0,1])
Alleghany_bar.set_yticklabels(['{:3.2f}%'.format(x*100) for x in Alleghany_bar.get_yticks()] )
plt.title("Alleghany County Share of Votes")
Alleghany_bar.figure.savefig("Alleghany County.pdf")
plt.show()

################################################################################
#Amelia County Plot
################################################################################
Amelia = results[results.index == "Amelia County"]
Amelia_bar = Amelia.plot.bar(x = "Year", y=["Republican Share", "Democrat Share"])
Amelia_bar.set_ylabel("Percent of Votes")
Amelia_bar.set_ylim([0,1])
Amelia_bar.set_yticklabels(['{:3.2f}%'.format(x*100) for x in Amelia_bar.get_yticks()] )
plt.title("Amelia County Share of Votes")
Amelia_bar.figure.savefig("Amelia County.pdf")
plt.show()
