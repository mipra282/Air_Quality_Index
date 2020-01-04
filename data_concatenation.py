# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:38:03 2019

@author: Mithilesh
"""

import pandas as pd
import matplotlib.pyplot as plt

def average_data(year):
    temp_i = 0
    average = []
    for rows in pd.read_csv("Data/AQI/aqi{}.csv".format(year),chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        
        for i in data:
            
            if type(i) is float or type(i) is int:
                add_var = add_var + i 
                
            elif type(i) is str:
                if i!="NoData" and i!="PwrFail" and i!="---" and i!="InVld":
                    temp = float(i)
                    add_var = add_var + temp
                    
        avg = add_var/24
        temp_i = temp_i + 1
        
        average.append(avg)
        
    return average
                
if __name__ == "__main__":
    
    list2013 = average_data(2013)
    list2014 = average_data(2014)
    list2015 = average_data(2015)
    list2016 = average_data(2016)
    list2017 = average_data(2017)
    list2018 = average_data(2018)
    
    plt.plot(range(0,365),list2013,label="Data for 2013")
    plt.plot(range(0,364),list2014,label="Data for 2014")
    plt.plot(range(0,365),list2015,label="Data for 2015")
    plt.show()
    
        
    
    
    