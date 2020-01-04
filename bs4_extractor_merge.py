# -*- coding: utf-8 -*-

from data_concatenation import average_data
import requests
import sys
import pandas as pd
from bs4 import BeautifulSoup
import os
import csv


def fetch_data(month,year):
    
    file_html = open('Data/Html_data/{}/{}.html'.format(year,month),'rb')
    plain_text = file_html.read()
    
    temp_data = []
    final_data = []
    
    soup = BeautifulSoup(plain_text,'lxml')
    
    for table in soup.findAll("table",{"class":"medias mensuales numspan"}):
        for tbody in table:
            for tr in tbody:
                a = tr.get_text()
                temp_data.append(a)
    
    rows = len(temp_data)/15
    
    for times in range(round(rows)):
        new_temp_data = []
        for i in range(15):
            new_temp_data.append(temp_data[0])
            temp_data.pop(0)
            
        final_data.append(new_temp_data)
        
    length = len(final_data)
    
    final_data.pop(length - 1)
    final_data.pop(0)
    
    for a in range(len(final_data)):
        final_data[a].pop(4)
        final_data[a].pop(5)
        final_data[a].pop(12)
        final_data[a].pop(11)
        final_data[a].pop(10)
        final_data[a].pop(9)
        final_data[a].pop(8)
        final_data[a].pop(0)
#        final_data[a].pop(6)
#        final_data[a].pop(13)
#        final_data[a].pop(12)
#        final_data[a].pop(11)
#        final_data[a].pop(10)
#        final_data[a].pop(9)
#        final_data[a].pop(0)
        
        
    return final_data
   
def combine_data(year,c):
    for a in pd.read_csv("Data/Target_Data/target_"+str(year)+".csv",chunksize=c):
        df = pd.DataFrame(data=a)
        my_list = df.values.tolist()
    return my_list



if __name__ == "__main__":
    if not os.path.exists("Data/Target_Data") :
        os.makedirs("Data/Target_Data")
        
    for year in range(2013,2019):
        finalData = []
        with open("Data/Target_Data/target_"+str(year)+".csv",'w')  as csvfile:
            wr = csv.writer(csvfile,dialect='excel')
            wr.writerow(['T', 'TM', 'Tm', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
            
        for month in range(1,13):
            temp = fetch_data(month,year)
            finalData = finalData + temp
            
        pm = getattr(sys.modules[__name__],'average_data')(year)
        
        if len(pm) == 364:
            pm.insert(364,'-')
            
        for i in range(len(finalData) - 1):
            finalData[i].insert(8,pm[i])
            
        with open("Data/Target_Data/target_"+str(year)+".csv",'a',newline='')  as csvfile:
            wr = csv.writer(csvfile,dialect='excel')
            for row in finalData:
                flag = 0
                for element in row:
                    if element == "" or element == "-":
                        flag = 1
                
                if flag!= 1:
                    wr.writerow(row)
                    
    data_2013 = combine_data(2013,600)
    data_2014 = combine_data(2014,600) 
    data_2015 = combine_data(2015,600) 
    data_2016 = combine_data(2016,600)
    data_2017 = combine_data(2017,600)
    data_2018 = combine_data(2018,600)

    total =  data_2013 + data_2014 + data_2015 + data_2016 +  data_2017 +  data_2018
   
    with open("Data/Target_Data/Target_combine.csv","w") as csvfile:
        wr = csv.writer(csvfile,dialect='excel')
        wr.writerow(['T','TM','Tm','H','VV','V','VM','PM.2.5'])
       
        wr.writerows(total)
       

                     
            
            