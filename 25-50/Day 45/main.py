from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
responce = requests.get(url)
html_content = responce.text 
soup = BeautifulSoup(html_content, 'html.parser')
title = soup.title.string


movies_titles = soup.findAll('h3', class_='title')
movies_list = []

for movie in movies_titles : 
    movie_name = movie.get_text(strip=True)
    movies_list.append(movie_name)

movies_list.reverse()
string = "\n".join(movies_list)

with open('The100GreatestMovies.txt', 'w', encoding='utf-8') as output:
    output.write(title)
    output.write(string)