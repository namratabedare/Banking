import urllib3
import re
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

url = "https://login.yahoo.com/"

links=[]
website = requests.get(url)
website_text=website.text
soup=BeautifulSoup(website_text)
for link in soup.find_all('a'):
    links.append(link.get('href'))

for link in links:
    print(link)

print(len(links))


