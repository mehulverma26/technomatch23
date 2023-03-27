"""API Version of the data"""
# import urllib.request
# import sys

# import csv
# import codecs
# try: 
#   ResultBytes = urllib.request.urlopen("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/delhi?unitGroup=metric&include=days&key=6NP2VX8V52NB7R9VEVVYXA3CE&contentType=csv")
  
#   # Parse the results as CSV
#   CSVText = csv.reader(codecs.iterdecode(ResultBytes, 'utf-8'))
        
# except urllib.error.HTTPError  as e:
#   ErrorInfo= e.read().decode() 
#   print('Error code: ', e.code, ErrorInfo)
#   sys.exit()
# except  urllib.error.URLError as e:
#   ErrorInfo= e.read().decode() 
#   print('Error code: ', e.code,ErrorInfo)
#   sys.exit()
"""csv checking"""
# import pandas as pd
# data=pd.read_csv("z.csv")
# print(data)