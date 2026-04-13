import requests
from bs4 import BeautifulSoup
url = https://www.foxnews.com/sports/juan-soto-sends-yankees-worldseries-first-time-15-years # example website
response = requests.get(url)
if response.status_code != 200:
raise Exception(f"Failed to load page:
Status code {response.status_code}")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("h1", class_="headline speakable")

# title should be the following
# Juan Soto sends the Yankees to the World Series for the first time in
# 15 years