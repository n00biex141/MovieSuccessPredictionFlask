from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

#url = 'https://www.imdb.com/list/ls066672023/'
url = 'https://www.imdb.com/list/ls021545925/'
#url = 'https://www.imdb.com/list/ls041664436/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
first = []
second = []
first_names = []
first_years = []
first_genres = []
first_rates = []
language = []
first_gros = []
first_directors = []
first_casts = []
year_list = []
verdict = []
hit_flop = []
worldwide_gross_in_crore = []
votes = []
movie_containers = soup.find_all('div', class_ = 'lister-item mode-detail')
for first_movie in movie_containers: 
    first = first_movie.findAll("p",{"class":"text-muted text-small"})
    second = first[1]
    first_director = second.a.text
    first_directors.append(first_director)
    
for first_movie in movie_containers: 
    """first_name = first_movie.h3.a.text"""
    first_name = first_movie.img["alt"] 
    first_names.append(first_name)

for first_movie in movie_containers: 
    first_scrape = first_movie.findAll("p",{"class":"text-muted text-small"})
    second_scrape = first_scrape[1]
    a_num=second_scrape.findAll("a")
    final_lis = []
    lis = []
    for x in range(len(a_num)):
        sec=a_num[x].text
        lis.append(sec)
    final_lis = lis[1:]
    first_casts.append(final_lis)

for first_movie in movie_containers: 
    first_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold').text
    year_list.append(first_year)
for elem in year_list:
    elem = elem[elem.find("2"):]
    elem = elem[:-1]
    elem = int(elem)
    first_years.append(elem)
    
"""for first_movie in movie_containers: 
    first_genre = first_movie.p.find('span', class_='genre').text
    first_genres.append(first_genre)
    first_genres = [item.strip() for item in first_genres if str(item)] 
    
for item in first_genres:
    my_list = item.split(",")"""

first_genres1 = []
for first_movie in movie_containers:
    first_genre = first_movie.p.find('span', class_='genre').text
    first_genres1.append(first_genre)
    first_genres1 = [item.strip() for item in first_genres1 if str(item)]   
for item in first_genres1:
    my_list = item.split(",")
    first_genres.append(my_list)

my_item = ['Action', 'Thriller', 'Biography', 'Drama', 'History', 'Romance','Comedy', 'Crime', 'Adventure', 'Horror', 'Sport', 'Fantacy', 'War']
for item in my_item:
    vars()[item] = []
for item in my_item:
    for i in first_genres:
        if item in i or " "+item in i:
            vars()[item].append(1)
        else:
            vars()[item].append(0)

SciFi = []
for i in first_genres:
    if 'Sci-Fi' in i or ' Sci-Fi' in i:
        SciFi.append(1)
    else:
        SciFi.append(0)
    
    
for first_movie in movie_containers: 
    first_rate = first_movie.find('div', class_='ipl-rating-star small')

    first_rate = float(first_rate.find('span', class_='ipl-rating-star__rating').text)
    first_rates.append(first_rate)

for first_movie in movie_containers: 
    first_gross = first_movie.find('div', class_='list-description').get_text(separator='\n')
    first_gros.append(first_gross)

for elem in first_gros:
    elem = elem[elem.find(":")+2:]
    elem = elem[:elem.find("\n")]
    language.append(elem)
    
for elem in first_gros:
    elem = elem[elem.find("G")+8:]
    elem = elem[:elem.find("cr")]
    worldwide_gross_in_crore.append(elem)
worldwide_gross_in_crore = list(map(float, worldwide_gross_in_crore))

for elem in first_gros:
    elem = elem[elem.find("Verdict : ")+10:]
    if(elem[-1:]==' '):
        elem = elem[:-1]
    if(elem[-2:]=='\n'):
        elem = elem[:-2]
    verdict.append(elem)

for elem in verdict:
    if "Blockbuster" in elem or "Hit" in elem:
        hit_flop.append(1)
    else:
        hit_flop.append(0)

ls1 = []
ls2 = []
for first_movie in movie_containers: 
    ls1 = first_movie.findAll("span",{"name":"nv"})
    ls2 = ls1[0]
    vote = int(ls2.text.replace(",", ""))
    votes.append(vote)
    

final_dataset = pd.DataFrame({'Movie Names' : first_names,
                     'Directors' : first_directors,
                     'Cast' : first_casts,
                     'Language' : language,
                     'Verdict' : verdict,
                     'Year of Release' : first_years,
                     'Action' : Action,  
                     'Thriller' : Thriller, 
                     'SciFi' : SciFi,
                     'Biography' : Biography, 
                     'Drama' : Drama, 
                     'History' : History, 
                     'Romance' : Romance,
                     'Comedy' : Comedy, 
                     'Crime' : Crime, 
                     'Adventure' : Adventure, 
                     'Horror' : Horror, 
                     'Sport' : Sport, 
                     'Fantacy': Fantacy,
                     'War' : War,
                     'Ratings' : first_rates,
                     'Votes' : votes,
                     'Worldwide Gross in Crores' : worldwide_gross_in_crore,
                     'Hit or Flop' : hit_flop})

print(final_dataset)

#export_csv = final_dataset.to_csv ('DatasetToCsv.csv', index = None, header=True)

with open('DatasetToCsv.csv', 'a') as f:
    final_dataset.to_csv(f, index=None, header=False)
