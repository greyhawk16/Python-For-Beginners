from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
# options.add_experimental_option("detach", True)
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(options=options)


def get_page_count(keyword):
    base_url = "https://kr.indeed.com/jobs?q="
    end_url = "&limit=50"
    browser.get(f"{base_url}{keyword}{end_url}")

    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("nav", {"aria-label": "pagination"})
    pages = pagination.select('div a')
    count = len(pages)+1

    for page in pages:
        if (page['aria-label'] == "Previous Page") or (page['aria-label'] == "Next Page"):
            count -= 1

    return min(count, 5)


def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    print('found', pages, ' pages')
    base_url = "https://kr.indeed.com/jobs"
    res = []

    for page in range(pages):
        final_url = f"{base_url}?q={keyword}&start={page*10}"
        browser.get(final_url)

        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        jobs = job_list.find_all("li", recursive=False)

        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")

            if zone == None:
                anchor = job.select_one("h2 a", class_="jobTitle")
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find('span', class_='companyName')
                location = job.find('div', class_='companyLocation')

                job_data = {
                    'link': f"https://kr.indeed.com{link}",
                    'company': company.string.replace(",", " "),
                    "location": location.string.replace(",", " "),
                    'position': title.replace(",", " "),
                }
                res.append(job_data)

    return res
