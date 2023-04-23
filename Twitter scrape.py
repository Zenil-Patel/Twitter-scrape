from bs4 import BeautifulSoup
from selenium import webdriver
import time

PATH = ' C:/Program Files/Google/Chrome/Application/chrome.exe'

output=[]
temp={}

print('Enter the twitter URL:')
target_url =  input()

driver=webdriver.Chrome(PATH)

try:
    driver.get(target_url)
    time.sleep(2)

    response = driver.page_source
    soup=BeautifulSoup(response,'html.parser')

    temp["Profile"]=soup.find("div",{"class":"r-1wvb978"}).text
    temp["Biography"]=soup.find("div",{"data-testid":"UserDescription"}).text
    temp["following_count"]=soup.find_all("a",{"class":"r-rjixqe"})[0].text
    temp["followers_count"]=soup.find_all("a",{"class":"r-rjixqe"})[1].text
    temp["number_of_tweets"]=soup.find("div",{"class":"r-1bwzh9t"}).text

    output.append(temp)
    print(output)

except:
    print("URL Not found")
    
finally:
    driver.close()