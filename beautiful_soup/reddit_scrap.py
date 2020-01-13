import requests
import csv
import time
import bs4
from bs4 import BeautifulSoup

url = "https://old.reddit.com/r/datascience/"
headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')
domains = soup.find_all('span', class_='domain')
attrs = {'class': 'thing', 'data-domain': 'self.datascience'}

counter = 1
for post in soup.find_all('div', attrs=attrs):

	title = post.find('p', class_="title").text
	author = post.find('a', class_="author").text

	comment_nbr = post.find('a', class_="comments").text.split(" ")[0]
	if comment_nbr == "comment":
		comment_nbr = 0

	likes = post.find("div", attrs={"class": "score likes"}).text
	if likes == "•":
		likes = "None"

	post_line = [counter, title, author, comment_nbr, likes]
	with open("output.csv", 'a') as f:
		writer = csv.writer(f)
		writer.writerow(post_line)
	
	counter += 1