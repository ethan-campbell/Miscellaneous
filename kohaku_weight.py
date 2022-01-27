from numpy import *
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import os

os.chdir('/Users/Ethan/Documents/Emi/Kohaku the cat/2022-01-26 - weight plots, starting with FIP journey/')

data = pd.read_excel('Kohaku weight.xlsx',header=1,index_col='Date')
# data['Date'] = pd.DatetimeIndex(data['Date'])

plt.figure(figsize=(9,5))
plt.plot(data.index,data['Weight (lbs)'].values,c='k',lw=1,zorder=2)
plt.scatter(data[:'2020-10-23'].index,data[:'2020-10-23'].values,c='k',s=8,zorder=3,
            marker='o',label='Non-renal food')
plt.scatter(data['2020-10-24':'2020-11-02'].index,data['2020-10-24':'2020-11-02'].values,c='k',s=8,zorder=3,
            marker='s',label='Mix of non-renal and renal food')
plt.scatter(data['2020-11-03':'2021-03-06'].index,data['2020-11-03':'2021-03-06'].values,c='k',s=8,zorder=3,
            marker='^',label='Renal food')
plt.scatter(data['2021-03-07':'2021-05-10'].index,data['2021-03-07':'2021-05-10'].values,c='k',s=8,zorder=3,
            marker='o')  # Non-renal food
plt.scatter(data['2021-05-11':'2021-06-24'].index,data['2021-05-11':'2021-06-24'].values,c='k',s=8,zorder=3,
            marker='s')  # Mix of non-renal and renal food
plt.scatter(data['2021-06-25':'2021-08-20'].index,data['2021-06-25':'2021-08-20'].values,c='k',s=8,zorder=3,
            marker='^')  # Renal food
plt.scatter(data['2021-08-21':'2021-09-04'].index,data['2021-08-21':'2021-09-04'].values,c='k',s=8,zorder=3,
            marker='s')  # Mix of non-renal and renal food
plt.scatter(data['2021-09-05':'2021-12-23'].index,data['2021-09-05':'2021-12-23'].values,c='k',s=8,zorder=3,
            marker='^')  # Renal food
plt.scatter(data['2021-12-24':'2022-01-03'].index,data['2021-12-24':'2022-01-03'].values,c='k',s=8,zorder=3,
            marker='s')  # Mix of non-renal and renal food
plt.scatter(data['2022-01-04':'2022-01-27'].index,data['2022-01-04':'2022-01-27'].values,c='k',s=8,zorder=3,
            marker='^')  # Renal food
plt.gca().axvspan(xmin=datetime(2019,12,4),xmax=datetime(2019,12,18),
                  ymin=0,ymax=1,facecolor='cornflowerblue',alpha=0.3,zorder=1,label='Shelter #1')
plt.gca().axvspan(xmin=datetime(2019,12,18),xmax=datetime(2020,1,5),
                  ymin=0,ymax=1,facecolor='goldenrod',alpha=0.3,zorder=1,label='Shelter #2')
plt.gca().axvspan(xmin=datetime(2020,1,5),xmax=datetime(2020,1,7),
                  ymin=0,ymax=1,facecolor='maroon',alpha=0.8,zorder=1,label='Adopted')
plt.gca().axvspan(xmin=datetime(2020,1,29),xmax=datetime(2020,4,21),
                  ymin=0,ymax=1,facecolor='brown',alpha=0.3,zorder=1,label='On GS-441524 (FIP antiviral)')
plt.gca().axvspan(xmin=datetime(2020,7,17),xmax=datetime(2020,8,1),
                  ymin=0,ymax=1,facecolor='0.5',alpha=0.2,zorder=1,label='Low-appetite period')
plt.gca().axvspan(xmin=datetime(2020,11,21),xmax=datetime(2020,12,13),
                  ymin=0,ymax=1,facecolor='0.5',alpha=0.2,zorder=1)   # Low-appetite period
plt.gca().axvspan(xmin=datetime(2021,2,18),xmax=datetime(2021,3,10),
                  ymin=0,ymax=1,facecolor='0.5',alpha=0.2,zorder=1)   # Low-appetite period
plt.gca().axvspan(xmin=datetime(2021,8,10),xmax=datetime(2021,9,4),
                  ymin=0,ymax=1,facecolor='0.5',alpha=0.2,zorder=1)   # Low-appetite period
plt.gca().axvspan(xmin=datetime(2021,11,23),xmax=datetime(2022,2,2),        # end date: to present
                  ymin=0,ymax=1,facecolor='0.5',alpha=0.2,zorder=1)   # Low-appetite period
plt.ylabel('Weight (lbs)')
plt.ylim([8,None])
plt.xlim([datetime(2019,12,1),datetime(2022,2,1)])
plt.gcf().autofmt_xdate()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.grid(lw=0.5,alpha=0.3)
plt.legend(frameon=False,loc='lower right')
plt.title('Kohaku\'s weight, food, and appetite from adoption onwards')
plt.savefig('2022-01-26 - Kohaku.jpg',dpi=450)
plt.close()