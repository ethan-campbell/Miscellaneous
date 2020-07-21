from numpy import *
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os

os.chdir('/Users/Ethan/Documents/Emi/Kohaku the cat/2020-02-26 - FIP journey plots/')

data = pd.read_excel('Kohaku weight.xlsx',header=1)
# data['Date'] = pd.DatetimeIndex(data['Date'])

plt.figure(figsize=(9,5))
plt.plot(data['Date'].values,data['Weight (lbs)'].values,c='k',lw=1,zorder=2)
plt.scatter(data['Date'].values,data['Weight (lbs)'].values,c='k',s=8,zorder=3)
plt.ylabel('Weight (lbs)')
plt.gca().axvspan(xmin=datetime(2019,12,4),xmax=datetime(2019,12,18),
                  ymin=0,ymax=1,facecolor='cornflowerblue',alpha=0.3,zorder=1,label='Shelter #1')
plt.gca().axvspan(xmin=datetime(2019,12,18),xmax=datetime(2020,1,5),
                  ymin=0,ymax=1,facecolor='goldenrod',alpha=0.3,zorder=1,label='Shelter #2')
plt.gca().axvspan(xmin=datetime(2020,1,5),xmax=datetime(2020,1,5,12,0,0),
                  ymin=0,ymax=1,facecolor='maroon',alpha=0.7,zorder=1,label='Adopted')
plt.gca().axvspan(xmin=datetime(2020,1,29),xmax=datetime(2020,4,21),
                  ymin=0,ymax=1,facecolor='0.5',alpha=0.3,zorder=1,label='On GS')
plt.xticks([datetime(2019,12,1),datetime(2020,1,1),datetime(2020,2,1),datetime(2020,3,1),datetime(2020,4,1),
            datetime(2020,5,1),datetime(2020,6,1),datetime(2020,7,1)])
plt.xlim([datetime(2019,12,1),datetime(2020,7,20)])
plt.gcf().autofmt_xdate()
plt.grid(alpha=0.5)
plt.legend(loc='lower left')
plt.title('Kohaku\'s FIP recovery')
plt.savefig('Kohaku.jpg')
plt.close()