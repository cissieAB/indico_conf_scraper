import requests
from bs4 import BeautifulSoup
import pandas as pd

# 26th CHEP
CHEP2023_LINK = 'https://indico.jlab.org/event/459/contributions/'
CHEP2023_LINK_PREFIX = 'https://indico.jlab.org'

# 25th CHEP
CHEP2021_LINK = 'https://indico.cern.ch/event/948465/contributions/'
CERN_PREFIX = 'https://indico.cern.ch'

# 24th CHEP
CHEP2019_LINK = 'https://indico.cern.ch/event/773049/contributions/'

# 23rd CHEP
CHEP2018_LINK = 'https://indico.cern.ch/event/587955/contributions/'

# 22nd CHEP
CHEP2016_LINK = 'https://indico.cern.ch/event/505613/contributions/'


column_heads = ['Year', 'Link', 'Title', 'Authors', 'Attachment']

def get_authors_n_attachment(url, url_prefix):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    def get_authors():
        authors, all_author_str = [], ''
        span_elements = soup.find_all('span', class_='speaker-item icon-user')
        for span_tag in span_elements:
            author_name = span_tag.find('span', class_='').text.strip()
            authors.append(author_name.replace(',', ''))

        # exclude the first author (the speaker) because it appears in the full speaker list again
        for author in authors[1:]:
            all_author_str += author + ', '

        return all_author_str

    def get_attachment():
        attach = soup.find_all('a', attrs={'class': ['attachment icon-file-presentation', 'attachment icon-file-pdf']})
        return url_prefix + attach[0]['href'] if attach else ''

    return get_authors(), get_attachment()

# test
##  CHEP 2023
# print(get_authors_n_attachment('https://indico.jlab.org/event/459/contributions/11472/', CHEP2023_LINK_PREFIX))  # no title
# print(get_authors_n_attachment('https://indico.jlab.org/event/459/contributions/11598/', CHEP2023_LINK_PREFIX))
## CHEP 2022
# print(get_authors_n_attachment('https://indico.cern.ch/event/948465/contributions/4323667/', CHEP2021_LINK_PREFIX))


def get_contrib_of_a_year(url, year_str, url_prefix):
    data = []  # each entry is a dictionary

    # Send a GET request to the URL and get the page content
    response = requests.get(url)
    content = response.content

    # Use BeautifulSoup to parse the page content
    soup = BeautifulSoup(content, "html.parser")

    contrib_tags = soup.find_all('a', {"class": "js-mathjax"})

    for contrib_tag in contrib_tags:
        link = url_prefix + contrib_tag['href']
        title = contrib_tag.text.strip().split('\n')[1].strip()
        authors, attach_link = get_authors_n_attachment(link, url_prefix)

        # append the contribution data to the list
        print(dict(zip(column_heads, [year_str, link, title, authors, attach_link])))
        data.append(dict(zip(column_heads, [year_str, link, title, authors, attach_link])))

    df = pd.DataFrame(data)

    # write the DataFrame to an Excel file
    df.to_csv(f'chep_contrib_{year_str}.csv', index=False)


get_contrib_of_a_year(CHEP2023_LINK, '2023', CHEP2023_LINK_PREFIX)
get_contrib_of_a_year(CHEP2021_LINK, '2021', CERN_PREFIX)
get_contrib_of_a_year(CHEP2019_LINK, '2019', CERN_PREFIX)
get_contrib_of_a_year(CHEP2018_LINK, '2018', CERN_PREFIX)
get_contrib_of_a_year(CHEP2016_LINK, '2016', CERN_PREFIX)
