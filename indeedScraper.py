# https://www.blog.datahut.co/post/scrape-indeed-using-selenium-and-beautifulsoup

from webbrowser import Chrome
from bs4 import BeautifulSoup #Parses and pulls out data from HTML and XML files
from lxml import etree as et #Processes HTML and XML files
from csv import writer
from selenium import webdriver #WebDriver that basically acts as an automated browser via API requests
from webdriver_manager.chrome import ChromeDriverManager #Needed library for selenium to use chrome
import time #will allow the ability to display multiple time formats

# define job and location search keywords
job_search_keyword = ['UX', 'UX+Research', 'UX+Designer']
location_search_keyword = ['Texas', 'New York', 'California']

# define base and pagination URLs
base_url = 'https://www.indeed.com'
pagination_url = 'https://www.indeed.com/jobs?q={}&l={}&radius=35&start={}'

#init Chrome webdriver using ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

#open initial URL
driver.get("https://www.indeed.com/q-USA-jobs.html?vjk=823cd7ee3c203ac3")

# function to get DOM from given URL
def get_dom(url):
   driver.get(url)
   page_content = driver.page_source
   product_soup = BeautifulSoup(page_content, 'html.parser')
   dom = et.HTML(str(product_soup))
   return dom