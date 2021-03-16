from bs4 import BeautifulSoup
from urllib.request import urlopen 
from plyer import notification      
import time
import webbrowser

url = 'https://feeds.feedburner.com/TheHackersNews'
website = 'https://thehackernews.com/search/label/Vulnerability'

client = urlopen(url)
xml_data = client.read()
client.close()


soup = BeautifulSoup(xml_data,'xml')
news_list = soup.find_all('item')
news_list = news_list[0:5]
 

for news in news_list:
     notification.notify(title = "Daily News", message=news.title.text + '\nPuplished on :'+news.pubDate.text, timeout=20)
     
webbrowser.open(website, new=1, autoraise=True)    

news_file = open('News_List.txt', 'w')
#novel_file.write(response.text[:178978])
for chunk in news_list:
     news_file.write("Title: ")
     news_file.write(news.title.text)
     news_file.write(news.pubDate.text)
     news_file.write("\nNews Body: ")
     news_file.write(news.text[166:])
     news_file.write("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

news_file.close()

time.sleep(1200)

