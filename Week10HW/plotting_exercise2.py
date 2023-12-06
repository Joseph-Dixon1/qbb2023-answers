#!/usr/bin/env python3

import numpy as np
import pandas as pd
from pydeseq2 import preprocessing
from matplotlib import pyplot as plt

taylor_album_songs =pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-10-17/taylor_album_songs.csv')
taylor_all_songs =pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-10-17/taylor_all_songs.csv')
taylor_albums =pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-10-17/taylor_albums.csv')

print(taylor_album_songs)

#2.2
# Graph acoustic score against albums 
print(taylor_album_songs.columns)
print(taylor_album_songs['album_name'].unique())
debut=taylor_album_songs.loc[taylor_album_songs['album_name'] == 'Taylor Swift', 'acousticness']
speaknow=taylor_album_songs.loc[taylor_album_songs['album_name'] == 'Speak Now', 'acousticness']
nineteeneightynine=taylor_album_songs.loc[taylor_album_songs['album_name'] == '1989', 'acousticness']
reputation=taylor_album_songs.loc[taylor_album_songs['album_name'] == 'reputation', 'acousticness']
lover=taylor_album_songs.loc[taylor_album_songs['album_name'] == 'Lover', 'acousticness']
folklore=taylor_album_songs.loc[taylor_album_songs['album_name'] == 'folklore', 'acousticness']
evermore=taylor_album_songs.loc[taylor_album_songs['album_name'] == 'evermore', 'acousticness']
fearless_tv=taylor_album_songs.loc[taylor_album_songs['album_name'] == "Fearless (Taylor's Version)" , 'acousticness']
red_tv=taylor_album_songs.loc[taylor_album_songs['album_name'] == "Red (Taylor's Version)", 'acousticness']
midnights=taylor_album_songs.loc[taylor_album_songs['album_name'] == 'Midnights', 'acousticness']

blondie=[debut,fearless_tv,speaknow,red_tv,nineteeneightynine,reputation,lover,folklore,evermore,midnights]

blondie_median=[]


for swifties in blondie: 
	blondie_median.append(swifties.median())



plt.figure(figsize=(40, 6))
plt.scatter(x=taylor_album_songs['album_name'].unique(), y=blondie_median)
plt.xlabel('Taylors Many Albums')
plt.ylabel('How Guitar-y ( Acousticness) she was i.e. Country Taylor')
plt.title(f'Taylor Swift Acoustic Score as her albums progressed')
plt.show()

# Histogram of Keys 

plt.figure(figsize=(40, 6))
plt.hist(x=taylor_album_songs.loc[:,'key_name'].astype(str))
plt.xlabel('Keys')
plt.ylabel('Number of Appearances of Key')
plt.title(f'Taylor Swift Choice of Keys')
plt.show()


# Number of explicit not explicit songs 

explicit=taylor_album_songs.loc[taylor_album_songs['explicit'] == True]
not_explicit=taylor_album_songs.loc[taylor_album_songs['explicit'] == False]

explicit=explicit.shape[0]
not_explicit=not_explicit.shape[0]

plt.figure(figsize=(40, 6))
plt.bar(x=['Explicit','Clean'], height=[explicit,not_explicit])
plt.xlabel('Cleanliness')
plt.ylabel('Number of Songs')
plt.title(f'Number of Taylor Swift Songs She Swears In')
plt.show()