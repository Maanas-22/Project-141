from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser=webdriver.Chrome(".\chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scraped_data=[]

def scrape():
    soup=BeautifulSoup(browser.page_source, "html.parser")
    table=soup.find("table", attrs={"class","wikitable"})
    tbody_tag=table.find("tbody")
    tr_tags = tbody_tag.find_all("tr")
    for row in tr_tags:
        td_tags=row.find_all("td")
        temp_list=[]
        for td_data in td_tags:

            data=td_data.text.strip()

            temp_list.append(data)
        scraped_data.append(temp_list)


scrape()

stars_data = []

for i in range(len(scraped_data)):
    Stars_names=scraped_data[i][1]
    Dist=scraped_data[i][3]
    Mass=scraped_data[i][5]
    Radius=scraped_data[i][6]
    Lum=scraped_data[i][7]
    
    required_data = [Stars_names, Dist, Mass, Radius, Lum]
    stars_data.append(required_data)

header=["Name", "Distance", "Mass", "Radius", "Luminosity"]

star_df=pd.DataFrame(stars_data,columns=header)

star_df.to_csv('stars.csv',index=True, index_label="id")

