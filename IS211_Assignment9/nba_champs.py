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
    table = soup.find_all('table', {'class': 'wikitable'})[1]
    # remove the rows that demarcate bba and nba era winners 
    bba_col = table.tbody.find_all('tr')[1]
    nba_col = table.tbody.find_all('tr')[5]
    bba_col.decompose()
    nba_col.decompose()
    table = str(table)    
    table = StringIO(table)
    return table

    
def clean(df):
    pd.set_option('display.max_rows', None)
    df = df[0][['Year', 
                'Western champion', 
                'Coach', 
                'Result',
                'Eastern champion',
                'Coach.1',
                'Finals MVP[a]']]
    df. columns = ['Year', 'Western Champion', 'W. Coach', 'Result', 'Eastern Champion', 'E. Coach', 'Finals MVP']
    blankIndex = [''] * len(df)
    df.index = blankIndex
    return df


def main():
    soup = scrape("https://en.wikipedia.org/wiki/List_of_NBA_champions")
    table = get_table(soup)
    wiki_df = pd.read_html(table)
    df = clean(wiki_df)
    print(df)


if __name__ == "__main__":
    main()
    