import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import PDFtoString3

url = "https://www.americanrhetoric.com/top100speechesall.html"

# Search for the path where your Scrapytutorial folder is (obviously not diegoponce).Has to be in same Folder path otherwise it will give an directory error
folder_location = r"/Users/diegoponce/Desktop/TCMFinalProjectDiegoPonce"
if not os.path.exists(folder_location):os.mkdir(folder_location)

response = requests.get(url)
soup= BeautifulSoup(response.text, "html.parser")
for link in soup.select("a[href$='.pdf']"):

    # The PDF will be named based on the last portion of its link
    filename = os.path.join(folder_location,link['href'].split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url,link['href'])).content)

PDFtoString3.pdf_to_text()
