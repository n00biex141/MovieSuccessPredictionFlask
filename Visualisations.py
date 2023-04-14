import matplotlib
import matplotlib.pyplot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

imdbdata=pd.read_csv('DatasetToCsv.csv', encoding="ISO-8859-1")

from os import path
import matplotlib.pyplot as plt
import random

#DIRECTOR ANALYSIS :
imdbdata.Directors.value_counts()[:10].plot.pie(autopct='%1.1f%%',figsize=(10,10))
plt.title('TOP 10 DIRECTORS OF MOVIES')
plt.show()

#ACTOR ANALYSIS
imdbdata.Cast.value_counts()[:10].plot.pie(autopct='%1.1f%%',figsize=(10,10))
plt.title('TOP 10 Actors OF MOVIES')
plt.show()

#YEAR ANALYSIS :
sns.stripplot(x="Year of Release", y="Ratings", data=imdbdata, jitter=True);
print(' RATING BASED ON YEAR')
plt.show

sns.swarmplot(x="Year of Release", y="Votes", data=imdbdata);
print(' VOTES BASED ON YEAR')
#VOTES BASED ON YEAR
sns.stripplot(x="Year of Release", y="Worldwide Gross in Crores", data=imdbdata, jitter=True);
print(' REVENUE BASED ON YEAR')

#RATING ANALYSIS :

imdbdata["Ratings"].value_counts()

#top 10 rating movies 
Sortedrating= imdbdata.sort_values(['Ratings'], ascending=False)

#medium rated movies
mediumratedmovies= imdbdata.query('(Ratings > 3.0) & (Ratings < 7.0)')

#('(MOVIES WITH MEDIUM RATING , VOTES')
sns.jointplot(x="Ratings", y="Votes", data=mediumratedmovies);

#('(MOVIES WITH MEDIUM RATING , REVENUE')
sns.jointplot(x="Ratings", y="Worldwide Gross in Crores", data=mediumratedmovies);

highratedmovies= imdbdata.query('(Ratings > 7.0) & (Ratings < 10.0)')

#('(MOVIES WITH HIGH RATING ,VOTES')
sns.jointplot(x="Ratings", y="Votes", data=highratedmovies);

#('(MOVIES WITH HIGH RATING ,REVENUE')
sns.jointplot(x="Ratings", y="Worldwide Gross in Crores", data=highratedmovies);

plt.show()



