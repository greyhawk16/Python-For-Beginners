from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

jobs = extract_wwr_jobs('python')
for j in jobs:
    print(j) 