# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 00:01:29 2021

@author: Laura
"""
#import usefull libraries
import matplotlib.pyplot as plt #for plots
import pandas as pd #for dataframes
import tkinter as tk #for dialog box
from tkinter import filedialog

#open dialog box to  select file
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
input('hit any key to exit console')

#open any document of your choice
doc = pd.read_csv(file_path, skiprows=8)

#to filter the data for altitude to only plot what we want
collect = doc[doc['CPUt_st'].str.contains("COLLECT")]
doc_length = len(doc)
collect_length = len(collect)
collect_start = doc_length - collect_length

#altitude vs time
time= pd.DataFrame(doc, columns=['CPUt_cv'])
altitude= pd.DataFrame(doc, columns=['AOG_cv'])
plt.figure(1)
plt.subplot(2,1,1)
plt.grid()
plt.title('Altitude vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Altitude (m)')
plt.plot(time, altitude, 'r+')
plt.xlim([collect_start, 2000])    
plt.savefig('fig1')
      
#compare a plot of aog_cv vs aog_av
plt.figure(1)
plt.tight_layout(pad = 3.0)
plt.subplot(2,1,2)
altitude_av= pd.DataFrame(doc,columns=['AOG_av'])
plt.plot(time, altitude_av,'b*',time, altitude, 'r+')
plt.legend(('AOG_av','AOG_cv')) #find an easier way so you don't repeat
plt.xlim([collect_start, 2000])   
plt.title('Altitude (current & average) vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Altitude (m)')
plt.grid()

#temperature vs altitude 
temp = pd.DataFrame(doc, columns=['Th_cv'])
plt.figure(11)
plt.grid()
plt.plot(altitude,temp)
plt.title('Temperature vs Altitude')
plt.xlabel('Altitude (m)')
plt.ylabel('Temp (*C)')
plt.savefig('fig11')

#compare accellerometer data 
plt.figure(111)
ax_av = pd.DataFrame(doc, columns=['Ax_av'])
ay_av = pd.DataFrame(doc, columns=['Ay_av'])
az_av = pd.DataFrame(doc, columns=['Az_av'])
plt.plot(time, ax_av,time, ay_av,time, az_av)
plt.grid()
plt.xlim([0, 2250])  
plt.title('Time vs Accelleration')
plt.xlabel('Time (s)')
plt.ylabel('Accelleration (m/s^2)')
plt.legend(('Ax_av','Ay_av','Az_av'))

#barometric pressure vs time
plt.figure(1111)
pressure = pd.DataFrame(doc, columns=['P_av'] )
plt.plot(time, pressure, 'b+')
plt.xlim([0, 2250])   
plt.grid()
plt.title('Time vs Barometric pressure')
plt.xlabel('Time (s)')
plt.ylabel('Pressure (hPa')
plt.savefig('fig1111')

#slice out the of data into different parts: 
#1) main plot 
#2) slice from tmin to tmax and 
#3) alt vs temp linear 
plt.figure(11111)
plt.subplot(3,1,1)
plt.plot(time, altitude,'r')
plt.grid()
plt.title('Time vs Altitude')
plt.xlabel('Time (s)')
plt.ylabel('Altitude (m)')

plt.figure(11111)
plt.subplot(3,1,2)
t_min = int(input("enter a value for t_min: "))
t_max = int(input("enter a value for t_max: "))
plt.plot(time, altitude,'k')
plt.xlim([t_min, t_max])
plt.title('Time vs Altitude (t_min to t_max)')
plt.xlabel('Time (s)')
plt.ylabel('Altitude (m)')
plt.grid()

plt.figure(11111)
plt.subplot(3,1,3)
filterState = (doc['CPUt_av'] > t_min) & (doc['CPUt_av'] < t_max)
docFiltered = doc[filterState]
plt.plot(docFiltered['Th_cv'],docFiltered['AOG_av'],'m+')
plt.grid()
plt.title('Altitude vs Temp')
plt.xlabel('Temp (*C)')
plt.ylabel('Altitude (m)')
plt.tight_layout(pad = 1.0)
plt.savefig('fig11111')

print(docFiltered[["Th_cv","AOG_cv"]].describe())

close_all = input('do you want to close all figures?: ')
if close_all ==  'yes':
    plt.close('all')
    
 #prints statistics for specified column
#how to get the statistics for multiple columns??

# TO-DO:
#apply filterstate for t vs alt w tmin & tmax 
#comment more 
#change t_min and t_max so they can be changed w/o a restart (possibly a while loop) 
#make t_max and t_min input more user-friendly 
#drop down box for creating unanticipated plots 
#make github/dropbox