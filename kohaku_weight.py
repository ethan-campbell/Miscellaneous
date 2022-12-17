from numpy import *
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import os

os.chdir('/Users/Ethan/Documents/Emi/Kohaku the cat/2022-11-24 - weight plots (RUNNING FOLDER)/')

data = pd.read_excel('Kohaku weight.xlsx',header=1,index_col='Date')
episodes = pd.read_excel('Asthma attacks and vomit episodes.xlsx',header=1,index_col='Date')

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
plt.scatter(data['2022-01-04':'2022-10-17'].index,data['2022-01-04':'2022-10-17'].values,c='k',s=8,zorder=3,
            marker='^')  # Renal food
plt.scatter(data['2022-10-18':'2022-11-03'].index,data['2022-10-18':'2022-11-03'].values,c='k',s=8,zorder=3,
            marker='s')  # Mix of non-renal and renal food
plt.scatter(data['2022-11-03':'2022-11-25'].index,data['2022-11-03':'2022-11-25'].values,c='k',s=8,zorder=3,
            marker='^')  # Renal food

plt.gca().axvspan(xmin=datetime(2019,12,4),xmax=datetime(2019,12,18),
                  ymin=0,ymax=1,facecolor='cornflowerblue',alpha=0.3,zorder=1,label='Shelter #1')
plt.gca().axvspan(xmin=datetime(2019,12,18),xmax=datetime(2020,1,5),
                  ymin=0,ymax=1,facecolor='goldenrod',alpha=0.3,zorder=1,label='Shelter #2')
plt.gca().axvspan(xmin=datetime(2020,1,5),xmax=datetime(2020,1,7),
                  ymin=0,ymax=1,facecolor='maroon',alpha=0.8,zorder=1,label='Adopted')
plt.gca().axvspan(xmin=datetime(2020,7,17),xmax=datetime(2020,8,1),
                  ymin=0,ymax=1,facecolor='0.5',alpha=0.2,zorder=1,label='Low-appetite period')
plt.gca().axvspan(xmin=datetime(2020,11,21),xmax=datetime(2020,12,13),
                  ymin=0,ymax=1,facecolor='0.5',alpha=0.2,zorder=1)   # Low-appetite period
plt.gca().axvspan(xmin=datetime(2021,2,18),xmax=datetime(2021,3,10),
                  ymin=0,ymax=1,facecolor='0.5',alpha=0.2,zorder=1)   # Low-appetite period
plt.gca().axvspan(xmin=datetime(2021,8,10),xmax=datetime(2021,9,4),
                  ymin=0,ymax=1,facecolor='0.5',alpha=0.2,zorder=1)   # Low-appetite period
plt.gca().axvspan(xmin=datetime(2021,11,23),xmax=datetime(2022,1,29),
                  ymin=0,ymax=1,facecolor='0.5',alpha=0.2,zorder=1)   # Low-appetite period
plt.gca().axvspan(xmin=datetime(2022,5,26),xmax=datetime(2022,11,25),        # end date: to present
                  ymin=0,ymax=1,facecolor='0.5',alpha=0.2,zorder=1)   # Low-appetite period

plt.gca().axvspan(xmin=datetime(2020,1,29),xmax=datetime(2020,4,21),
                  ymin=0,ymax=1,facecolor='brown',alpha=0.2,zorder=1)
plt.text(datetime(2020,1,29)+(datetime(2020,4,21)-datetime(2020,1,29))/2,11.2,
         'GS-441524\n(FIP antiviral)',ha='center',va='center',fontsize='xx-small')
plt.fill_between([datetime(2022,1,28),datetime(2022,8,29)],[10.4,10.4],[10.7,10.7],
                  color='forestgreen',edgecolor=None,alpha=0.2,zorder=2)
plt.fill_between([datetime(2022,8,30),datetime(2022,10,15)],[10.4,10.4],[10.7,10.7],
                 color='brown',edgecolor=None,alpha=0.2,zorder=2)
plt.fill_between([datetime(2022,10,16),datetime(2022,11,25)],[10.4,10.4],[10.7,10.7],
                 color='brown',edgecolor=None,alpha=0.35,zorder=2)     # to present
plt.text(datetime(2022,1,28) + timedelta(days=16),10.55,
         'Cyproheptadine 1 mg q48h',ha='left',va='center',fontsize='xx-small')
plt.text(datetime(2022,8,30) + timedelta(days=4),10.85,
         'Mirtazapine\n1.875 mg',ha='left',va='center',fontsize='xx-small')
plt.text(datetime(2022,8,30) + timedelta(days=4),10.55,
         'q48h',ha='left',va='center',fontsize='xx-small')
