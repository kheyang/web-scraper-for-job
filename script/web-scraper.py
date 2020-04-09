# 2.1 Import Requests
import requests
# 3.2 Import Beautiful Soup
from bs4 import BeautifulSoup

# 2.2 Perform HTTP Request to an URL
URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

# 3.2 Create a Beautiful Soup Object
soup = BeautifulSoup(page.content, 'html.parser')

# 3.4 Filter Out Specific Element by its ID
results = soup.find(id='ResultsContainer')

# print(results.prettify())

# 3.5 Find Elements by HTML Class Name
job_elems = results.find_all('section', class_='card-content')

"""
This part is to scrape all job information
# 3.6 Extract Text from HTML Elements & Clear White Spaces
for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print() 
"""

# 4.2 Filter Out Content of Interests
python_jobs = results.find_all('h2', string=lambda text: 'python' in text.lower())

for python_job in python_jobs:
    # 4.3 Extract Attribute from HTML Elements
    link = python_job.find('a')['href']
    print(python_job.text.strip())
    # the "f" in front of the statement is to validate the link
    print(f"Apply here: {link}")