
import pandas as pd 
import matplotlib.pyplot as plt 

#import datafile
data=pd.read_csv('file.csv')

#filter cities
#if need to filter other cities just include name of that city and others aswell
data_ =data.loc[((data['Viewer Hometown'] == 'Pittsburgh') | (data['Viewer Hometown'] == 'Cleveland')) ]

 
# change sum to mean if average nunber of view needed to  be plotted
 
temp=pd.DataFrame(data.groupby(data['Program Genre'])['Number of Viewers'].sum()) 
ax = plt.subplot(111)
ax.bar(temp.index,temp.iloc[:,0],width=0.3,  color='b', align='center')
plt.xlabel('Genres')
plt.title('Total Number of Viewers from Pittsburgh or Cleveland')
plt.show()


