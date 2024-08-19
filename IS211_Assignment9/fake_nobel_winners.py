from bs4 import BeautifulSoup
import pandas as pd
import requests
from io import StringIO  
# bs4, pandas, lxml, html5lib


def scrape(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


def get_table(soup):
    table = soup.find('table', {'class': 'wikitable'})
    table = str(table)    
    table = StringIO(table)
    return table

    
def clean(df):
    pd.set_option('display.max_rows', None)
    df = df[0][['Year', 
                'Laureate (birth/death)', 
                'PhD (or equivalent) alma mater', 
                'Institution (most significant tenure/at time of receipt)']]
    df. columns = ['Year', 'Winner', 'PhD alma mater', 'Institution']
    blankIndex = [''] * len(df)
    df.index = blankIndex
    return df


def main():
    soup = scrape("https://en.wikipedia.org/wiki/List_of_Nobel_Memorial_Prize_laureates_in_Economic_Sciences")
    table = get_table(soup)
    wiki_df = pd.read_html(table)
    df = clean(wiki_df)
    print(df)


if __name__ == "__main__":
    main()
    