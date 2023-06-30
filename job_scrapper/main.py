from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_experimental_option("detach", True)
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# base_url = "https://www.indeed.com/jobs?q="
# search_term = "python"
# response = get(f"{base_url}{search_term}")

browser = webdriver.Chrome(options=options)
browser.get(
    'https://kr.indeed.com/jobs?q=python&l=&from=searchOnHP&vjk=89395b6ac5014113')

print(browser.page_source)
