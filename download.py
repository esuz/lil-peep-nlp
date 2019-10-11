#   Oddly specific lyrics scraper

def read_song_titles(file: str)->str:
    import pandas as pd
    return(pd.read_csv(file, names=['song_name']))

def build_url(file:str)->list:
    """Reads song file and creates urls for scraping"""
    import pandas as pd
    prefix = "https://www.[****CENSORED****].com/lyrics/lilpeep/" 
    # sorry i propably dont have permission to webscrape
    # maybe you can figure out which website i used
    # good luck
    postfix = ".html"
    titles = read_song_titles(file)
    urls = []
    [urls.append(prefix+title+postfix) for title in titles.song_name]
    return(urls)

def scrape_lyrics(url: str)->str:
    from bs4 import BeautifulSoup
    import requests
    import time
    time.sleep(1)
    data  = requests.get(url).text
    soup = BeautifulSoup(data, "lxml")
    return(str(soup.find_all("div", class_=None)))


def clean_up(harvest:str)->str:
    tmp = harvest.split("\n",2)[2]
    tmp = (tmp[:tmp.rfind('\n')])

    import re
    tmp = re.sub('<br>', '', tmp)
    tmp = re.sub('<br/>', '', tmp)
    return(tmp)

def write_result(file: str, lyrics:str):
    with open("./lyrics/" + file + ".txt", "w") as f:
        f.write(lyrics)

urls = build_url("song_titles.txt")
titles = read_song_titles("song_titles.txt")
titles_list = []
[titles_list.append(i) for i in titles.song_name]

for url,title in zip(urls, titles_list):
    lyrics = clean_up(scrape_lyrics(url))
    write_result(title, lyrics)
    print(title)