plt.text(datetime(2022,10,16) + timedelta(days=4),10.55,
         'q24h',ha='left',va='center',fontsize='xx-small')
plt.fill_between([datetime(2021,3,9),datetime(2022,10,15)],[10.0,10.0],[10.3,10.3],
                  color='rebeccapurple',edgecolor=None,alpha=0.2,zorder=2)
plt.fill_between([datetime(2022,10,16),datetime(2022,11,25)],[10.0,10.0],[10.3,10.3],
                  color='rebeccapurple',edgecolor=None,alpha=0.35,zorder=2)    # to present
plt.text(datetime(2021,3,9) + timedelta(days=16),10.15,
         'Famotidine 2.5 mg q48h',ha='left',va='center',fontsize='xx-small')
plt.text(datetime(2022,10,16) + timedelta(days=4),10.15,
         'q24h',ha='left',va='center',fontsize='xx-small')
plt.text(datetime(2021,1,9) + timedelta(days=4),9.72,
         'Fluticasone inhaler (q12h):',ha='left',va='bottom',fontsize='xx-small')
plt.fill_between([datetime(2021,1,9),datetime(2021,2,1)],[9.4,9.4],[9.7,9.7],
                  color='lightcyan',edgecolor=None,alpha=0.5,zorder=2)
plt.text(datetime(2021,1,9) + timedelta(days=4),9.55,
         '50\nmcg',ha='left',va='center',fontsize='xx-small')
plt.fill_between([datetime(2021,2,2),datetime(2021,4,8)],[9.4,9.4],[9.7,9.7],
                  color='paleturquoise',edgecolor=None,alpha=0.4,zorder=2)
plt.text(datetime(2021,2,2) + timedelta(days=15),9.55,
         '125\nmcg',ha='left',va='center',fontsize='xx-small')
plt.fill_between([datetime(2021,4,8),datetime(2022,1,2)],[9.4,9.4],[9.7,9.7],
                  color='turquoise',edgecolor=None,alpha=0.4,zorder=2)
plt.text(datetime(2021,4,8) + timedelta(days=4),9.55,
         '250\nmcg',ha='left',va='center',fontsize='xx-small')
plt.fill_between([datetime(2022,1,2),datetime(2022,1,11)],[9.4,9.4],[9.7,9.7],
                  color='mediumturquoise',edgecolor=None,alpha=0.4,zorder=2)
# plt.text(datetime(2022,1,2) + timedelta(days=4),9.55,
#          '375 mcg q12h',ha='left',va='center',fontsize='xx-small')
plt.fill_between([datetime(2022,1,12),datetime(2022,1,25)],[9.4,9.4],[9.7,9.7],
                  color='darkturquoise',edgecolor=None,alpha=0.4,zorder=2)
plt.text(datetime(2022,1,12) + timedelta(days=4),9.55,
         '500\nmcg',ha='left',va='center',fontsize='xx-small')
plt.fill_between([datetime(2022,1,26),datetime(2022,11,25)],[9.4,9.4],[9.7,9.7],
                  color='mediumturquoise',edgecolor=None,alpha=0.4,zorder=2)     # to present
plt.text(datetime(2022,1,26) + timedelta(days=20),9.55,
         '375\nmcg',ha='left',va='center',fontsize='xx-small')

asthma_attack_dates = episodes['Asthma attack (True/False)'].dropna().index
vomit_dates = episodes['Vomit (True/False)'].dropna().index
plt.scatter(asthma_attack_dates,tile(9.1,len(asthma_attack_dates)),
            marker='*',c='k',s=15,edgecolors='none')
plt.scatter(vomit_dates,tile(9.2,len(vomit_dates)),
            marker='o',c='k',s=8,edgecolors='none')
plt.text(min(vomit_dates) - timedelta(days=3),9.30,
         'Vomit episodes (•) and\nasthma attacks (★):',ha='left',va='bottom',fontsize='xx-small')

plt.ylabel('Weight (lbs)',fontsize='small')
plt.ylim([8,None])
plt.gca().tick_params(axis='y',labelsize='small')
plt.xlim([datetime(2019,12,1),datetime(2022,11,30)])
plt.gcf().autofmt_xdate()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(fontsize='small')
plt.grid(lw=0.5,alpha=0.3)
plt.legend(frameon=False,loc='lower right',fontsize='x-small',ncol=2)
plt.title('Kohaku\'s health and medications from adoption onwards',fontsize='medium')
plt.savefig('2022-11-24 - Kohaku.jpg',dpi=450)
plt.close()