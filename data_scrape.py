import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup
# url = "https://www.foxnews.com/lifestyle/jack-carrs-eisenhower-d-days-memo-noble-undertaking"
# response = requests.get(url)
# if response.status_code != 200:
#     raise Exception(f"Failed to load page: Status code {response.status_code}")
titles = {}
skipped = []
# get all of the links
with open('url_only_data.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)
    i = 0
    for row in reader:
        # if i > 10:
        #     break
        i += 1
        print(f"Link scraped: {row[0]} \n{i}")
        response = requests.get(row[0])
        if response.status_code != 200:
            print(f"Failed to load page: Status code {response.status_code}")
        
        # To find nbc
        # article-hero-headline__htag lh-none-print black-print
        # nbc cards
        # p tag -> headline-title-text
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        potential_classes = ['headline speakable', 'article-hero-headline__htag']
        title = soup.find("h1", class_=potential_classes)
        if (title):
            titles[row[0]] = title.get_text()
            print('GOT title')
        else:
            last_6 = row[0][-6:]
            if last_6 == ".print":
                title = soup.find("h1")
                if (title):
                    titles[row[0]] = title.get_text()
                    print('GOT print title!', title)
                else:
                    print('skipped in loop!!!')
                    skipped.append(row)
            else:
                print('skipped!!!')
                skipped.append(row)
    
df = pd.DataFrame(list(titles.items()), columns=['url', 'headline'])
df.to_csv('data/news_headlines.csv', index=False)
df_skipped = pd.DataFrame(skipped, columns=['url'])
df_skipped.to_csv('data/skipped_headlines.csv', index=False)
#print(titles)


# title should be the following
# Juan Soto sends the Yankees to the World Series for the first time in
# 15 years