# Data Collection
# Data Preprocessing (Feature Engineering)
#https://en.tutiempo.net/climate/03-2013/ws-421820.html

import os
import time
import requests
import sys

def fetch_page_html():
    for year in range(2013,2019):
        for month in range(1,13):
            
            if month < 10:
                url = "https://en.tutiempo.net/climate/0{}-{}/ws-432950.html".format(month,year)
                #url = "https://en.tutiempo.net/climate/0{}-{}/ws-421820.html"
                
            else:
                url = "https://en.tutiempo.net/climate/{}-{}/ws-432950.html".format(month,year)
                #url = "https://en.tutiempo.net/climate/{}-{}/ws-421820.html"
                
            
            text_source = requests.get(url)
            text_utf = text_source.text.encode("utf-8")
        
            if not os.path.exists("Data/Html_data/{}".format(year)):
                os.makedirs("Data/Html_data/{}".format(year))
            
            with open("Data/Html_data/{}/{}.html".format(year,month),"wb") as out:
                out.write(text_utf)
            
            
        sys.stdout.flush()
                
            
if __name__ == "__main__":
    
    start_time = time.time()
    fetch_page_html()
    end_time = time.time()
    print("Time taken to fetch source html {}".format(end_time - start_time))
             
        
 

